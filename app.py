from multiprocessing import allow_connection_pickling
from dotenv import load_dotenv
import anthropic
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
import sqlite3
from ex06_leitner import schedule 
 
load_dotenv()
client=anthropic.Anthropic()


app = FastAPI()
app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:3000"],  # 允许前端这个地址来访问
      allow_methods=["*"],                       # 允许所有方法(GET/POST...)
      allow_headers=["*"],
  )
def get_conn():
    #小助手:每次要用数据库就叫它开个连接
    conn=sqlite3.connect("recall.db")
    conn.row_factory=sqlite3.Row
    return conn

# 数据保安:要求"创建新卡"时,对方必须按这个格式给数据,缺字段自动打回
class CardIn(BaseModel):
    front:str
    back:str
    branch: str

class Quiz(BaseModel):
    question:str
    answer:str
    difficulty: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/cards")
def list_cards():
    conn=get_conn()
    rows=conn.execute("SELECT * FROM cards").fetchall()
    conn.close()
    # 每行转字典,FastAPI 自动变 JSON
    return [dict(r) for r in rows]


@app.get("/cards/{card_id}")
def get_cards(card_id: int):
    conn=get_conn()
    row=conn.execute("SELECT * FROM cards WHERE id=?",(card_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="找不到这张卡")
    return dict(row)
    
   
    
@app.post("/cards", status_code=201)
def create_card(card: CardIn):
   conn=get_conn()
   cur=conn.execute("INSERT INTO cards (front, back, branch) VALUES (?,?,?)",(card.front, card.back, card.branch))
   conn.commit()
   conn.close()
   new_id=cur.lastrowid
   return f"item added, the id is {new_id}"

@app.post("/ai/generate-cards", status_code=201)
def generate_card(topic:str):
    resp=client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[{"role":"user", "content": f"为{topic}这个知识点出一道复习题."}],
        output_format=Quiz
    )
    quiz=resp.parsed_output
    conn=get_conn()
    cur=conn.execute("INSERT INTO cards (front, back, branch) VALUES(?,?,?)",(quiz.question, quiz.answer, "ai"))
    conn.commit()   
    conn.close()
    new_id=cur.lastrowid
    return {"id":new_id, "front":quiz.question, "back":quiz.answer, "branch":"ai" }

@app.post("/cards/{card_id}/review")
def review_card(card_id: int, correct: bool):
    conn=get_conn()
    row=conn.execute("SELECT * FROM cards WHERE id=?", (card_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="not found")
    new_box,due=schedule(row["box"], correct)
    conn.execute("UPDATE cards SET box=?, due_date=? WHERE id=?",(new_box,due,card_id))
    conn.commit()
    conn.close()
    return {"id": card_id, "box": new_box, "due_date":due}


@app.delete("/cards/{card_id}")
def delete_card(card_id:int):
    conn=get_conn()
    id=card_id
    cur=conn.execute("DELETE FROM cards WHERE id=?", (id,))
    conn.commit()
    conn.close()
    if cur.rowcount==0:
        raise HTTPException(status_code=404,detail="no items founded")
    
    return "deleted succefuly"

    