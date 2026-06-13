import sqlite3

conn=sqlite3.connect("recall.db")

conn.execute("INSERT INTO cards (front, branch) VALUES (?, ?)",
("Pydantic", "py"))
conn.execute("INSERT INTO cards (front, branch) VALUES (?, ?)",
("SQL injection", "db"))
conn.commit()

branch="db"


for row in conn.execute(
    "SELECT id, front From cards WHERE branch=?", 
    (branch,)).fetchall():
        print(row)