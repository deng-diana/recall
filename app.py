from fastapi import FastAPI
import json

app = FastAPI()

with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/cards")
def get_cards():
    # FastAPI 用函数名作为路由的 "operationId"，这里用 get_cards 比较规范
    return cards  # 注意这里变量名 cards 和函数名不能同名，否则会覆盖卡片数据
