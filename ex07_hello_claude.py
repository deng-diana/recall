# ex07_hello_claude.py — 你人生第一个 Claude API 调用。读懂 + 跑。
from dotenv import load_dotenv
load_dotenv()                      # 把 .env 里的 ANTHROPIC_API_KEY 加载进"环境变量"
import anthropic

client = anthropic.Anthropic()     # 不用填 key,它自动从环境变量读 ANTHROPIC_API_KEY

resp = client.messages.create(
    model="claude-haiku-4-5",      # 最便宜最快的模型
    max_tokens=200,                # 限制输出长度 = 控制成本
    messages=[
        {"role": "user", "content": "用一句话解释什么是 API"},
    ],
)

# 回复 resp.content 是一串"块"(block),取出文字块打印
for block in resp.content:
    if block.type == "text":
        print(block.text)

# 看这次花了多少 token(成本意识)
print("\n用量:", resp.usage)
