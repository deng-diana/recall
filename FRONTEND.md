# 《前端强化 · 集训课》(FRONTEND.md)

> 给 Dan 的设计工程师专精课。配套 BACKEND.md。目标:把你"AI 帮我写过、能跑但讲不清"的前端,打成**自己能写、能讲原理、做出一个亮眼作品**。
> 你的杀手锏:**design engineer(设计工程师)**——设计系统 + 动效 + 对 UI 品质的高敏感。这门课把它做到最深最出彩。
> 诚实边界:几天不会把你变 senior。这门课给的是**扎实手艺 + 能独立写能讲原理 + 一个让面试官记住的技能树作品**,足够让你自信投 junior→mid。

**记号**:🔥 核心必学　⏳ 进阶可延后　⭐ 面试高频(越多越常被问)
**针对你"熟悉但不扎实"的额外信号**:🟢 你大概率已会(诊断后可快速跳过)　🔴 必须打牢
**两类内容**:📖 只扫读(别背,看懂能查)　✍️ 学习点(要能讲会敲)

---

## ① 一页课程地图

> 这页给谁看:每次迷路了回这看"我在哪、为什么学这个"。

你今天会的:JSX、用 AI 写过 React/Next/RN 项目。我们把"会用"打成"扎实"。
顶层 **5 个模块(M0–M5)**;每个大模块里用从属编号(如 M1.3)拆小节,**全文只有这一套编号**。

| 模块 | 核心问题(一句话) | 面试权重 | 你现状 | 挂到 Recall 的实操 |
|---|---|---|---|---|
| **M0** 诊断 + 工具链 🔥 | 找到"熟悉但不扎实"的洞在哪 | ⭐ | — | 30 分钟冷启动自测 |
| **M1** React 内功 🔴🔥 | React 何时重画、状态放哪、性能 | 🔴 讲不清 | ⭐⭐⭐ | XP/技能树状态架构 + 修一次卡顿 |
| **M2** Next.js App Router 🔴🔥 | 默认在服务器、缓存、写数据 | 🔴 夹生 | ⭐⭐⭐ | Web 仪表盘:拉 FastAPI `/stats` |
| **M3** 设计系统 ★🔴🔥 | token / 主题 / a11y / shadcn | 🟡 设计强、代码弱 | ⭐⭐⭐ | 一套 Recall 设计系统 |
| **M4** 动效 Motion ★🔴🔥 | 技能树/XP 动画、手感、性能 | 🟡 用过没讲过 | ⭐⭐⭐ | 技能树逐个点亮 + 升级弹窗 |
| **M5** React Native 🔥 | 把 Recall 搬上手机 | 🟡 半会 | ⭐⭐⭐ | Recall 手机版 |

★ = 你的差异化主场(设计工程师),投入最多打磨时间。

**学习顺序(谁解锁谁)**

主链:**M0 → M1 → M2 → M3 → M4 → M5**

| 模块 | 学它前要先会 |
|---|---|
| M2 Next.js | M1(React 心智是地基) |
| M3 设计系统 | M1(组件设计);**不依赖后端,后端卡住时切来这里** |
| M4 动效 | M3(组件 + token);Web 用 `motion/react`(见 M4.0) |
| M5 RN | M1;复用 M3 的设计 token 思路 |

**读多于憋的分配**:M1 的渲染/状态选型/性能、M2 的 Server/Client 边界与缓存、M3、M4 你最弱或最该出彩 → 样例最足、引导最满。基础节(🟢)诊断后快速跳过。

---

## ② 怎么学这门课(≤3 段)

**主循环(已验证有效)**:读懂带逐行注释的完整样例 → 合上代码用大白话讲回来(费曼,讲给"小黄鸭"听)→ 参考着自己敲(**禁复制粘贴**)→ 次日合上参考从零重写核心片段。新/难概念给足样例,**绝不冷启动硬憋**;诊断标 🟢 的基础快速跳过。

**认知负荷规则(阅读障碍适配)**:每模块每小节**新概念 ≤ 3 个**(超了拆带标题的小块,如 M5.1 的"5 样差异"用一张表呈现);代码块 ≤ 15 行;优先级 **图 > 表 > 短句 > 段落**;缩写首次出现给全称 + 一句大白话(见 §缩写表)。**信号灯**:讲回来卡壳 = 黄灯(重读样例);敲代码偷看超 3 次 = 红灯(退回上一节,别夹生)。

**两类内容自检**:表格标"📖 只扫读"= **别背**,看懂能查即可;标"✍️ 学习点"= 要能讲会敲。每节结束:存 1 张卡进你自己的 Recall(顺便体验产品),次日抽卡 + 第 3 / 第 7 天再刷(间隔重复,正好用 Recall 自练)。

---

## ③ 模块逐节展开

> 每节统一模板:**目标 / 读什么样例 / 讲回来检验 / Recall 实操 / 过关标准 / 存 1 张卡**。

---

### M0 · 诊断 + 工具链:先测漏,再补 🔥

**目标**:用 30–45 分钟自测,把"熟悉但不扎实"的洞找出来——据此决定哪些节真跳过。**自评常偏乐观,所以这步必做。**

**✍️ 冷启动诊断(不看任何资料,做完给自己打档)**

| 小任务(不查文档) | 自评 |
|---|---|
| 写一个带清理函数的 `useEffect` | 🟢能 / 🟡能讲要查 / 🔴卡 |
| 说清"列表 key 为什么不能用 index" | 🟢🟡🔴 |
| 徒手写一个受控 `<input>` | 🟢🟡🔴 |
| 说清 Next.js "Server vs Client" 边界 | 🟢🟡🔴 |
| 看懂 `function X({ n }: { n: number })` 这行 TS 类型 | 🟢🟡🔴 |

> 🟢 = 独立做到 → 该节扫读跳过。🟡 = 能讲要查 → 快速过。🔴 = 卡 → 样例全做。地图里的 🟢/🔴 预判**由你诊断后确认**,别替自己假设。

**📖 只扫读 — 工具链(知道是什么)**

| 工具 | 全称/大白话 |
|---|---|
| Vite | 超快的前端打包/开发服务器(Web 起步用) |
| TS | TypeScript,给 JS 加"类型标签"的语言,写错早发现 |
| Expo | 一套开箱即用的 React Native 工具箱(M5 用) |

**Recall 实操**:`npm create vite@latest recall-web -- --template react-ts` 起一个空 Web 项目;诊断表填完存进 Recall。
**过关标准**:空项目能 `npm run dev` 打开;诊断表每行有档位。
**该存的 1 张卡**:正面"我最弱的两个前端点是?" 反面:你诊断出的那两个 🔴。

---

## M1 · React 内功 🔴🔥

> 这条线把"AI 帮我写、能跑"打成"自己能写、能讲原理"。React 面试的分水岭全在这。

---

### M1.1 · 渲染心智模型 🔴 ⭐⭐⭐(最重要,先打这个)

**目标**:一句话说清 React 何时重画。你 90% 的 bug 和卡顿,根在这。

**✍️ 核心三条(记死)**:
1. 组件就是个函数,**state(状态,会变的数据)变了它就重新跑一遍**。
2. 重新跑 = 函数里的变量、函数全部重建一次(这是后面 `useMemo` 存在的原因)。
3. 父组件重渲染,**默认所有子组件也跟着重渲染**(哪怕 props 没变)。

**读什么样例**(≤15 行):
```jsx
function XpBadge() {
  const [xp, setXp] = useState(0);
  console.log("XpBadge 重新跑了", xp); // 每次点都会打印
  return <button onClick={() => setXp(xp + 1)}>XP: {xp}</button>;
}
```
> render / re-render = 渲染 / 重渲染:React 重新跑组件函数算出新画面。

**讲回来检验**:点一下按钮,函数跑了几次?为什么 `console.log` 会再打印?
**Recall 实操**:给仪表盘的 XP 数字加 `console.log`,点几下,数重渲染次数。
**过关标准**:能用大白话说"state 变 → 函数重跑 → 算新 UI"。
**该存的 1 张卡**:正面"React 什么时候重画?" 反面:state 变 → 组件函数重跑 → 算新画面 → 只贴变的部分。

---

### M1.2 · useState + 受控表单 🟢→🔴 ⭐⭐⭐

**目标**:会改 state(避两个坑),会写受控输入框。

**✍️ useState 两个坑**(🟢 会用就看这两个):
- 改 state 要给**新对象**:`setItems([...items, x])` ✅,`items.push(x)` ❌(React 看不到变化)。
- `setXp(xp+1)` 连写两次只 +1;连加用函数式 `setXp(n => n+1)`。⭐面试常问。

**✍️ 受控 vs 非受控**:
- **受控** = 值由 React state 说了算(`value={x}`),主流选这个,可实时校验。
- **非受控** = 输入框自己记,你用 ref 去拿(简单表单、文件上传)。

```jsx
const [front, setFront] = useState("");
<input value={front} onChange={e => setFront(e.target.value)} />
```
> 只写 `value` 不写 `onChange` → 输入框打不了字(React 锁死)。经典 bug。

**讲回来检验**:"为什么用 `n => n+1`?" "受控/非受控差在哪?"
**Recall 实操**:做"新建卡片"表单(正面/反面两个受控输入)。
**过关标准**:能写受控输入 + 讲清函数式更新。
**该存的 1 张卡**:正面"受控输入框靠哪两个属性?" 反面:`value` + `onChange`。

---

### M1.3 · React 19 Actions + 表单状态 🔴 ⭐⭐⭐(2025/2026 标准答案)

**目标**:用 React 19 的 Actions 处理"新建卡片"提交——自动管 pending(加载中)/error。这是现在表单的标准做法,面试高频。

**✍️ 三个新 hook**:
- `<form action={fn}>`:表单直接绑一个函数(可异步)。
- `useActionState`:拿到 `[state, formAction, isPending]`。
- `useFormStatus`:**子组件**里读父表单的 pending,用来禁用按钮。

```jsx
import { useActionState } from "react";

function NewCard() {
  const [state, formAction, isPending] = useActionState(
    async (prev, formData) => {        // formData = 表单里的值
      await createCard(formData.get("front"));
      return { ok: true };
    }, null);
  return (
    <form action={formAction}>
      <input name="front" />
      <button disabled={isPending}>{isPending ? "保存中…" : "保存"}</button>
    </form>
  );
}
```
> `useOptimistic`(乐观更新)= UI 先假装成功(复习后 XP 先涨),后台失败再回滚。⭐进阶,知道有这回事。

**讲回来检验**:"pending 状态从哪来?不用自己写 `useState(loading)` 了?"
**Recall 实操**:"新建卡片"表单用 `useActionState`,提交时按钮显示"保存中…"。
**过关标准**:能讲清 Actions 替你省掉的样板(loading/error 手动管理)。
**该存的 1 张卡**:正面"React 19 表单怎么拿 pending?" 反面:`useActionState` 给 `isPending`;子按钮用 `useFormStatus`。

---

### M1.4 · useEffect 心智 + useRef 🔴 ⭐⭐⭐(你最易滥用)

**目标**:搞懂**大部分时候你不需要 effect**;分清 ref 和 state。

> side effect(副作用)= 画界面以外的事(调接口、定时器)。`useEffect` = 渲染**之后**去做这种事。

**✍️ 何时真用 effect**:

| 你想干的事 | 用 effect? |
|---|---|
| 根据 props 算个派生值 | ❌ 直接在渲染里算 |
| 组件出现时拉数据 | ✅ 但更推荐 TanStack Query / RSC(见 M1.6、M2) |
| 订阅事件 / 定时器 / WebSocket | ✅ 且要返回清理函数 |
| 点按钮做事 | ❌ 写在 onClick 里 |

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id); // 清理:组件消失就停,防内存泄漏
}, []); // 依赖数组:[] = 只在出现时跑一次
```
> 依赖数组(dependency array)= 方括号里的值变了才重跑。漏写 = 用到旧数据(stale,过期)的经典 bug。⭐⭐⭐
> useRef(引用)= "改了**不触发重画**的盒子"。用途:① 拿 DOM(聚焦输入框)② 存计时器 id。**变了要重画→state;不用重画→ref。**

**讲回来检验**:"哪些事不该用 effect?" "ref 和 state 分工?"
**Recall 实操**:打开"新建卡片"时用 ref 自动聚焦输入框。
**过关标准**:能说出 3 件"不该塞进 effect"的事。
**该存的 1 张卡**:正面"effect 和 ref 各管什么?" 反面:effect=渲染后的副作用(带清理);ref=不触发重画的盒子。

---

### M1.5 · 列表 + 组件组合 + 状态放哪 🔴 ⭐⭐⭐(面试最爱)

**目标**:列表正确用 key;会拆组件;给任意状态选对家。

**✍️ key**:`.map()` 渲染数组,每个给唯一 `key`。**别用数组下标 index** —— 列表重排/删除时 index 错位,React 认错人 → 输入串台、动画乱跳。用稳定 id。⭐⭐⭐
```jsx
{cards.map(c => <SkillNode key={c.id} card={c} />)} // key 用 c.id
```

**✍️ 状态放哪决策表**(背这张):

| 谁需要这个状态 | 放哪 | 工具 |
|---|---|---|
| 只有一个组件 | 组件内 | `useState` |
| 兄弟组件共享 | 提到共同父组件(状态提升) | `useState` + props |
| 全 App、很少变(主题/登录用户) | 全局 | `Context` |
| 全局、频繁变(XP、技能树进度) | 全局 store | **Zustand** |
| 来自服务器的数据 | 不算状态,是缓存 | **TanStack Query**(M1.6) |

> ⭐⭐⭐ **Context(上下文)不是状态管理库**,只负责"传递",而且它的值一变,所有用它的组件全重渲染 → 高频数据(XP)用它会卡,所以用 Zustand。
> prop drilling(逐层透传)= props 传太多层的麻烦,正是 Context 要解决的。

**讲回来检验**:"index 当 key 出什么 bug?" "XP 该放哪、为什么不用 Context?"
**Recall 实操**:仪表盘拆成 `<XpBar>` `<SkillTree>` `<DueList>`;XP/技能树进度用 Zustand store,当前用户用 Context。
**过关标准**:给任意状态能说出放哪 + 为什么。
**该存的 1 张卡**:正面"频繁变的全局状态用 Context 还是 Zustand?" 反面:Zustand;Context 一变全部重渲染会卡。

---

### M1.6 · 性能 + 服务器数据 🔴 ⭐⭐⭐

**目标**:会用 Profiler 定位卡顿并修;懂服务器数据不该塞 useState。

**✍️ memo 三兄弟**:每次重跑都重算变量、重建函数。`useMemo` 缓存**计算结果**,`useCallback` 缓存**函数**,`React.memo` 包**子组件**(props 没变就不重画)。
```jsx
const dueCards = useMemo(
  () => cards.filter(c => c.due <= today), // 只有依赖变才重算
  [cards, today]);
```
> ⭐陷阱:**别到处乱包**。简单计算包了反而更慢(缓存有成本)。**先用 React DevTools 的 Profiler(性能分析器)测到卡,再优化。**

**✍️ 服务器数据用 TanStack Query**(原 React Query):后端来的数据不是普通 state,是"服务器的缓存副本"。别手写 `useEffect + useState`。
```jsx
const { data, isLoading, error } = useQuery({
  queryKey: ["due-cards"],            // 数据身份证,相同 key 共享缓存
  queryFn: () => fetch("/v1/cards?due=today").then(r => r.json()),
});
```
> **何时用 Query vs Server Component 取数**:页面首屏静态数据 → 在 M2 的 Server Component 里 `await`;客户端交互后变化、要轮询/缓存的数据 → TanStack Query。别两个一起套同一份数据。

**讲回来检验**:"什么时候**不**该用 memo?" "服务器数据为什么不塞 useState?"
**Recall 实操**:故意让 `<SkillTree>` 在 XP 变化时也重渲染,用 Profiler 看到,用 `React.memo` 修好;再用 TanStack Query 拉 FastAPI "今日到期卡片"。
**过关标准**:能演示"定位→修→验证变快";能讲清 Query 的好处。
**该存的 1 张卡**:正面"卡顿先做什么、再做什么?" 反面:先 Profiler 测,再用 memo 三兄弟修(别凭感觉乱包)。

---

## M2 · Next.js App Router 现代实践 🔴🔥

> Next.js = 建在 React 上的全套框架(路由、服务器渲染、打包、上线)。App Router = 现在的标准:**文件夹结构当网址,默认在服务器跑**。
> 实操母题:**用 App Router 搭 Recall Web 仪表盘,从 FastAPI `/stats` 拉数据渲染技能树。**

---

### M2.1 · 心智模型 + 路由布局 🔥 ⭐⭐⭐

**目标**:说清"默认在服务器"差在哪;用文件夹搭 `/dashboard` + 共享侧边栏。

> RSC = React Server Component:在**服务器**渲染好、只送 HTML 的组件(默认)。
> Client Component:送到**浏览器**跑、能用 `useState`/点击/动效(要手动标 `"use client"`)。

```
请求 → 服务器跑 RSC → 直接 await FastAPI → 生成 HTML(秒出、利于 SEO)
     → 送浏览器 → 浏览器只"激活"标了 "use client" 的小岛(按钮/动效)
```
> SEO = Search Engine Optimization,搜索引擎优化 — 让谷歌看得懂页面。

**✍️ 文件夹即网址**:

| 文件 | 含义 |
|---|---|
| `app/dashboard/page.tsx` | 页面 `/dashboard` |
| `app/dashboard/layout.tsx` | 包裹下面所有页的"外壳",切页不重渲染 |
| `app/dashboard/loading.tsx` | 加载中占位 |
| `app/dashboard/error.tsx` | 出错时显示 |

```tsx
// app/dashboard/layout.tsx — 切页时侧边栏不重渲染
export default function DashboardLayout(
  { children }: { children: React.ReactNode }) {
  return (
    <div className="flex">
      <Sidebar />                      {/* 跨页保留 */}
      <main className="flex-1">{children}</main>
    </div>
  );
}
```

**讲回来检验**:"为什么 RSC 能直接 await 而不用 useEffect?" "layout 的 children 是什么?"
**Recall 实操**:建 `app/dashboard/page.tsx` + `layout.tsx`,侧边栏放"技能树/复习/设置"。
**过关标准**:能说出"默认服务器,客户端是例外"。
**该存的 1 张卡**:正面"App Router 默认在哪渲染?" 反面:服务器;只有标 `"use client"` 才进浏览器。

---

### M2.2 · Server vs Client 边界 🔥 ⭐⭐⭐(最易夹生)

**目标**:学会画边界——静态内容留服务器,只有交互/动效的叶子标客户端。

**✍️ 谁该是 Client**:

| 你要用… | 那它得是 |
|---|---|
| `useState` / `useEffect` / `onClick` | Client |
| Motion 动效 | Client |
| 只展示数据 / `await fetch` | Server(默认) |

> **黄金法则**:`"use client"` 标在**尽量靠下的叶子组件**。**红灯信号**:想给整个 `page.tsx` 标 `"use client"` → 停,重画边界(否则整棵树都进浏览器,白白变重)。

```tsx
// app/dashboard/page.tsx (Server) — 拉数据 + 渲染
import { XpBar } from "./xp-bar";
export default async function Page() {
  const stats = await getStats();
  return <XpBar value={stats.xp} />;     // 数据当 prop 传进去
}
```
```tsx
// app/dashboard/xp-bar.tsx (Client) — 只这个小岛进浏览器
"use client";
import { motion } from "motion/react";
export function XpBar({ value }: { value: number }) {
  return <motion.div animate={{ width: `${value}%` }} />;
}
```
> 这个 `XpBar` 就是 React / Next / Motion 三条线的交汇点。

**讲回来检验**:"`"use client"` 该标哪?整页标会怎样?"
**Recall 实操**:技能树容器是 Server,带动效的 XP 条/节点是 Client。
**过关标准**:看到"想给整页标 client"会停下重画边界。
**该存的 1 张卡**:正面"`"use client"` 标哪?" 反面:尽量靠下的交互叶子,不标整页。

---

### M2.3 · 拉后端数据 + Server Actions 🔥 ⭐⭐⭐

**目标**:在 RSC 里直接 `await` FastAPI;用 Server Action 回写数据。

```tsx
// app/dashboard/page.tsx
async function getStats() {
  const res = await fetch(`${process.env.FASTAPI_URL}/stats`, {
    next: { revalidate: 60, tags: ["stats"] }, // 缓存 60 秒,可按 tag 失效
  });
  if (!res.ok) throw new Error("stats failed"); // 触发最近的 error.tsx
  return res.json();
}
```
> 为什么在服务器拉:① 不暴露 API 地址/密钥给浏览器 ② 数据离服务器近 ③ 浏览器不用等 useEffect 二次往返。

> Server Action = 标了 `"use server"` 的函数,**在服务器跑**,但客户端按钮能直接调——这就是 M1.3 的 React 19 Actions 在 Next.js 里的形态。pending/error 同样用 `useActionState` / `useFormStatus` 拿。

```tsx
// app/dashboard/actions.ts
"use server";
import { updateTag } from "next/cache";
export async function markReviewed(cardId: string) {
  await fetch(`${process.env.FASTAPI_URL}/cards/${cardId}/review`,
    { method: "POST" });
  updateTag("stats");   // 让 /stats 缓存失效 → XP 自动刷新(见 M2.4)
}
```

**讲回来检验**:"为什么这里不用 useEffect?" "Server Action 和普通 API 路由差在哪?"
**Recall 实操**:FastAPI 加 `/stats`(返回 `{xp, level, skills:[...]}`)和 `/cards/{id}/review`;Next.js 服务端拉来渲染;复习按钮 `<form action={markReviewed}>` 点完 XP 自动更新。
**过关标准**:端到端跑通"表单 → Server Action → FastAPI 写 → 缓存失效 → UI 刷新"。
**该存的 1 张卡**:正面"RSC 怎么拉数据?" 反面:直接 `await fetch`,配 `next.revalidate` / tag。

> ⏳⭐ **设计工程师的手感挑战**:上面 Server Action 走的是"回写→失效→重拉",XP 会有一点延迟才跳。想让它**复习完瞬间涨**(不等服务器),把 M1.3 的 `useOptimistic` 接到复习按钮——这种对微延迟的敏感,正是设计工程师的签名。

---

### M2.4 · 渲染 + 缓存策略 🔥 ⭐⭐⭐

**目标**:分清四种渲染时机;懂 Next.js 16 的 `use cache` 心智。

> ⚠️ **此 API 在演进**:`use cache` / `cacheLife` / `cacheTag` / `updateTag` 属 Next.js 16 Cache Components,需开 `cacheComponents` 开关。**做这步当天核对官方文档。** 部署到 Vercel、想要跨请求持久缓存时,指令写 `"use cache: remote"`;`cacheLife` 字段建议用 `{ revalidate, expire }` 成对。

**📖 只扫读 — 四种渲染(别背,会选就行)**:

| 名 | 何时生成 HTML | 适合 |
|---|---|---|
| SSG 静态 | 构建时 | 不变的页(落地页) |
| SSR 服务端 | 每次请求 | 高度个性化页 |
| ISR 增量 | 构建后定时再生 | `/stats`(几十秒旧没事) |
| PPR 部分预渲染 | 静态壳秒出 + 动态部分流式补 | 仪表盘(壳静态、数字动态) |

> SSG=Static Site Generation　SSR=Server-Side Rendering　ISR=Incremental Static Regeneration　PPR=Partial Prerendering。

**✍️ `use cache`(选一种缓存写法,别和上面 `fetch` 的 `next:{revalidate}` 同时套同一份数据)**:
```tsx
// next.config.ts: { cacheComponents: true } 先开开关
import { cacheLife, cacheTag } from "next/cache";
async function getStats() {
  "use cache";
  cacheTag("stats");              // 配合 Server Action 的 updateTag
  cacheLife({ revalidate: 60 });  // 60 秒后台再生
  const res = await fetch(`${process.env.FASTAPI_URL}/stats`);
  return res.json();
}
```
> **失效二选一**(别记混):配 `use cache` + `cacheTag` → 用 **`updateTag('stats')`**(Next 16.2 转正);老写法 `revalidateTag` 现需带 cacheLife profile 作第二参。

**讲回来检验**:"ISR(定时再生)和 updateTag(事件触发失效)差在哪?"
**Recall 实操**:`/stats` 用 PPR——侧边栏/标题静态秒出,技能树数字 `use cache` 缓存 60 秒;复习后 `updateTag("stats")` 即时刷新。
**过关标准**:能区分定时再生 vs 事件失效。
**该存的 1 张卡**:正面"`use cache` + `cacheTag` 怎么主动失效?" 反面:`updateTag('stats')`。

---

### M2.5 · 环境变量 + 上线 Vercel 🔥 ⭐⭐

**✍️ 两种环境变量**:

| 写法 | 谁能看 | 放什么 |
|---|---|---|
| `FASTAPI_URL` | 仅服务器 | API 地址、密钥 |
| `NEXT_PUBLIC_XXX` | 浏览器也能看 | 公开配置(分析 ID) |

> 红线:任何 `NEXT_PUBLIC_` 前缀的值都**打包进浏览器代码**,绝不放密钥。

**📖 只扫读 — 上线 Vercel**:
```
1. GitHub 建仓 push 代码
2. Vercel 导入仓库(自动认出 Next.js)
3. Settings → Environment Variables 填 FASTAPI_URL(生产公网地址)
4. push main → 自动生产部署;PR → 自动 preview 预览
```
> 本地 `localhost:8000` 的 FastAPI 上线后要换**公网地址**,否则 Vercel 拉不到。

**讲回来检验**:"`NEXT_PUBLIC_` 意味着什么?"
**Recall 实操**:仪表盘上线 Vercel;FastAPI 先部署公网,地址填进环境变量。
**过关标准**:能安全管理环境变量 + 走通 preview/production。
**该存的 1 张卡**:正面"密钥能用 NEXT_PUBLIC_ 吗?" 反面:不能,会暴露给浏览器。

---

## M3 · 设计系统 ★🔴🔥(设计工程师主场,最深)

> 前面是"会写";这条是"写得**漂亮、可访问、有手感**,还能讲清为什么"。做出让面试官记住的技能树仪表盘。**不依赖后端,后端卡住时切来这里,永不空转。**

---

### M3.1 · 设计 token + 主题 🔥 ⭐⭐

**目标**:把"这个蓝色/这个间距"起名存一处;暗色模式 = 第二套 token 值。

> token = design token,设计令牌:设计的"乐高积木",一个颜色/间距的命名值,**改一处全站变**(就像 Figma 的 styles 搬进代码)。

**✍️ 四类基础 token**:

| 类别 | 命名例 | Recall 用法 |
|---|---|---|
| 颜色 | `--color-xp` | XP 进度条的金色 |
| 间距 | `--space-2` (8px) | 卡片内边距,4 的倍数成阶梯 |
| 字号 | `--text-lg` | 技能名 vs 描述的层级 |
| 圆角 | `--radius-card` | 技能节点统一圆角 |

```css
:root {
  --color-primary: 222 89% 55%;  /* HSL 三个数,留空格 */
  --color-xp: 45 93% 58%;        /* 经验金 */
  --radius-card: 0.75rem;
}
.dark { --color-primary: 222 89% 65%; --color-bg: 222 47% 11%; }
```
> HSL = Hue/Saturation/Lightness(色相/饱和度/亮度)。用它不用 hex:暗色模式只改"亮度"那个数。组件永远写 `bg-[hsl(var(--color-bg))]`,从不知道自己是亮是暗 —— 切换 = 给 `<html>` 加 `.dark` 类(这就是 shadcn/ui 的做法)。
> ⭐**面试加分**:区分 **primitive token**(原始值 `--blue-500`)和 **semantic token**(语义 `--color-primary` 指向某 primitive)。换品牌色只改映射,不动组件。
> ⏳ `next-themes` 处理"记住选择 + 跟随系统 + 防刷新闪烁(FOUC)"。

**讲回来检验**:"暗色模式为什么不用改组件代码?" "primitive vs semantic token?"
**Recall 实操**:写一套 Recall token(色/距/字/角)+ 暗色模式,切换无闪烁。
**过关标准**:切暗色全站变、组件代码没动、对比度仍达标。
**该存的 1 张卡**:正面"暗色模式本质是?" 反面:第二套 token 值,组件代码不变。

---

### M3.2 · 组件分层 + 与 Tailwind/shadcn 的关系 🔥 ⭐⭐⭐

**目标**:小积木拼大积木;讲清 Tailwind / shadcn / token 三者关系(面试常问)。

**✍️ 三层组件**:

| 层 | 例子 | 特征 |
|---|---|---|
| Primitive(原子) | Button, Badge, ProgressBar | 无业务,纯样式+行为 |
| Composite(组合) | SkillCard, XPBar | 拼原子 + 一点业务 |
| Pattern(模式) | SkillTree 整页 | 拼组合 + 布局 |

> 分层后改 Button 圆角,全站自动跟变 —— 这是"设计系统"区别于"一堆页面"的地方。

**✍️ Tailwind / shadcn / token**:

| 它是什么 | 大白话 | 你怎么用 |
|---|---|---|
| Tailwind | 把 CSS 变成 class 工具箱(`p-2`=padding) | 写样式的手 |
| shadcn/ui | **不是组件库**,是"把组件源码复制进你项目"的配方 | 你**拥有**代码,随便改 |
| 你的 token | 喂给上面两个的"颜色/尺寸字典" | 地基 |

> ⭐**面试金句**:shadcn 不是 npm 装的黑盒,是把组件源码放进 `components/ui/` 让**你拥有** → 设计工程师能改到像素级,正是你的卖点。
> shadcn 的可访问交互(对话框/下拉/Tabs)底层是 **Radix UI primitives** —— a11y 的键盘/焦点/ARIA 不用自己手写焦点陷阱,全靠它。
> 三层咬合:token 写进 CSS 变量 → Tailwind config 映射成 class(`bg-primary`)→ shadcn 组件用这些 class。改 token,三层一起变。

**讲回来检验**:"shadcn 和普通组件库差在哪?" "改一个 token 怎么传到组件?"
**Recall 实操**:`<XPBar value={320} max={500} />` —— 受控、可复用、内部用 token,外部只传数据;再拼出 `<SkillCard>`。
**过关标准**:XPBar / SkillCard 用 token 写成,受控可复用。
**该存的 1 张卡**:正面"shadcn 是组件库吗?" 反面:不是,是把源码复制进你项目的配方,底层 a11y 靠 Radix。

---

### M3.3 · 可访问性 a11y 🔥 ⭐⭐⭐(设计师的良心 + 面试加分)

**目标**:让用键盘、用读屏、看不清的人也能用 Recall。这是**专业度信号**。

> a11y = accessibility,无障碍。WCAG = Web Content Accessibility Guidelines,无障碍国际及格线。ARIA = Accessible Rich Internet Applications,给元素贴"我是什么/什么状态"标签给读屏听。

**✍️ WCAG 入门四把刀**:

| 项 | 做什么 | Recall 例 |
|---|---|---|
| 语义 | 按钮就用 `<button>`,不是 `<div onClick>` | 技能节点可点 → `<button>` |
| 焦点 | 键盘 Tab 走得到、看得见焦点框 | 别 `outline:none` 不补 |
| 对比度 | 文字/背景 ≥ 4.5:1 | XP 金字够深 |
| ARIA | 进度条加 `role` + 状态 | 读屏念"经验 320/500" |

```tsx
<div role="progressbar" aria-valuenow={320}
     aria-valuemin={0} aria-valuemax={500}>
  {/* 视觉条 */}
</div>
```
> ⭐**作品集杀手锏**:录一段"全程只用键盘操作技能树"的视频。90% 候选人做不到 → 立刻显出设计工程师的专业。
> 落地工具:浏览器装 **axe** 扩展或跑 **Lighthouse** 的 a11y 评分,把错误清零。a11y 不只这一节——表单要 `<label>`、列表用语义标签、RN 用 `accessibilityLabel`(见 M5)。

**讲回来检验**:"为什么 `<div onClick>` 不如 `<button>`?" "进度条怎么让读屏念出来?"
**Recall 实操**:技能节点用 `<button>` + 可见焦点框;XPBar 加 `role="progressbar"`;用 axe 跑到 0 错。
**过关标准**:全程键盘可操作技能树 + axe 无错(录视频)。
**该存的 1 张卡**:正面"a11y 四把刀?" 反面:语义标签、键盘焦点、对比度 4.5:1、ARIA。

> ⏳⭐ **Storybook(组件试衣间)**:给每个组件单独开一页摆出所有状态(空/满/加载/禁用)——你的"代码版 Figma 组件页"。先给 XPBar / SkillCard 各写 3–4 个 story(0%、50%、100%、满级)。面试给链接 = 直接证明"我懂设计系统"。

---

## M4 · 动效 Motion ★🔴🔥(差异化武器,最出彩)

> M4.0 命名:库 2024 起从 "Framer Motion" 改名 **Motion**,新项目用包名 `motion`,React 里 `import { motion } from "motion/react"`(现 v12)。老教程里的 `framer-motion` 仍可见,API 基本一致。**RN 端不是这个库**——RN 用 Reanimated/Moti(见 M5),心智相通(声明式、只动 transform/opacity)但 API 不同,别混用。

---

### M4.1 · motion 组件 + variants 编排 🔥 ⭐⭐⭐

**目标**:把 `<div>` 换成 `<motion.div>`(给起点终点,它画中间);用 variants 让技能树节点**逐个点亮**。

```tsx
import { motion } from "motion/react";
<motion.div
  initial={{ opacity: 0, y: 8 }}   // 起点
  animate={{ opacity: 1, y: 0 }}   // 终点
  transition={{ duration: 0.25 }}  // 怎么走
/>
```
> 为什么 `y` 不用 `top`:`y` 走 transform(GPU,丝滑),`top` 触发 layout(卡)。性能铁律见 M4.3。

**✍️ variants(给动画状态起名 + 父子编排)**:
```tsx
const list = { visible: { transition: { staggerChildren: 0.06 } } };
const item = { hidden: { opacity: 0, y: 10 }, visible: { opacity: 1, y: 0 } };
```
```tsx
<motion.ul variants={list} initial="hidden" animate="visible">
  {skills.map(s => <motion.li key={s.id} variants={item} />)}
</motion.ul>
```
> 🔥 **Recall 炫酷点**:技能树节点 stagger 0.06s **逐个**点亮,不是一起蹦 → 一下就有"游戏感"。

**讲回来检验**:"为什么动 y 不动 top?" "variants 怎么让父子排队?"
**Recall 实操**:技能卡入场淡入 + 上移;技能树节点逐个点亮。
**过关标准**:能讲"变体让动画声明式 + 父子编排"。
**该存的 1 张卡**:正面"技能树逐个点亮靠什么?" 反面:variants + `staggerChildren`。

---

### M4.2 · layout 动画 + AnimatePresence + 手势 🔥 ⭐⭐⭐

**目标**:元素移位自动平滑过渡;删除时也能放退场动画;加手感。

> `layout` prop:位置/大小变了**自动**补平滑过渡(底层是 FLIP = First-Last-Invert-Play,量两个位置用 transform 补差)。
> `AnimatePresence`:元素**被删除时**也能放退场动画(React 默认直接消失)。

```tsx
<AnimatePresence>
  {leveledUp && (
    <motion.div
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      exit={{ scale: 0.8, opacity: 0 }}>  {/* 退场 */}
      升级!
    </motion.div>
  )}
</AnimatePresence>
```
> 手势:`whileHover={{ scale: 1.03 }}` / `whileTap={{ scale: 0.97 }}` —— 悬停微抬、按下回弹。**手感就是设计工程师的签名。** ⏳ 进阶:`useScroll` 让 XP 条随滚动填充(别滥用,滚动动画多了晕)。

**讲回来检验**:"`layout` 解决什么?" "AnimatePresence 解决什么?"
**Recall 实操**:技能重排加 `layout` 平滑挪位;"升级"弹窗用 AnimatePresence 进退;节点 `whileHover` 微抬发光。
**过关标准**:升级弹窗优雅进退 + 卡片重排平滑。
**该存的 1 张卡**:正面"元素被删还能放动画靠什么?" 反面:AnimatePresence + `exit`。

---

### M4.3 · 动效设计原则 + 性能 🔥 ⭐⭐⭐(最值钱的一节)

**目标**:动画的本事不在"会动",在"知道**何时别动**"。这是普通前端 vs 设计工程师的分水岭。

**✍️ 四条铁律**:

| 原则 | 具体 | 为什么 |
|---|---|---|
| 时长 | UI 微动 150–300ms | 再长就拖沓 |
| 缓动 | 用 `ease-out`(快进慢出) | 像真实物体 |
| 只动 transform/opacity | 不动 width/top/margin | 只有这俩不触发重排,稳 60fps |
| 尊重偏好 | `prefers-reduced-motion` 关大动画 | a11y:有人晕动效 |

```tsx
import { useReducedMotion } from "motion/react";
const reduce = useReducedMotion();  // 尊重"减少动效"系统设置
const y = reduce ? 0 : 12;
```
> ⭐**面试金句三连**:① "我只动 transform 和 opacity,因为它们不触发 layout/paint,稳 60fps。" ② "我接 `prefers-reduced-motion`,动效也是 a11y。" ③ "动效要克制——它服务于反馈和层级,不是装饰。"

**讲回来检验**:"为什么只动 transform/opacity?" "动效和 a11y 有什么关系?"
**Recall 实操**:全部 Recall 动效只用 transform/opacity;接 `useReducedMotion` 关大动画。
**过关标准**:能讲三条金句 + `prefers-reduced-motion` 生效。
**该存的 1 张卡**:正面"动画只该动哪两个属性?" 反面:transform 和 opacity(不触发重排)。

---

## M5 · React Native:Recall 手机版 🔥

> RN = React Native:用你已会的 React 写法,但渲染到**手机原生控件**(不是网页)。90% React 知识直接迁移,只换 5 样东西。

---

### M5.1 · 心智 + 布局 + Expo 起步 🔥 ⭐⭐⭐

**目标**:说清 RN 和 Web 差的 5 样;用 Expo 起一个能在手机上跑的屏。

> Expo = 开箱即用的 RN 工具箱,省掉配置原生环境的苦。

**✍️ Web ↔ RN 对照(背这张就懂一半)**:

| Web | RN | 大白话 |
|---|---|---|
| `<div>` | `<View>` | 装东西的盒子 |
| `<p>` `<span>` | `<Text>` | **所有文字必须包在 `<Text>` 里** |
| `<img>` | `<Image>` | 图片 |
| `<button>` | `<Pressable>` | 能按的东西 |
| CSS / className | `StyleSheet` 对象 | 样式写成 JS 对象,`camelCase` |

> **没有 DOM、没有 window**。DOM = Document Object Model,网页的"积木树"。⭐面试爱问"RN 是 WebView 吗?"**答:不是**,它把组件翻译成真原生控件(iOS `UIView` / Android `View`),手感原生。
> 布局三个差异:默认 `flexDirection: column`(竖);单位是**纯数字**(=dp,密度无关像素,不同清晰度看起来一样大);样式是 JS 对象。

```tsx
import { View, Text, StyleSheet } from "react-native";
export default function Home() {
  return (
    <View style={s.box}><Text style={s.title}>Recall 技能树</Text></View>);
}
const s = StyleSheet.create({
  box: { flex: 1, justifyContent: "center", alignItems: "center" },
  title: { fontSize: 24, fontWeight: "600" },
});
```
起步:`npx create-expo-app@latest recall-mobile` → `npx expo start` → 手机装 "Expo Go" 扫码即看(不用 Xcode/Android Studio)。

**讲回来检验**:"文字为什么必须包 `<Text>`?" "RN 是 WebView 吗?"
**Recall 实操**:起项目,屏幕中央显示"Recall 技能树";做一个 `SkillCard`(用 token 的颜色思路,值写进 StyleSheet)。
**过关标准**:自己手机能看到这行字 + 一张技能卡。
**该存的 1 张卡**:正面"RN 和 Web 差哪 5 样?" 反面:View/Text/Image/Pressable/没有 DOM。

---

### M5.2 · 导航 + 列表性能 🔥 ⭐⭐⭐

**目标**:页面能跳(expo-router);长列表不卡(FlashList)。

**✍️ 导航 expo-router**(文件即路由,和 Next.js App Router 一个心智):

| Web(Next.js) | RN(expo-router) |
|---|---|
| `app/cards/page.tsx`→`/cards` | `app/cards.tsx` |
| `[id]` 动态段 | `[id].tsx`(`useLocalSearchParams()` 拿 id) |
| `<Link href>` / `useRouter().push` | 几乎一样 |

> 老牌选手 React Navigation(代码配路由);expo-router 建在它之上的"文件路由皮",新项目首选。

**✍️ 列表性能**:

| 方式 | 何时用 | 问题 |
|---|---|---|
| `.map()` 全渲染 | 几条死数据 | 一千条 = 创建一千控件 → 卡死 |
| `FlatList`(自带) | 长列表 | 只渲染可见的几条(虚拟化),够用 |
| `FlashList`(Shopify)🔥 | 长列表 + 更顺 | 2026 首选,更快更省内存 |

```tsx
import { FlashList } from "@shopify/flash-list";
<FlashList
  data={cards}
  keyExtractor={(c) => c.id}     // 稳定 key,别用 index
  renderItem={({ item }) => <SkillCard name={item.name} xp={item.xp} />}
/>
```
> 虚拟化(virtualization)= 只把眼睛看得见的几行真正画出来,滑走的回收。
> ⚠️ **版本提示**:FlashList **v1** 要你估每行高度(`estimatedItemSize`);**v2(2025 重写)自动测量,不用估了**——别再写那个 prop。
> v2 需要 RN **新架构**(New Architecture,RN 重写的底层引擎,Expo SDK 53+ 新项目默认就开)。`create-expo-app` 新建的项目默认开着,你直接能用;老项目报错先确认新架构已开。
> ⭐两个陷阱:① `renderItem` 里写内联函数/对象会每帧重建 → 提取组件或 `useCallback`;② 用 index 当 key → 列表抖动、状态错位。

**讲回来检验**:"长列表为什么不能 `.map()`?" "expo-router 和 Next.js 哪里像?"
**Recall 实操**:卡片列表 `index.tsx` → 详情 `[id].tsx` → 复习页;列表用 FlashList 塞 500 条假数据滚一滚。
**过关标准**:点列表进详情、系统返回能回;500 条不卡。
**该存的 1 张卡**:正面"RN 长列表用什么、为什么?" 反面:FlatList/FlashList 做虚拟化;`.map()` 会卡死。

---

### M5.3 · 调后端 API + 本地通知 🔥 ⭐⭐

**目标**:手机拉 FastAPI 到期卡;到点弹"该复习了"。

**✍️ Web ↔ RN 取数差异**:
- `fetch` / TanStack Query **完全通用** ✅。
- **没有 CORS**(Cross-Origin Resource Sharing,浏览器的跨域安全锁)——RN 不是浏览器,这条烦恼没了(安全仍靠后端 token)。
- **连本机后端的地址**(最经典的坑):

| 在哪跑 | 地址写 |
|---|---|
| iOS 模拟器 | `localhost` 可用 |
| Android 模拟器 | `10.0.2.2` |
| 真机 | 电脑局域网 IP(如 `192.168.x.x`),**不是 localhost** |

```tsx
import { useQuery } from "@tanstack/react-query";
const API = "http://192.168.1.10:8000";   // 真机:电脑局域网 IP
function useDueCards() {
  return useQuery({
    queryKey: ["cards", "due"],
    queryFn: async () => {
      const r = await fetch(`${API}/v1/cards?due=today`);
      if (!r.ok) throw new Error("拉卡失败");
      return r.json();
    },
  });
}
```

**✍️ 本地通知(调原生能力三步:装库 → 求权限 → 调用)**:
```tsx
import * as Notifications from "expo-notifications";
async function scheduleReview(inSeconds: number) {
  const ok = await Notifications.requestPermissionsAsync(); // 1 求权限
  if (!ok.granted) return;                                  // 被拒兜底
  await Notifications.scheduleNotificationAsync({           // 2 排闹钟
    content: { title: "Recall", body: "有卡片该复习了 📚" },
    trigger: { type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
               seconds: inSeconds, repeats: false },        // 过 N 秒后响
  });
}
```
> ⚠️ trigger 用结构化写法(`type: TIME_INTERVAL`);iOS 若要 `repeats`,秒数必须 ≥60。

**讲回来检验**:"真机连本机后端为什么写 localhost 连不上?" "调原生能力三步?"
**Recall 实操**:`useDueCards()` 拉到期卡喂给 FlashList(带 loading/error);复习完按下次到期时间排一条本地通知。
**过关标准**:真机看到后端真卡 + 锁屏收到提醒。
**该存的 1 张卡**:正面"RN 真机连本机后端地址写啥?" 反面:电脑局域网 IP,不是 localhost。

> ⏳ **真机/打包心智**:JS 改了热更新秒见;**装了新原生库必须重新打 Development Build**,Expo Go 不再够用。真上架用 EAS(Expo Application Services,云打包)`eas build`。本课不要求走完上架。

---

## ④ 能力关卡清单(面试自信依据)

> 每过一关 = 一条能写进简历、能当面演示的能力。**自己能独立、不偷看做到**才算过。

| 关卡 | 解锁模块 | 独立做到 | 简历句 |
|---|---|---|---|
| **G1** React 渲染直觉 | M1.1–1.2 | 不看代码讲清"何时重渲染" + 函数式更新 + 受控表单 | "deep understanding of React hooks" |
| **G2** React 19 表单 | M1.3 | `useActionState` 做"新建卡片"含 pending/error | "modern React forms (Actions)" |
| **G3** 状态架构 + 性能 | M1.5–1.6 | 给任意状态选对家;Profiler 定位重渲染并修好 | "state mgmt & perf" |
| **G4** Next.js 数据流 | M2.2–2.4 | 正确划 Server/Client 边界;RSC 取数 + Server Action 写 + tag 失效 | "App Router / RSC" |
| **G5** 设计系统 ★ | M3 | token + 暗色无闪烁 + a11y axe 0 错 + Storybook | "built a design system" |
| **G6** 动效 ★ | M4 | 技能树 stagger 点亮 + 升级弹窗进退 + 性能金句 + 纯键盘视频 | "motion / design engineering" |
| **G7** React Native | M5 | 列表+导航不掉帧 + 真机拉 FastAPI + 本地通知 | "React Native / Expo" |
| **G8** 顶石 | 全部 | Web 仪表盘 + 手机版端到端可演示 + 讲清取舍 | "shipped a full design-engineered product" |

> **G5 + G6 是简历头牌**(设计工程师差异化),占最多打磨时间。

**G8 顶石产出物(收口)**:
- **Web 仪表盘**:登录态 → 技能树(RSC 拉 `/stats`)→ 复习按钮(Server Action 回写)→ XP 动效升级 → 暗色 + 全键盘可用。
- **手机版**:卡片列表(FlashList)→ 详情 → 复习 → 收到本地通知。
- **面试 60 秒电梯话术(背下来改成你自己的)**:
> "Recall 前端用 Next.js App Router:静态壳在服务器渲染、技能树数据 RSC 直接 await FastAPI,复习用 Server Action 回写并 updateTag 失效缓存。状态上本地用 useState、全局高频的 XP 用 Zustand、服务器数据用 TanStack Query。我的主场是设计系统——一套 primitive/semantic 双层 token、shadcn(我拥有源码)+ Radix 保证 a11y、暗色无闪烁、技能树全键盘可操作。动效用 Motion:只动 transform/opacity 稳 60fps、接 prefers-reduced-motion,技能节点 stagger 点亮、升级弹窗 AnimatePresence。手机版用 Expo + expo-router + FlashList 复用同一套设计语言。"

---

## ⑤ 与 5 天主课 + BACKEND.md 协同排期

> **原则**:FRONTEND 是在 BACKEND 冲刺**之后**(或主课第 1 周 BACKEND 仅起步时,纯不依赖后端的部分可低载并行)启动的独立集训。**不与 BACKEND 同时双开 10–12h。** 同一天不双开两门新硬概念。

| 阶段 | 主课(5天) | BACKEND.md | FRONTEND.md(本课) |
|---|---|---|---|
| 第 1 周 | 5 天核心 | M0–M5 起步 | M0 诊断 + M1.1–1.2(纯前端,不依赖后端,可并行) |
| BACKEND 冲刺 D6–D12 | 已毕 | 每天 10–12h 推 M5→M12 | **暂停或仅"读样例"低载**,不抢带宽 |
| 前端冲刺 第 3–4 周 | — | 维护(`/stats`、`/cards/{id}/review` 已就绪)| 每天 10–12h:M1.3–M2(接后端)→ M3–M4(纯前端)→ M5 |

**前端冲刺每日节奏(每天 10–12h)**

| 时段 | 时长 | 干嘛 |
|---|---|---|
| 晨练 | 30–45 分钟 | **次日重写**昨天核心片段 + 抽卡 |
| 上午 | 2–3h | 新概念主循环(读样例→讲回来→敲一半) |
| 下午+晚 | 余下 | 全实操(挂 Recall)+ 缝合 |

**缝合 + 防超载护栏**
- 每个大模块结束做一次"缝合课":只练不学新,把小节连起来。
- 红线:任一天出现**红灯**(敲码偷看超 3 次)→ **停新概念**,改纯缝合/复习。宁可慢,不可夹生。
- **M3/M4 不依赖后端**——后端没就绪或主课累时切来这里,永不空转。
- 每模块结束:更新 `SCRATCHPAD.md`(落地)+ `SCRATCHPAD.local.md`(▶ Resume here)。

---

## ⑥ 诚实边界

- 这门课给的是**设计工程师的扎实手艺 + 能讲清原理 + 一个亮眼作品(Web 仪表盘 + 手机版)**,不是 senior 头衔。
- 「能独立写、能讲回原理、能演示」三件套达成 → 可自信投 junior→mid。
- **不是**"精通 React fiber 内部调度 / 大规模渲染调优 / 完整上架流程"——那需要更久的实战年头。
- 你的差异化(G5 设计系统 + G6 动效 + 纯键盘 a11y 视频)是简历里**少有人拿得出**的组合,足以让你在面试里把"为什么"讲到底。
- 技术基线锁 2025/2026:React 19+(Actions、`use`、RSC)、Next.js 16 App Router + Cache Components(API 演进中,做相关步骤当天核对官方文档)、Motion(`motion/react`,v12)、FlashList v2、expo-router。

---

## 缩写表(首次出现处也会再点一句)

| 缩写 | 全称 | 一句大白话 |
|---|---|---|
| JSX | JavaScript XML | 在 JS 里写"长得像 HTML"的标签 |
| state | 状态 | 会变、变了要重画界面的数据 |
| props | properties | 父传子的只读数据 |
| hook | 钩子 | `use` 开头的函数,给组件加能力 |
| RSC | React Server Component | 在服务器渲染好、不带 JS 到浏览器的组件 |
| SSR/SSG/ISR/PPR | Server-Side Rendering / Static Site Generation / Incremental Static Regeneration / Partial Prerendering | 四种"何时把页面画出来"的策略 |
| SEO | Search Engine Optimization | 让搜索引擎看得懂你的页面 |
| TS | TypeScript | 给 JS 加类型标签,写错早发现 |
| a11y | accessibility | 让残障用户(键盘/读屏/低视力)也能用 |
| WCAG | Web Content Accessibility Guidelines | 无障碍的国际及格线 |
| ARIA | Accessible Rich Internet Applications | 给元素贴"我是什么/状态"标签给读屏听 |
| token | design token | 设计的"乐高积木",颜色/间距的命名值 |
| HSL | Hue/Saturation/Lightness | 色相/饱和度/亮度,比 hex 好调主题 |
| FOUC | Flash of Unstyled Content | 刷新瞬间样式没加载好的闪烁 |
| FLIP | First-Last-Invert-Play | 布局动画的底层把戏:量两个位置用 transform 补差 |
| RN | React Native | 用 React 写手机 App |
| Expo | — | 开箱即用的 RN 工具箱 |
| DOM | Document Object Model | 网页的"积木树"(RN 没有它) |
| dp | density-independent pixel | 密度无关像素,不同清晰度看起来一样大 |
| CORS | Cross-Origin Resource Sharing | 浏览器的跨域安全锁(RN 没有) |
| EAS | Expo Application Services | Expo 的云打包/上架服务 |
| API | Application Programming Interface | 两个程序说话的"菜单" |