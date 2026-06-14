# ex06_leitner.py — Leitner 间隔重复引擎(纯函数,Recall 的灵魂)。读懂 + 跑。
from datetime import date, timedelta

# 盒子 → 隔几天再复习。盒子越高 = 记得越牢 = 间隔越长。
INTERVALS = {1: 1, 2: 2, 3: 4, 4: 7, 5: 15}

def schedule(box, correct):
    """给一张卡当前的盒子 + 这次答对没,算出 (新盒子, 下次复习日期)。"""
    if correct:
        new_box = min(box + 1, 5)   # 答对:升一盒,最高到 5(min 防止超过 5)
    else:
        new_box = 1                 # 答错:打回盒 1,很快再考
    days = INTERVALS[new_box]                     # 查"这个盒子隔几天"
    due = date.today() + timedelta(days=days)     # 今天 + N 天 = 下次复习日
    return new_box, due.isoformat()               # 例:(3, "2026-06-18")

# 跑几个例子看看(纯函数最好测:给输入,看输出)
if __name__=="__main__":

    print(schedule(2, True))    # 盒 2 答对 → 盒 3
    print(schedule(5, True))    # 盒 5 答对 → 还是 5(封顶)
    print(schedule(4, False))   # 盒 4 答错 → 回盒 1
