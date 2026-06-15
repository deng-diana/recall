# ex01_load_cards.py
# 这是给你「读」的示例，不是让你抄。读懂它，待会你写自己的版本。
# 目标：把 cards.json 读进来，挨个打印每张卡的正面 + 它属于哪个分支。

import json   # json 是 Python 自带的工具，专门读 / 写 JSON 数据

# open(...) 打开文件；"r" = read（只读）；encoding="utf-8" 保证中文不乱码
# with ... as f:  用完自动关门，不用手动关文件
with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)   # 把文件里的 JSON 文字，变成 Python 能用的列表

# 现在 cards 是一个列表（list），里面每个元素是一张卡（字典 dict）
for card in cards:                  # 一张一张地过
    front = card["front"]           # 取出这张卡的正面文字
    branch = card["branch"]         # 取出它的分支（py / fe / db ...）
    print(f"[{branch}] {front}")    # f"..." 把变量塞进字符串里一起打印

print(f"\n一共 {len(cards)} 张卡")   # len(...) 数一数列表有多长
