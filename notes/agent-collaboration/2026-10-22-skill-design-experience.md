---
date: 2026-10-22
tags:
  - Skill设计
  - Agent协作
  - 工作流进化
  - 经验总结
visibility: link-only
---

# 从「内容归档」到「技能进化」：一次 Skill 设计与制作复盘

> 状态：待审稿（`link-only`），已入库但不对外宣传；审稿通过后再改为 `public`。

## 一、给人类

这次把技能体系从零搭起来，并把可分享的部分放进了个人仓的 `agents/`：`agents/skills/skill-evolution` 负责把刚完成的工作流提炼成可复用技能并按反馈进化；`agents/roles`、`agents/workflows`、`agents/fun` 预留角色、工作流与趣味提示词的分享位。工作区内部另有一个内容归档技能 `organize-content`，负责把新增素材整理到正确目录；最大的教训是先把「整理内容」和「整理流程」分开。

- 有素材要归位：说「整理今日新增经验到对应目录」（工作区内部）。
- 有流程要固化：说「把这个流程沉淀成 skill」。
- 改完跑 `lint_skills.py`；对外内容按 `agents/README.md` 的脱敏红线检查。

## 二、给 Agent：完整版

> 以下路径均相对本仓根目录（`openmylife/`），不依赖作者电脑上的工作区。

### 1. 这次做了什么

| 产出 | 位置 | 作用 |
|---|---|---|
| Agent 产物目录 | [`agents/README.md`](../../agents/README.md) | 角色 / 工作流 / 趣味提示词 / skill 的分类、命名与脱敏红线 |
| 技能索引 | [`agents/skills/README.md`](../../agents/skills/README.md) | 技能结构、命名与 front-matter、新增流程 |
| 技能进化元技能 | [`agents/skills/skill-evolution/SKILL.md`](../../agents/skills/skill-evolution/SKILL.md) | 把刚完成的工作流提炼成可复用技能，并按反馈进化 |
| 进化细则 | [`agents/skills/skill-evolution/references/evolution.md`](../../agents/skills/skill-evolution/references/evolution.md) | 证据模板、可复用性评分、Hermes 对照、质量清单、合并 / 归档规则 |
| 技能库校验脚本 | [`agents/skills/skill-evolution/scripts/lint_skills.py`](../../agents/skills/skill-evolution/scripts/lint_skills.py) | 只读：frontmatter、name 与目录一致、索引登记、相对引用、空壳目录 |
| 仓库索引同步 | [`README.md`](../../README.md) / [`CONTEXT.md`](../../CONTEXT.md) / [`llms.txt`](../../llms.txt) | 目录地图、命名约定、脱敏规则与 AI 读取入口 |

> 工作区内部另有一个内容归档技能 `organize-content`（含路由表与只读体检脚本），负责把新增素材整理到正确目录；它是作者本地工作流的一部分，**未随本仓发布**。

### 2. 最大的坑：「沉淀」是歧义词

最初把「自动沉淀流程的 skill」理解成「把素材归档到对应目录」，于是先做了一个内容归档技能。用户纠正后才知道，真正想要的是**把当前工作流提炼成 skill 的元技能**；而「整理今日新增经验到对应目录」是另一个独立的内容技能。

| 说法 | 最初理解 | 实际含义 | 处理 |
|---|---|---|---|
| 增加一个自动沉淀流程的 skill | 把素材归档 | 把当前工作流提炼成 skill，类似 Hermes 进化体系 | 新建 `skill-evolution` |
| 整理今日新增经验到对应目录 | 以为与上者是同一件事 | 独立的内容归档技能 | 拆成独立内容技能 |

**可迁移规则**：先确认「沉淀 / 整理 / 归档」的宾语是**内容**还是**流程**。一个词同时对应两条流程时，先拆词，再拆技能；否则触发器会打架，整轮产出都要返工。

### 3. 最终结构

```text
agents/
├── README.md                     ← 目录定位、文件约定、脱敏红线
├── roles/                        ← 角色设定（待补）
├── workflows/                    ← 工作流提示词（待补）
├── fun/                          ← 好玩 / 实验性提示词（待补）
└── skills/
    ├── README.md                 ← 技能索引与格式约定
    └── skill-evolution/          ← 已公开的元技能
        ├── SKILL.md
        ├── references/evolution.md
        └── scripts/lint_skills.py
```

| 产物 | 类型 | 触发词（摘要） | 输入 | 输出 |
|---|---|---|---|---|
| `skill-evolution` | 元技能 | 把这个流程沉淀成 skill、以后都这么做、固化这套做法、进化技能 | 刚完成的工作流、用户纠正、技能使用反馈 | 新建 / 更新的 `SKILL.md` + 注册索引 + 验证结果 |
| 内容归档（工作区内部） | 内容技能 | 整理今日新增经验到对应目录、归档、整理 inbox、这条放哪 | 一个路径 / 一段素材 / 一次 inbox 巡检 | 规范内容 + 索引同步 + 体检报告 + 提交状态 |

> 一句话分工：内容技能整理**内容**，`skill-evolution` 整理**流程**。

### 4. 设计原则（可迁移）

| 原则 | 做法 | 为什么 |
|---|---|---|
| 对齐 Hermes 学习循环 | Observe → Distill → Reuse → Refine | 技能不是一次写完，而是从真实任务中长出来，再按反馈修补 |
| 3+ 次门槛 | 同一模式成功重复 3 次以上才固化；至少 2 次且稳定可提前；用户明确要求可直接做 | 防止一次性任务把技能库变成垃圾场 |
| 程序性 vs 事实性 | 「怎么做」进技能；「是什么 / 偏好 / 参数」进 memory / TODO / 项目文档 | 技能是程序性记忆，不是日记 |
| 一个技能只做一件事 | 触发器、输入输出、边界都要能一句话说清 | 过宽的技能（「所有 XX」）不会被正确加载 |
| 渐进披露 | `SKILL.md` 放主流程；细节放 `references/`；脚本放 `scripts/` | 只加载需要的内容，减少 token 与误读 |
| 触发器唯一 | 两个技能不能共用同一个核心触发词 | 否则 Agent 无法判断该加载哪个 |
| 脚本只读 | 脚本做清单、校验、统计；分类、隐私判断、发布确认由 Agent / 人做 | 自动写文件 / 推送的风险不可逆 |
| 索引同步 | 新增 / 改名技能必须更新 `agents/skills/README.md`；结构变化同步 README / CONTEXT / llms | 否则技能不可发现，旧名会变成死引用 |
| 对外分享脱敏 | 只用相对路径；不写真实姓名、密钥、隐私、本机绝对路径 | 对外内容一旦发布就不可撤回 |

### 5. 这次实际走的流程

1. **盘点需求**：区分「内容归档」与「工作流沉淀」两类需求。
2. **写技能总约定**：定义目录、frontmatter、生命周期、脚本准入。
3. **做内容技能**（工作区内部）：路由表 + 只读体检，跑通内容归档链路。
4. **接受纠正**：把内容技能与元技能彻底拆开，清除旧名引用。
5. **做元技能**：`skill-evolution` + `evolution.md` + `lint_skills.py`，对齐 Hermes 循环。
6. **建立分享目录**：`agents/` 下设 `roles` / `workflows` / `fun` / `skills`，把 `skill-evolution` 改编为公开副本。
7. **同步规则**：在根 `AGENTS.md`、本仓 `README.md` / `CONTEXT.md` / `llms.txt` 写入相对路径与脱敏红线。
8. **验证**：
   - 在仓库根目录运行 `python agents/skills/skill-evolution/scripts/lint_skills.py` → 1 个技能，`ERROR 0 · WARN 0`，退出码 0；
   - 内容归档的只读体检在工作区内部单独运行，未随本仓发布。

### 6. 踩坑清单

| 坑 | 现象 | 修正 | 可迁移规则 |
|---|---|---|---|
| 「沉淀」歧义 | 做成了内容归档，整轮返工 | 拆成内容技能 + 元技能 | 先确认宾语是内容还是流程 |
| 触发器冲突 | 两个技能都可能响应「沉淀」 | 内容技能用「整理 / 归档」；元技能用「沉淀成 skill」 | 核心触发词必须唯一 |
| 复制后路径失效 | 技能原文件引用作者工作区，复制到个人仓后链接断开 | 公开副本改为本仓相对路径，去掉工作区专属链接 | 复制技能 = 重新适配路径与依赖 |
| 重命名后旧引用 | 文档、命令、索引仍指向旧名 | 全仓 grep + 更新索引 | 改名后必须全仓搜索旧名 |
| 审计脚本误报 | README 里的占位路径、inbox 原始素材链接、旧报告失效链接被当成错误 | 跳过含 `...` 的占位符与 inbox；内部文档降为 WARN；公开仓仍为 ERROR | 校验脚本要区分「公开风险」与「存量噪音」 |
| 脚本缓存 | `py_compile` 生成 `__pycache__` | `.gitignore` 加 `__pycache__/`、`*.pyc`，并清理 | 脚本产物不要进版本库 |
| 工具加载 | 本地工具通过目录联接加载技能，重命名后当前会话仍显示旧技能 | 新会话 / 重新加载后生效 | 改技能只改实体目录，不在联接路径内建副本 |
| 存量 WARN | 无日期笔记、旧报告失效链接一直存在 | 保留 WARN，不冒充本次改动 | 体检要能区分新问题与历史欠账 |

### 7. 给下一个 Agent 的复用清单

创建 / 更新技能前，逐项确认：

- [ ] 这是**内容技能**还是**元技能**？两者的触发词、输入输出、验证方式是否已分开？
- [ ] 现有 `agents/skills/README.md` 是否已有同触发器、同步骤的技能？有则合并 / 扩展。
- [ ] 是否满足固化门槛：用户明确要求，或同一模式重复 3 次以上（至少 2 次且稳定）？
- [ ] 四个问题是否回答清楚：触发词 / 输入 / 输出 / 边界（不能做什么）？
- [ ] `SKILL.md` 是否只放主流程，细节是否放进 `references/`？
- [ ] frontmatter 是否有 `name` / `description` / `version`，且 `name` 与目录名一致？
- [ ] 是否更新了 `agents/skills/README.md` 索引？结构变化是否同步 README / CONTEXT / llms？
- [ ] 是否跑了 `python agents/skills/skill-evolution/scripts/lint_skills.py`，且 0 ERROR？
- [ ] 是否用真实任务试跑，并记录验证日期？
- [ ] 对外分享前是否按 `agents/README.md` 检查路径 / 姓名 / 密钥等敏感信息？

**人类可直接说的两句话**

```text
整理今日新增经验到对应目录：<路径或一句话素材>。
把这个流程沉淀成 skill：<一句话流程>；触发词是 <...>；不做 <...>。
```

### 8. 文件索引

| 文件 | 角色 |
|---|---|
| [`agents/README.md`](../../agents/README.md) | 分享目录的定位、分类、命名与脱敏红线（先读这个） |
| [`agents/skills/README.md`](../../agents/skills/README.md) | 技能索引、格式约定、新增流程 |
| [`agents/skills/skill-evolution/SKILL.md`](../../agents/skills/skill-evolution/SKILL.md) | 工作流提炼 / 技能进化主流程 |
| [`agents/skills/skill-evolution/references/evolution.md`](../../agents/skills/skill-evolution/references/evolution.md) | 证据模板、评分、质量清单、归档规则 |
| [`agents/skills/skill-evolution/scripts/lint_skills.py`](../../agents/skills/skill-evolution/scripts/lint_skills.py) | 技能库只读校验 |
| [`README.md`](../../README.md) | 人类入口与目录索引 |
| [`CONTEXT.md`](../../CONTEXT.md) | AI 上下文：目录地图、命名、隐私边界 |
| [`llms.txt`](../../llms.txt) | AI 可读入口与整理步骤 |

> 工作区内部的 `organize-content` 及其路由表 / 体检脚本未随本仓发布，不在本索引内。

### 9. 一句话收尾

**先分清整理的是内容还是流程，再决定写哪个技能；技能不是文档，是下一次能直接执行的动作序列。**
