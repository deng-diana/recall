# test_leitner.py — 人生第一个自动化测试。
# 运行方式:在 recall 文件夹里敲   pytest
from ex06_leitner import schedule

# 一个测试 = 调用你的函数 + 用 assert 断言结果是不是你期望的。
# assert 后面条件为真 → 这条过(绿);为假 → 失败(红)并告诉你哪错了。

def test_correct_moves_up():
    new_box, due = schedule(2, True)   # 盒 2 答对
    assert new_box == 3                # 期望:升到盒 3


# 👇 你来写:盒 5 答对,应该还是 5(封顶)
def test_box5_caps():
    new_box,due=schedule(5, True)
    assert new_box == 5
    ...   # 仿照上面:调用 schedule(5, True),断言 new_box == 5


# 👇 你来写:盒 1 答错,应该还是 1
def test_wrong_resets():
    new_box, due=schedule(1, False)
    assert new_box==1
   # 调用 schedule(1, False),断言 new_box == 1
