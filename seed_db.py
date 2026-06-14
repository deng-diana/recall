# seed_db.py — 把 cards.json 的 30 张卡灌进数据库(干净重建)。读懂 + 跑。
import sqlite3, json

conn = sqlite3.connect("recall.db")

# 干净重建:先删旧表(连之前的测试垃圾一起清掉),再按 Leitner 需要的结构建新表
conn.execute("DROP TABLE IF EXISTS cards")     # DROP = 删表
conn.execute("""
CREATE TABLE cards (
    id        INTEGER PRIMARY KEY,
    front     TEXT NOT NULL,
    back      TEXT,
    branch    TEXT,
    box       INTEGER DEFAULT 1,    -- Leitner 盒子(1-5),默认从 1 开始
    due_date  TEXT                  -- 下次复习日期
)
""")

# 读 cards.json,逐张插入(值放第二个参数 —— 你刚学的)
with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

for c in cards:
    conn.execute(
        "INSERT INTO cards (id, front, back, branch, box, due_date) VALUES (?, ?, ?, ?, ?, ?)",
        (c["id"], c["front"], c["back"], c["branch"], c["box"], c["due_date"]),
    )

conn.commit()
n = conn.execute("SELECT COUNT(*) FROM cards").fetchone()[0]   # COUNT(*) = 数行数
conn.close()
print(f"灌入完成,数据库里现在有 {n} 张卡")
