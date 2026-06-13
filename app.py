from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
 
# 数据保安:要求"创建新卡"时,对方必须按这个格式给数据,缺字段自动打回
class CardIn(BaseModel):
    front:str
    back:str
    branch: str


app = FastAPI()

with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/cards")
def list_cards():
    return cards

@app.get("/cards/{card_id}")
def get_cards(card_id: int):
    for card in cards: 
        if card["id"]==card_id:
            return card
    raise HTTPException(status_code=404, detail="找不到这张卡")
   
    
@app.post("/cards", status_code=201)
def create_card(card: CardIn):
    new_id=len(cards)+1
    new_card={"id": new_id, "front": card.front, "back": card.back, "branch": card.branch }
    cards.append(new_card)
    return new_card

@app.delete("/cards/{card_id}")
def delete_card(card_id:int):
    for card in cards:
        if card["id"]==card_id:
            cards.remove(card)
            return {"deleted":card_id}
    raise HTTPException(status_code=404,detail="no items founded")