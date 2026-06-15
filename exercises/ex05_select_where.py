# ex05_select_where.py — 读懂 + 跑。WHERE:给查询加"只要符合条件的行"。
# 这个脚本只读不写,跑几次都安全。
import sqlite3

conn = sqlite3.connect("recall.db")

# 1) 不加条件:取全部
print("全部卡:")
for row in conn.execute("SELECT id, front, branch FROM cards").fetchall():
    print("  ", row)

# 2) 加 WHERE:只取 branch = 'fe' 的行
#    查询里也用 ? 占位符(筛选值同样别拼字符串)
branch = "fe"
print(f"只要 branch = '{branch}' 的:")
for row in conn.execute(
    "SELECT id, front FROM cards WHERE branch = ?", (branch,)
).fetchall():
    print("  ", row)

conn.close()
