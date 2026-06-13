# ex02_hello_api.py
# 这是给你「读 + 跑」的示例，演示一个最小的 API 服务器长什么样。
# 和你刚写的 cli_recall.py 最大的不同：
#   - cli_recall.py：跑一次 → 做完 → 退出。
#   - API 服务器：  一直开着，等别人来"敲门"(发请求)，敲一次答一次。

from fastapi import FastAPI    # FastAPI = 帮你快速搭 API 的框架(厨房里的工作台)

app = FastAPI()                # 造一个 app，它就是你的服务器本体

# 下面这行 @app.get("/health") 叫"装饰器"(decorator)。
# 意思是："如果有人访问 /health 这个地址，就运行下面这个函数。"
@app.get("/health")
def health():
    return {"status": "ok"}    # 返回字典，FastAPI 会自动变成 JSON 发回去

# {name} 是地址里会变化的一段，它会被塞进下面函数的 name 参数。
# 访问 /hello/dan  →  name 就是 "dan"
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"你好, {name}!"}
