# ex04_insert_select.py — 读懂 + 跑。往表里存卡(INSERT)+ 读卡(SELECT)。
import sqlite3

conn = sqlite3.connect("recall.db")

# ---- INSERT:存一张卡 ----
# 注意那几个 ? —— 这叫"占位符"。真正的值放在后面的元组里,按顺序对上。
# id 不用写,PRIMARY KEY 会自动编号。
conn.execute(
    "INSERT INTO cards (front, back, branch) VALUES (?, ?, ?)",
    ("React", "一个做界面的 JS 库", "fe"),   # 这三个值依次填进上面三个 ?
)
conn.commit()   # 别忘了存盘

# ---- SELECT:把卡读出来 ----
# SELECT 列名 FROM 表名 —— "从 cards 表里,取这几列"
rows = conn.execute("SELECT id, front, branch FROM cards").fetchall()
for row in rows:
    print(row)   # 每个 row 是一个元组,像 (1, 'React', 'fe')

conn.close()
