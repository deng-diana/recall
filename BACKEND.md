# 《后端工程基础 · 集训课》(BACKEND.md)

> 给 Dan 的拓展加固课。目标:打牢**可迁移的后端判断力** + 留下一套挂在 Recall 上、能自己往下练的真系统。
> 诚实边界:几天不会把你变 senior。这门课给你的是**判断力 + 词汇表 + 能跑能讲的 Demo**,足够让你面 mid-level 时言之有物。

**记号**:🔥 核心必学　⏳ 进阶可延后　⭐ 面试高频(越多越常被问)

---

## ① 一页课程地图

> 这页给谁看:每次迷路了回这看"我在哪、为什么学这个"。

你今天会的:HTTP 请求-响应、跑通 FastAPI、一个 GET 接口。我们从这里**只往外推一圈**,每圈挂在 Recall 上。
三条主线:**Comms**=通信协议　**Arch**=系统架构　**AI**=AI 后端。

| 模块 | 主线 | 核心问题(一句话) | 面试权重 | 挂到 Recall 的实操 |
|---|---|---|---|---|
| M0 你在哪 | — | 一个请求从浏览器到数据库再回来,经过哪些站 | ⭐ | 画一张 Recall 请求路径图 |
| M1 HTTP + REST 🔥 | Comms | 好接口长什么样:方法/状态码/幂等 | ⭐⭐⭐ | `/v1/cards` 分页 + 统一错误 |
| M2 数据库 + SQL 🔥 | Arch | 把卡片存进**真数据库**,会查会改 | ⭐⭐⭐ | 建 `cards` 表 + 查"今天到期" |
| M3 ORM + 建模 🔥 | Arch | 用 Python 对象操作表,设计表关系 | ⭐⭐⭐ | 卡片 + 复习记录两张表 |
| M4 校验 + 错误 🔥 | Comms | 入参校验(Pydantic)、统一错误 | ⭐⭐ | 给写接口加校验 |
| M5 认证授权 🔥 | Arch | 谁能动谁的卡:哈希、JWT | ⭐⭐⭐ | JWT 登录 + "只能动自己的卡" |
| M6 异步 + 后台任务 🔥 | Comms | 慢活儿丢后台,接口立刻返回 | ⭐⭐ | "出下一题"丢 BackgroundTask |
| M7 缓存 + 性能 🔥 | Arch | 慢在哪、加索引、N+1、缓存 | ⭐⭐⭐ | 索引 + 修 N+1 + cache-aside |
| M8 AI 后端 I 🔥 | AI | 安全地调 Claude 出题:流式/重试/计费 | ⭐⭐ | 流式 AI 出题官 |
| M9 AI 后端 II ⏳ | AI | 工具调用 / 结构化输出 / RAG / 评估 | ⭐⭐ | 结构化出题 + LLM 评分 |
| M10 通信形态全景 🔥 | Comms | WebSocket/SSE/gRPC/Webhook 各用在哪 | ⭐⭐⭐ | 选型判断(讲,不全做) |
| M11 上线工程 ⏳ | Arch | 迁 Postgres、日志、测试、Docker | ⭐⭐ | 结构化日志 + /health + 测试 |
| M12 顶石 🔥 | 全部 | 串起来,能对面试官讲清取舍 | ⭐⭐⭐ | 端到端跑通 + 讲故事 |

**学习顺序(谁解锁谁)**

主链(按顺序走):**M0 → M1 → M2 → M3 → M4 → M5 → M6 → M7 → M8 → M9 → M11 → M12**

旁支:学完 **M6** 后,**M10**(通信形态全景)也解锁了,可随时插进来学。

| 模块 | 学它前要先会 |
|---|---|
| M7 缓存性能 | M2、M3(先有数据库才谈优化) |
| M8 AI 后端 I | M5、M6(先有密钥管理 + 后台任务) |
| M10 通信全景 | M6 |

**读多于憋的分配**:M2/M3/M5/M8/M9 是你最弱的(数据库零动手、AI 只有概念)→ 样例最多、引导最足。M1/M6 你有概念 → 快速跳过式。

---

## ② 怎么学这门课(≤3 段)

**主循环(已验证有效)**:读懂带逐行注释的完整样例 → 合上代码用大白话讲回来(费曼,讲给"小黄鸭"听)→ 参考着自己敲(**禁复制粘贴**)→ 次日合上参考从零重写核心片段。新/难概念给足样例,**绝不冷启动硬憋**;会的基础快速跳过。

**认知负荷规则(阅读障碍适配)**:每模块**新概念 ≤ 3 个**;代码块 ≤ 15 行(超了切成带标题的小块);优先级 **图 > 表 > 短句 > 段落**;缩写首次出现给全称 + 一句大白话(见 §缩写表)。**信号灯**:讲回来卡壳 = 黄灯(重读样例);敲代码偷看超 3 次 = 红灯(退回上一模块,别夹生)。

**两类内容自检**:表格如果标了"📖 只扫读"= **别背**,只要看懂能查;标了"✍️ 学习点"= 要能讲会敲。每个模块结束:存 1 张卡进你自己的 Recall(顺便体验产品),次日抽卡复习。

---

## ③ 模块逐节展开

> 每节统一模板:**目标 / 读什么样例 / 讲回来检验 / Recall 实操 / 过关标准 / 存 1 张卡**。

---

### M0 · 你在哪:请求的一生 🔥

**目标(一句话)**:画出"浏览器点一下 → 到 Recall 服务器 → 到数据库 → 返回"的完整路径站点。

**读什么样例**:一张文字流程图。
```
浏览器  → [HTTP 请求] → FastAPI 路由 → 校验入参 → 查数据库 → 组装 JSON → [HTTP 响应] → 浏览器
                                   ↑ 你今天会到这                  ↑ 这门课要补
```
> HTTP = HyperText Transfer Protocol,超文本传输协议 — 浏览器和服务器说话的"礼貌用语规则"。
> JSON = JavaScript Object Notation — 一种大家都看得懂的"数据打包格式",像 `{"名字": "卡片1"}`。

**讲回来检验**:用大白话说出每一站在干嘛,以及"你今天卡在哪一站"。

**Recall 实操**:把这张图画在纸上,标出"我已经会"和"要学"的站。

**过关标准**:能不看图复述这条链路。

**该存的 1 张卡**:正面"一个请求经过哪 5 站?" 反面:请求→路由→校验→数据库→响应。

---

### M1 · HTTP 深一层 + REST 设计 🔥 ⭐⭐⭐

**目标**:给 Recall 设计一组"别人一看就懂"的接口:对的 HTTP 方法、对的状态码、分页、幂等。

> REST = Representational State Transfer — 一套"用网址表示东西(资源)、用动词表示动作"的约定。
> API = Application Programming Interface,应用程序接口 — 两个程序之间说话的"菜单"。

**📖 只扫读 — 状态码速查(别背,会查就行)**

| 码 | 意思 | 何时 |
|---|---|---|
| 200 / 201 | 成功 / 已创建 | GET 成功 / POST 建好了 |
| 400 / 401 / 403 | 你传错了 / 没登录 / 没权限 | 客户端的锅 |
| 404 / 409 | 找不到 / 冲突 | 资源不在 / 重复创建 |
| 500 | 服务器自己崩了 | 我的锅 |

**✍️ 学习点 — HTTP 方法 + 幂等**

| 方法 | 干啥 | 幂等? |
|---|---|---|
| GET | 读 | ✅ 读 10 次结果一样 |
| POST | 建 | ❌ 建 10 次 = 10 张卡 |
| PUT | 整体改 | ✅ |
| DELETE | 删 | ✅ |

> 幂等性(idempotency,"重复无害性")= 同一请求做 10 次 = 做 1 次的结果。
> POST 不幂等,所以**网络重试会重复扣钱 / 重复建卡**。解法:客户端带一个 `Idempotency-Key`(幂等键)头,服务端记下"这个 key 处理过了"就返回旧结果。支付/下单系统的命根子。

**读什么样例**(分页 + 幂等键,≤15 行):
```python
# 内存字典先记 key(真项目用 Redis/数据库)
seen_keys = {}

@app.post("/v1/cards", status_code=201)
def create_card(card: dict, idempotency_key: str | None = None):
    # 同一个 key 来过 → 直接还旧结果,不重复建
    if idempotency_key and idempotency_key in seen_keys:
        return seen_keys[idempotency_key]
    new = {"id": 1, **card}                 # 真项目这里写数据库
    if idempotency_key:
        seen_keys[idempotency_key] = new
    return new

@app.get("/v1/cards")                       # 分页:别一次返回一万条
def list_cards(limit: int = 20, offset: int = 0):
    return {"items": [], "limit": limit, "offset": offset}
```

**讲回来检验**:"为什么 POST 要幂等键,GET 不用?" "limit/offset 是干嘛的?"

**Recall 实操**:给 Recall 加 `GET /v1/cards?limit=20&offset=0` + 统一错误 JSON(`{"error": "...", "code": "..."}`) + `POST /v1/cards` 带幂等键(内存字典即可)。

**过关标准**:能独立写出分页接口 + 解释一个幂等场景。

**该存的 1 张卡**:正面"重试 POST 怎么不重复建卡?" 反面:Idempotency-Key,服务端记 key 返回旧结果。

---

### M2 · 数据持久化:SQLite + SQL 🔥 ⭐⭐⭐

**目标**:把卡片存进**真数据库**,会用 SQL 查出"今天到期的卡"。这是你最弱、优先级最高的一节,样例占比最大。

> SQL = Structured Query Language — 跟数据库要数据的"问话语言"。
> SQLite = 一个**一个文件就是一个数据库**的超轻量数据库,零安装,适合起步。

**读什么样例**(建表 + 安全查询,≤15 行):
```python
import sqlite3
conn = sqlite3.connect("recall.db")

# 建表:卡片有 id、正面、下次复习时间
conn.execute("""CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY,
    front TEXT NOT NULL,
    next_review_at TEXT
)""")

# 查"今天到期":注意那个 ? —— 这是"参数化查询"
today = "2026-06-13"
rows = conn.execute(
    "SELECT id, front FROM cards WHERE next_review_at <= ?", (today,)
).fetchall()
```
> ⚠️ 那个 `?` 是**参数化查询(parameterized query)**:把用户输入当"数据"塞进去,**不拼字符串**。拼字符串会被 SQL 注入攻击(坏人输入 `'; DROP TABLE cards;--` 把表删了)。M5 会再讲。

**讲回来检验**:"`?` 为什么比用 f-string 拼 SQL 安全?" "WHERE 是干嘛的?"

**Recall 实操**:
1. 建 `cards` 表,插几张卡。
2. 写 SQL 查出"今天到期的卡"。
3. (引出 M7)用 `EXPLAIN QUERY PLAN` 看这条查询走没走索引 —— 先记住这个词,M7 加索引。

**过关标准**:能从零建表 + 写出带 `WHERE ... <= ?` 的查询。

**该存的 1 张卡**:正面"SQL 里的 `?` 是什么、防什么?" 反面:参数化查询,防 SQL 注入。

---

### M3 · ORM + 数据建模 🔥 ⭐⭐⭐

**目标**:用 Python 对象代替手写 SQL,设计 Recall 的两张表关系(卡片 ↔ 复习记录)。

> ORM = Object-Relational Mapping,对象关系映射 — 让你用 Python 对象代替手写 SQL 的"翻译层"。写 `card.front` 而不是 `SELECT front ...`。
> CRUD = Create / Read / Update / Delete — 增、查、改、删四件基本事。

**读什么样例**(SQLModel,≤15 行):
```python
from sqlmodel import SQLModel, Field

class Card(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    front: str
    next_review_at: str | None = None

class Review(SQLModel, table=True):   # 复习记录:哪张卡、什么时候复习的
    id: int | None = Field(default=None, primary_key=True)
    card_id: int = Field(foreign_key="card.id")   # 外键:指向某张卡
    grade: int                                     # 这次记得多牢(0-5)
```
> 外键(foreign key)= 一张表里指向另一张表某行的"链接"。这里 `Review.card_id` 指向 `Card.id`,表示"这条复习记录属于哪张卡"。

**讲回来检验**:"ORM 帮你省了什么?" "外键把哪两张表连起来了?"

**Recall 实操**:用 ORM 做卡片的增删改查 + 一条"某张卡的所有复习记录"关联查询。

**过关标准**:能独立设计两张关联表 + 跑通 CRUD。

**该存的 1 张卡**:正面"外键是干嘛的?" 反面:一张表指向另一张表某行的链接,表达"属于"关系。

---

### M4 · 请求校验 + 统一错误 🔥 ⭐⭐

**目标**:用 Pydantic 校验入参,任何错误都返回统一格式的 JSON。

> Pydantic = FastAPI 自带的"数据保安" — 你声明字段类型,它自动挡住不合法的输入。

**读什么样例**(≤15 行):
```python
from fastapi import HTTPException
from pydantic import BaseModel, field_validator

class CardIn(BaseModel):
    front: str
    @field_validator("front")
    def not_empty(cls, v):
        if not v.strip():
            raise ValueError("front 不能为空")   # 自动变成 422 错误
        return v

@app.post("/v1/cards")
def create(card: CardIn):                          # 类型不对 FastAPI 自动挡
    if len(card.front) > 500:
        raise HTTPException(400, detail="卡片太长了")  # 主动报错
    return {"id": 1, "front": card.front}
```

**讲回来检验**:"校验放在哪一步?(看 M0 的图)" "422 和 400 区别?"

**Recall 实操**:给 `POST /v1/cards` 加 Pydantic 校验 + 全局统一错误返回(`{"error": ..., "code": ...}`)。

**过关标准**:乱传输入时,接口返回干净的错误 JSON 而不是崩溃。

**该存的 1 张卡**:正面"Pydantic 在请求生命周期里干嘛?" 反面:在进业务逻辑前挡住不合法输入。

---

### M5 · 认证与授权 🔥 ⭐⭐⭐

**目标**:实现注册/登录,保护"只能动自己的卡"。

> 认证(Authentication)= 你是谁。授权(Authorization)= 你能干啥。两件不同的事。
> JWT = JSON Web Token,JSON 网络令牌 — 一张**带防伪签名的通行证**,服务端不用存,自己验签就行。

**📖 只扫读 — session vs JWT(会讲对比即可)**

| | Session(会话) | JWT |
|---|---|---|
| 大白话 | 钥匙存服务端 | 自带签名的通行证,服务端不存 |
| 好处 | 容易撤销 | 无状态、好扩展 |
| 代价 | 服务端要存 | 签发后难撤销 → 配短过期 + 刷新令牌 |

**✍️ 学习点 — 读这个样例(≤15 行)**:
```python
import jwt, os                                  # PyJWT 库
from fastapi import Depends, HTTPException

SECRET = os.getenv("JWT_SECRET")                # 密钥从环境变量读,绝不进 Git

def make_token(user_id: int) -> str:
    return jwt.encode({"uid": user_id}, SECRET, algorithm="HS256")

def current_user(token: str) -> int:            # FastAPI 依赖:每个受保护接口先过它
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])["uid"]
    except jwt.PyJWTError:
        raise HTTPException(401, "无效令牌")     # 401 = 没登录

@app.delete("/v1/cards/{cid}")
def delete_card(cid: int, uid: int = Depends(current_user)):
    # 授权检查:这张卡是不是你的?不是 → 403
    ...
```

**讲回来检验**:"认证 vs 授权,各举一例?" "JWT 为什么好扩展、代价是什么?"

**Recall 实操**:
1. `POST /login` 发 JWT;受保护接口用依赖校验。
2. 卡片查询全用**参数化查询**(对比一次"拼接 vs 参数化",体会为何后者防注入)。
3. Claude API 密钥进 `.env`,`.env` 进 `.gitignore`,代码 `os.getenv` 读。(M8 要用)

**过关标准**:能签发/校验 JWT,且别人拿不到你的卡。

**该存的 1 张卡**:正面"JWT 的好处和代价?" 反面:无状态易扩展;难撤销 → 短过期 + 刷新令牌。

---

### M6 · 异步与后台任务 🔥 ⭐⭐

**目标**:把"调 AI 出下一题"这种慢活儿丢后台,接口立刻返回。

> 同步(sync)= 你站窗口等答案。异步(async)= 拿个号先去做别的,叫号再回来。

**📖 只扫读 — 同步 vs 异步何时用**

| | 同步 | 异步 |
|---|---|---|
| 比喻 | 排队等咖啡做好 | 星巴克给你叫号器 |
| 何时 | 答案快(毫秒) | 答案慢(秒级+)/ 要并发 |

**读什么样例**(≤15 行):
```python
from fastapi import BackgroundTasks

def call_ai_for_next_question(card_id: int):
    ...   # 慢:调 Claude 出题(M8 实现),可能几秒

@app.post("/v1/cards/{cid}/grade")
def grade(cid: int, bg: BackgroundTasks):
    save_grade(cid)                              # 快:存复习成绩
    bg.add_task(call_ai_for_next_question, cid)  # 慢活儿丢后台
    return {"status": "已记录,下一题正在准备"}   # 接口立刻返回,不让用户干等
```

**讲回来检验**:"为什么不在接口里直接等 AI 出题?"

**Recall 实操**:`POST /cards/{id}/grade` 后用 `BackgroundTasks` 起步把"出下一题"丢后台,接口立刻返回。

**过关标准**:接口毫秒返回,慢活儿在后台跑。

**该存的 1 张卡**:正面"慢任务为什么丢后台?" 反面:别让用户干等;接口立刻返回,后台慢慢做。

---

### M7 · 缓存 + 性能 + 索引 🔥 ⭐⭐⭐

**目标**:定位 Recall 的慢查询,用索引和缓存修好,会讲 N+1。

> 索引(index)= 给数据库一本"目录",查得快。慢查询头号解药。
> Redis = Remote Dictionary Server,远程字典服务器 — 超快的内存键值库,缓存/限流/队列都用它。

**📖 只扫读 — 扩展顺序口诀**:先加索引 → 再加缓存 → 最后才分库。别过早分片。

**✍️ 学习点 — N+1 问题(面试万能题)**

| | 症状 | 解法 |
|---|---|---|
| N+1 | 查 1 次列表,再循环里查 N 次 → 数据库被打爆;日志里同一句 SQL 刷屏 | `JOIN` 或预加载一次取够 |

**读什么样例 — cache-aside(旁路缓存,最常用模式,≤15 行)**:
```python
cache = {}   # 真项目用 Redis

def get_due_cards_today():
    key = "due:2026-06-13"
    if key in cache:                  # 1. 先查缓存
        return cache[key]
    rows = query_db_due_today()       # 2. 没有 → 查库
    cache[key] = rows                 # 3. 回填缓存(真项目设 30 秒过期)
    return rows
```

**讲回来检验**:"cache-aside 三步是什么?" "N+1 长什么样、怎么修?"

**Recall 实操(二选一做透)**:
- **缓存**:给"今日待复习卡"做 cache-aside,量加缓存前后耗时。
- **索引 + N+1**:给 `next_review_at` 加索引,用 `EXPLAIN QUERY PLAN` 看前后差别;再故意写出 N+1(列出卡 → 循环查每卡复习次数),用 `JOIN` 修掉,记下查询数变化。

**过关标准**:能讲清 N+1,并演示一次"加索引/缓存让查询变快"。

**该存的 1 张卡**:正面"cache-aside 三步?" 反面:查缓存→没有就查库→回填缓存。

---

### M8 · AI 后端 I:流式 AI 出题官 🔥 ⭐⭐

> 这节给谁看:这是你比同期面试者**多出来的差异化武器**。AI 概念零动手 → 样例最足,绝不让你冷启动。

**目标**:让 Claude 把题目**一个字一个字流出来**(打字机效果),并处理超时、重试、计费、拒答。

> LLM = Large Language Model,大语言模型 — 像 Claude 这种能聊天写字的 AI。
> SSE = Server-Sent Events,服务器发送事件 — 服务器单向把文字一点点推给浏览器。
> SDK = Software Development Kit,软件开发工具包 — 官方写好的"调用库",别自己手搓 HTTP。
> 流式(streaming)= 一个响应不一次发完,边生成边一小块一小块地发。

**为什么 LLM 爱用流式**:模型是一个 token(词块)一个一个算出来的。边算边推,用户立刻看到字往外蹦,体验从"卡 5 秒"变成打字机。

**第一步:热身 — 假数据先跑通 SSE(读懂,自己敲)**
```python
from fastapi.responses import StreamingResponse
import asyncio

async def fake_stream():
    for ch in "什么是无状态服务器?":          # 先用假数据模拟逐字输出
        yield f"data: {ch}\n\n"               # SSE 规定每条是 "data: 内容\n\n"
        await asyncio.sleep(0.05)
    yield "data: [DONE]\n\n"                   # 约定一个结束标记

@app.get("/quiz/stream")
async def quiz_stream():
    # media_type 必须是 text/event-stream —— SSE 的"身份证"
    return StreamingResponse(fake_stream(), media_type="text/event-stream")
```
命令行测试:`curl -N http://127.0.0.1:8000/quiz/stream`(`-N` 关掉缓冲,才看得到字一个个蹦)。

**第二步:换成真的 Claude 流式(这是关键,别凭记忆写)**

模型 ID 用 `claude-opus-4-8`(官方当前默认)。**模型 ID 会变,做这步当天再核对一次官方文档。**
```python
import anthropic
client = anthropic.Anthropic()   # 自动读环境变量 ANTHROPIC_API_KEY(见 M5)

async def claude_stream():
    # SDK 的 .stream() 已经帮你把模型输出切成一块块,你只管转发
    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=[{"role": "user", "content": "出一道关于'无状态服务器'的复习题"}],
    ) as stream:
        for text in stream.text_stream:        # 每次拿到一小块文字
            yield f"data: {text}\n\n"          # 包成 SSE 转发出去
        yield "data: [DONE]\n\n"
```
> 关键点(都是面试/真实会踩的坑):
> - **用 SDK 的 `.stream()`,别手搓**。SDK 已经把流切好块,`text_stream` 直接给你文字。
> - **SDK 自动重试**:遇到 429(太多请求)/5xx(服务端错)自带指数退避重试,默认 2 次。**别一上来自己写重试循环**。
> - **超时**:长输出连接开很久。SDK 默认超时 10 分钟;别用太小的值。
> - 📖 进阶(只扫读,别动手):真实生产里常给 Opus 加 `thinking={"type":"adaptive"}`,让模型自己决定"想多久"——出题这种简单任务可不加,记住有这回事就够了。

**第三步:三个防御性检查(计费 + 拒答 + 断开)**
```python
# 1. 拒答:模型可能因安全原因拒绝。先看 stop_reason 再读内容,否则会读到空报错
resp = client.messages.create(model="claude-opus-4-8", max_tokens=1024,
                              messages=[{"role": "user", "content": "..."}])
if resp.stop_reason == "refusal":
    handle_refusal()        # 别当成正常答案
else:
    text = next(b.text for b in resp.content if b.type == "text")

# 2. 计费意识:发请求前数 token(别用 tiktoken,那是 OpenAI 的,会数错)
n = client.messages.count_tokens(model="claude-opus-4-8",
        messages=[{"role": "user", "content": prompt}]).input_tokens

# 3. 客户端中途断开(用户关页面)→ 停止烧 token(FastAPI 里捕获取消异常即可)
```
> ⚠️ 数 token **必须用** `client.messages.count_tokens`,**不要用 `tiktoken`**(那是 OpenAI 的分词器,会把 Claude 的 token 数错)。

**幂等 + 重试的钱坑(连回 M1)**:AI 调用很贵。重试一个**写操作**(比如"生成并存一张卡")时,要带幂等键,否则重试会**重复烧 token + 重复建卡**。

**讲回来检验**:"为什么用 SSE 不用普通 JSON 返回?" "为什么先查 `stop_reason`?" "为什么不自己写重试?"

**Recall 实操**:把热身版换成真 Claude 流式出题官,挂到 `/quiz/stream`;密钥走 `.env`(M5 已配)。

**过关标准**:浏览器/`curl -N` 能看到 Claude 出的题一个字一个字蹦出来。

**该存的 1 张卡**:正面"调 Claude 出题,哪 3 件事别忘?" 反面:用 SDK `.stream()`、先查 stop_reason、靠 SDK 自带重试(别手搓)。

---

### M9 · AI 后端 II:工具调用 + 结构化输出 + RAG + 评估 ⏳ ⭐⭐

**目标**:让 Claude **稳定吐 JSON** 出题(结构化输出)、知道工具调用是什么、做一个最小 RAG、用"AI 当裁判"给输出打分。

> RAG = Retrieval-Augmented Generation,检索增强生成 — 先查资料再让 AI 回答,少胡说。
> 工具调用(tool use / function calling)= 让 Claude 调用你写的函数(查数据库、算数),它要什么你给什么,循环到它说"完成"。

**读什么样例 — 结构化输出(让出题稳定吐 JSON,Recall 的命根子,≤15 行)**:
```python
from pydantic import BaseModel
client = anthropic.Anthropic()

class Quiz(BaseModel):           # 声明你要的形状
    question: str
    answer: str
    difficulty: int

resp = client.messages.parse(    # .parse() 自动按 schema 校验
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "为'幂等性'出一道题"}],
    output_format=Quiz,          # 这是 .parse() 的入参;不是已废弃的 create() 顶层 output_format
)
quiz = resp.parsed_output        # 已经是验证过的 Quiz 对象,不用手动 json.loads
print(quiz.question, quiz.answer)
```
> 为什么这对 Recall 重要:出题官的输出要直接存进数据库的 `question`/`answer` 字段。结构化输出**保证**拿到合法 JSON,不会"AI 多说一句废话把解析搞崩"。

**📖 只扫读 — 另外三块(知道是什么、能讲即可,先别全做)**

| 概念 | 一句话 | Recall 怎么用 |
|---|---|---|
| 工具调用 | Claude 调你的函数,SDK 的 `tool_runner` 自动跑循环 | 让出题官查"这张卡历史错了几次"再决定难度 |
| RAG | 先检索相关资料,再塞进 prompt 让 AI 基于它答 | 出题前先捞用户最近复习的卡,出题更贴合 |
| LLM 评分 | 再用一次 LLM 给输出打分(LLM-as-judge) | 让第二次调用给"这道题质量"打 1-5 分 |

**讲回来检验**:"结构化输出解决了什么问题?" "RAG 为什么能减少胡说?"

**Recall 实操**:用 `messages.parse` 让出题官稳定吐 `{question, answer, difficulty}`,直接存库。进阶:加一次 LLM-as-judge 给题目质量打分。

**过关标准**:出题接口返回的 JSON 永远能直接存库,不崩。

**该存的 1 张卡**:正面"怎么逼 Claude 稳定吐合法 JSON?" 反面:结构化输出 `messages.parse` + Pydantic schema。

---

### M10 · 通信形态全景 🔥 ⭐⭐⭐

**目标**:给一个场景,能说清该用 REST / WebSocket / SSE / gRPC / Webhook 哪个、为什么。**这节重在"判断轴",不全做实现。**

**📖 只扫读 — 协议速查(理解轴,别背表)**

判断三轴:**延迟容忍度** + **单向/双向** + **实现成本**。

| 模式 | 一句话 | 何时用 |
|---|---|---|
| 请求-响应 | 问一句答一句 | 绝大多数 API |
| 轮询 Polling | 每隔几秒问"好了没" | 更新慢、能忍延迟 |
| 长轮询 Long Polling | 问一次,服务器有结果才答 | 要准实时又不想升级架构 |
| SSE | 服务器单向推文字(打字机) | **LLM 流式输出给浏览器** |
| WebSocket | 双向长连接,随时互发 | 聊天、双向实时语音 Agent |
| gRPC | 内部服务间又快又省的二进制调用 | 内部微服务高频低延迟 |
| Webhook | 长任务做完,服务器**回调你的 URL** | 支付回调、AI 长任务完成通知 |

> WebSocket = 双向长连接。SSE 更简单、走普通 HTTP、自动重连,**只需单向推就用 SSE**。
> gRPC = 一种由 Google 开源的高性能 RPC(Remote Procedure Call,远程过程调用)框架 — 像调本地函数一样调另一台机器的函数。**面试金句**:"对外给浏览器用 REST/JSON,对内微服务之间用 gRPC。"
> Webhook = 服务器在长任务做完后,主动 POST 到你给的一个网址。**关键安全点**:验证签名(HMAC),否则谁都能伪造回调。

**📖 AI 后端选型表(你的差异化武器,反复看)**

| 场景 | 选什么 | 为什么 |
|---|---|---|
| LLM 流式输出给浏览器 | **SSE** | 单向、走普通 HTTP、自动重连、简单 |
| 双向实时语音 Agent | WebSocket | 需要双向 |
| 内部模型推理服务互调 | gRPC | 二进制快、强类型 |
| 长任务(批量生成卡片) | **异步 + 轮询 / Webhook** | 几秒到几分钟,别占着连接死等 |

**讲回来检验**:给你"实时聊天""LLM 流式""支付到账通知"三个场景,各选哪个、为什么。

**Recall 实操**:写一句话说明 Recall 的"流式出题"为什么用 SSE 不用 WebSocket;再为"批量生成 100 张卡"设计一个"异步任务 + Webhook 完成回调"的流程图(画图即可,不全实现)。

**过关标准**:任意场景能在三轴上说清选型理由。

**该存的 1 张卡**:正面"只需服务器单向推,SSE 还是 WebSocket?" 反面:SSE — 更简单、普通 HTTP、自动重连。

---

### M11 · 上线工程 ⏳ ⭐⭐

**目标**:让 Recall "看得见、测得了、跑得起":结构化日志、健康检查、测试、Docker。

> 可观测性(observability)= 给系统装仪表盘和黑匣子,出事能查。
> Docker = 把"代码 + 环境"打包成一个盒子,到处一样跑,消灭"我机器上能跑"。
> CI = Continuous Integration,持续集成 — 每次改代码自动跑测试的"质检流水线"。

**📖 只扫读 — 12-Factor 挑 3 条记牢**:配置进环境变量、服务无状态、日志打到 stdout(别自己管文件)。

**读什么样例 — 结构化日志 + 健康检查 + 一个测试(≤15 行)**:
```python
@app.get("/health")                  # 给负载均衡看"我还活着"
def health():
    return {"status": "ok"}

# pytest:测你自己的接口(mid 面试会问"你写测试吗")
from fastapi.testclient import TestClient
def test_list_cards():
    client = TestClient(app)
    r = client.get("/v1/cards?limit=5")
    assert r.status_code == 200      # 断言:返回 200 才算过
```
> Docker 心智模型:`Dockerfile` = 配方,`image`(镜像)= 做好的盒饭,`container`(容器)= 正在吃的那份。

**讲回来检验**:"`/health` 给谁看?" "无状态为什么好水平扩展?(没机器独占你的会话 → 随便加/换机器)"

**Recall 实操**:加结构化日志中间件(每个请求打 `{request_id, method, path, status, 耗时ms}` 到 stdout)+ `GET /health` + 给一个接口写 pytest + 写最小 `Dockerfile` 本地 `docker run` 跑起来。⏳ 迁 Postgres、Prometheus 指标、完整 CI 懂概念即可。

**过关标准**:能本地 Docker 跑 Recall + 至少一个绿色 pytest。

**该存的 1 张卡**:正面"无状态为什么好扩展?" 反面:没机器独占会话 → 随便加/换机器。

---

### M12 · 顶石:端到端 + 面试讲故事 🔥 ⭐⭐⭐

**目标**:把 M1–M11 串成一个能演示的 Recall,并能向面试官讲清**每个决策的取舍**。

**读什么样例 — 面试电梯话术(背下来,改成你自己的)**:
> "Recall 的接口走 REST,状态码 + Pydantic 校验 + 幂等键保证重试安全。数据层先加索引、用事务、消灭 N+1;扩展时先 cache-aside 再异步、靠无状态水平扩展。安全上认证授权分离 + 参数化查询 + 密钥不进 Git。AI 出题官用 Claude SDK 流式(SSE)给浏览器,先查 stop_reason、靠 SDK 自带重试、结构化输出保证吐合法 JSON,长任务走异步 + Webhook。最后用结构化日志 + /health + pytest 让它可观测、可测。"

**讲回来检验**:对着"小黄鸭"把这段讲一遍,每个技术词都能展开一句"为什么这么选"。

**Recall 实操**:端到端跑一遍:登录 → 建卡 → 流式出题 → 评分 → 后台出下一题 → 看日志。录一段自己讲解的音。

**过关标准**:不看稿,能讲清整条链路 + 3 个关键取舍。

**该存的 1 张卡**:正面"面试 60 秒讲清你的后端能力?" 反面:背诵上面的电梯话术骨架。

---

## ④ 能力关卡清单(面试自信依据)

> 每过一关 = 一条能写进简历、能当面演示的能力。**自己能独立、不偷看做到**才算过。

| 关卡 | 解锁模块 | 独立做到 |
|---|---|---|
| G1 接口手艺 | M1, M4 | REST 接口:正确状态码、Pydantic 校验、统一错误、幂等键 |
| G2 数据层 | M2, M3 | 从零设计 Recall 的表、用 ORM 增删改查 + 关联查询 |
| G3 安全访问 | M5 | 注册/登录:JWT 签发与校验、"只能动自己的卡"、参数化查询 |
| G4 异步与性能 | M6, M7 | 慢活儿丢后台;定位慢查询用索引/缓存修好;能讲 N+1 |
| G5 AI 后端 | M8, M9 | Claude 流式出题官:SSE、stop_reason、SDK 重试、count_tokens 计费、结构化输出 |
| G6 通信判断力 | M10 | 给场景能说清 REST/WebSocket/SSE/gRPC/Webhook 选哪个、为什么 |
| G7 上线工程 | M11 | 结构化日志 + /health + pytest + 本地 Docker 跑起来 |
| G8 顶石 | M12 | 端到端可演示 + 向面试官讲清每个决策取舍 |

> **诚实边界**:过完 G1–G8 = **可信赖的 junior→mid 候选人**,有真项目和取舍判断力。**不是** senior(大规模分布式、百万连接调优仍需实战年头)。但你将**有底气、有据可讲**。

---

## ⑤ 与 5 天主课同步排期

> 主课 = 白天 5 天全栈特训。这门是**夜间挂载的拓展加固**,不抢主课认知带宽。

**每日节奏(模式 A)**

| 时段 | 时长 | 干嘛 |
|---|---|---|
| 晨练(主课前) | 30 分钟 | **次日重写**昨晚核心片段 + 抽卡 |
| 主课 | 全天 | 不动 |
| 夜间块 | 75 分钟 | 新模块"读样例 → 讲回来 → 敲一半",重活留晨练 |

**5 天 + 冲刺期映射**

| 天 | 夜间模块 | 备注 |
|---|---|---|
| D1 | M0 + M1 | 偏复习,轻 |
| D2 | M2 | 数据库零动手 → 给足时间,可能只"读 + 讲回来" |
| D3 | M3 | 建 Recall 表 |
| D4 | M4 | 校验/错误 |
| D5 | M5 起步 | 认证 |
| **冲刺 D6–D12** | 每天 10–12h 推 M5→M12 | 主课已毕,火力全开;每天 1 主模块 + 缝合 |

**缝合 + 防超载**
- 每 3 个模块后做一次"缝合课":只做练习,不学新概念,把前 3 个连起来。
- 红线:任何一晚出现**红灯**(敲码偷看超 3 次)→ **停新概念**,改纯缝合/复习。宁可慢,不可夹生。
- 重的一天(主课累)→ 夜间块只"读样例 + 讲回来",**不敲代码**,把实操挪到晨练。

---

## 缩写表(首次出现处也会再点一句)

| 缩写 | 全称 | 一句大白话 |
|---|---|---|
| HTTP | HyperText Transfer Protocol | 浏览器和服务器说话的礼貌用语规则 |
| API | Application Programming Interface | 程序之间说话的"菜单" |
| REST | Representational State Transfer | 用 URL + HTTP 方法管理"资源"的约定 |
| JSON | JavaScript Object Notation | 大家都看得懂的数据打包格式 |
| SQL | Structured Query Language | 跟数据库要数据的"问话语言" |
| ORM | Object-Relational Mapping | 用 Python 对象代替手写 SQL 的翻译层 |
| CRUD | Create Read Update Delete | 增、查、改、删 |
| JWT | JSON Web Token | 一张带签名的通行证 |
| LLM | Large Language Model | 像 Claude 这样的大语言模型 |
| SDK | Software Development Kit | 官方写好的调用库,别自己手搓 |
| SSE | Server-Sent Events | 服务器一点点把文字推给你(打字机) |
| RAG | Retrieval-Augmented Generation | 先查资料再让 AI 答,少胡说 |
| gRPC | 由 Google 开源的 RPC(Remote Procedure Call)框架 | 又快又省的机器间通话方式 |
| N+1 | N+1 query problem | 本该 1 次查询却查了 N+1 次的性能坑 |
| CI | Continuous Integration | 每次改代码自动跑测试的质检流水线 |
| HMAC | Hash-based Message Authentication Code | 验证回调没被伪造的"防伪签名" |
