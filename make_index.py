import sqlite3
conn=sqlite3.connect("recall.db")
conn.execute("CREATE INDEX IF NOT EXISTS idx_reviews_card_id ON reviews(card_id)")
conn.commit()
conn.close()
print("索引建好了!")