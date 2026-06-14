# ex08_quiz_generator.py — AI 出题官:让 Claude 稳定吐出"结构化"的题目。读懂 + 跑。
from dotenv import load_dotenv
load_dotenv()
import anthropic
from pydantic import BaseModel

client = anthropic.Anthropic()

# 1. 声明你要的"形状"(还是 Pydantic,你 Day 2 学过)。Claude 必须按这个吐。
class Quiz(BaseModel):
    question: str        # 题目
    answer: str          # 答案
    difficulty: int      # 难度 1-5

# 2. 用 .parse()(不是 .create())—— 它强制 Claude 按 Quiz 结构返回,并自动校验
resp = client.messages.parse(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "为'什么是 API'这个知识点出一道复习题。"},
    ],
    output_format=Quiz,      # ← 关键:指定输出形状(这是 .parse() 的入参)
)

# 3. resp.parsed_output 已经是验证过的 Quiz 对象,不用手动 json.loads!
quiz = resp.parsed_output
print("题目:", quiz.question)
print("答案:", quiz.answer)
print("难度:", quiz.difficulty)
print("\n用量:", resp.usage)
