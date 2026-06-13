# ex03_db_intro.py — 读懂 + 跑。SQLite:一个文件就是一个数据库。
import sqlite3   # Python 自带,不用安装

# connect 打开数据库文件 recall.db(不存在就新建一个)
conn = sqlite3.connect("recall.db")

# 建一张表 cards,像定义电子表格的表头:
#   id     = 编号(PRIMARY KEY 主键:每行唯一的身份证)
#   front  = 正面文字(TEXT 文本;NOT NULL 不能为空)
#   back   = 背面文字
#   branch = 分支(py / fe / db ...)
conn.execute("""
CREATE TABLE IF NOT EXISTS cards (
    id      INTEGER PRIMARY KEY,
    front   TEXT NOT NULL,
    back    TEXT,
    branch  TEXT
)
""")

conn.commit()   # 提交:把改动真正写进硬盘文件(=存盘)
conn.close()    # 关门
print("建表成功!看看文件夹,多了一个 recall.db 文件 —— 它就是你的数据库。")
