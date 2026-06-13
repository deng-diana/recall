import json
from fastapi import FastAPI

app=FastAPI()

with open ("cards.json", "r", encoding="utf-8") as f:
    cards=json.load(f)

@app.get("/cards")
def get_cards():
    return cards