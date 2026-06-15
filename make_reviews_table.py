import sqlite3

conn=sqlite3.connect("recall.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY,
    card_id INTEGER NOT NULL REFERENCES cards(id),
    correct INTEGER NOT NULL,
    review_at TEXT NOT NULL)
""")
conn.commit()
conn.close()
print("reviews 表建好了!")