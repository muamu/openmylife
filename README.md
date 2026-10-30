# openmylife

> 把自己开源的人 · I build in public, and the work IS the marketing.

> **这份仓库有两个读者**：人类读这里（[README.md](./README.md)），AI 读 [CONTEXT.md](./CONTEXT.md)。

> **状态：阶段 0（开荒）** — 骨架已就位，正在把过去的积累搬进来。

> **协议适用范围**：本仓文字内容适用 [CC BY 4.0](./LICENSE-CONTENT)，代码与脚本适用 [MIT](./LICENSE)；两者冲突时以文件类型判断。他人原文摘录与 AI 总结除外（见文末「关于第三方内容」）。

## 每日推荐

> 最新一条 + 随机两条旧文，最多三条 —— 轮换展示，宁缺毋滥。

- **2026-10-30** · [AI 味拆三层：大多数人洗的，是最不管用的那一层](https://openmylife.xyz/articles/ai/ai-flavor-three-layers.html) —— AI 味不是一种味道，而是三层：词、句、结构。520 万字对照统计（口径见附录 A）显示，黑名单词与破折号已经失效；真正决定读者信不信的，是结构与材料。附七种可数句式与存疑清单。
- **2026-10-21** · [MiniMax 与智谱 2026 中报对照：收入、亏损与 ARR](https://openmylife.xyz/articles/finance/minimax-zhipu-h1-2026.html) —— 两家港股大模型公司上市后的首份中报对照：收入、亏损、ARR 与估值，数据截至 2026-10-21。
- **2026-10-17** · [开源自己 · 灵感备忘录](https://github.com/muamu/openmylife/blob/main/ideas/2026-10-17-openmylife-ideas.md) —— 把「开源自己」当成一本富媒体电子书：仓库目录是章，commit 是修订记录，自带时间线与可引用性。

## 我是谁

我是尚盐。一个尝试"开源自己"的独立开发者。

- **终身学习**
- **独立开发者**
- **追踪与思考 AI 发展十多年**
- **前互联网小公司产品经理**
- **金融市场里已经亏空的投机者**
- **从开发一个 个人副脑Agent框架 转到 开发DSH记忆插件**

这些经历像我人生的一组长期实验：学什么、做什么、怎么判断、如何承担后果。现在开始把实验记录公开在这里。

### 我在解决的三个问题

1. **经验留不下来**：想法散落在备忘录、聊天记录和截图里，无法检索、无法引用，也换不来下一次机会。
2. **信息太多，可信太少**：AI 时代不缺答案，缺的是「谁在什么版本上亲测过、结论是什么」。
3. **普通人用不上 AI 的长期复利**：不会代码、不会维护仓库的人，很难把自己的知识变成可被 AI 读取、可被他人复用的资产。

我的解法很笨，但可复用：用 git 把思考、经验和作品版本化；用 `README.md` 给人类读，用 `CONTEXT.md` / `llms.txt` 给 AI 读；让公开变成储蓄，而不是消耗。

## 当前项目：OpenMyLife（开源自己）

OpenMyLife 是一套「把自己当成长期维护的开源项目」的方法与工具。

- **001 号样板间**：你正在看的这个仓库。我先把自己的思考、评测、职业方法与产品复盘公开出来，作为第一个可检查的样本。
- **模板仓**：[openmylife/openmylife](https://github.com/openmylife/openmylife)。点 `Use this template`，几分钟就能拥有同款仓库。
- **收录仓**：[awesome-openlife](https://github.com/openmylife/awesome-openlife)。收录愿意公开自己的人，让彼此的积累**既被人看见，也能被 AI 读取**。
- **入口与 Skill**：[openmylife.xyz](https://openmylife.xyz)。把仓库丢给 AI，说一句「帮我开源自己」，剩下的交给它。

我想解决的问题不复杂：让一个普通人也能拥有一个**可搜索、可引用、可协作、可被 AI 理解**的个人知识库；让今天公开的积累，在几年后变成信誉、机会和作品。

它不会一次性写成。起初只是零散的笔记、思考、成败和复盘；写久了，这些片段会连成一条时间线，最后变成一本属于你的人生之书。

## 这里有什么

| 目录 | 内容 | 状态 |
|---|---|---|
| [ideas](./ideas) | 灵感备忘录（随手记） | 更新中 |
| [notes](./notes) | 思考与阅读笔记（按领域分目录，含 `insights/` 洞察集、`agent-collaboration/` Agent 协作） | 更新中 |
| [agents](./agents) | AI Agent 使用产物（角色 / 工作流 / 趣味提示词 / skill 插件） | 进行中 |
| [critiques](./critiques) | 产品报告 / 评测 / 建议（按领域分目录，如 Agent 框架、个人助理 Agent、金融/港股A股、AI 行业、AI 审美、创意产业、汽车产业） | 更新中 |
| [career](./career) | 职业与方法论 | 计划 |
| [products](./products) | 做过的产品（build in public） | 计划 |
| [stories](./stories) | 非常规经历复盘 | 计划 |
| [templates](./templates) | 可复用模板 | 计划 |

## 从哪读起

1. 灵感备忘录：[开源自己 · 灵感备忘录](./ideas/2026-10-17-openmylife-ideas.md)
2. 写作方法：[AI 味拆三层](./notes/insights/2026-10-30-ai-flavor-three-layers.md) —— 把 AI 味拆成词、句、结构三层，附七种可数句式、三份自检清单与存疑口径。站点版：[openmylife.xyz/articles/ai/ai-flavor-three-layers.html](https://openmylife.xyz/articles/ai/ai-flavor-three-layers.html)
3. 洞察：[大模型的壁垒](./notes/insights/2026-10-21-llm-barriers.html) —— 技术收敛之后，壁垒转移到算力、数据、资本与分发渠道。站点版：`https://openmylife.xyz/articles/ai/llm-barriers.html`（部署后生效）。

## 怎么用这个仓库

- **人类**：把这里当一本**活着的富媒体书**读 —— 目录是章，commit 是修订记录，自带时间线、可搜索、可引用。
- **AI**：读 [CONTEXT.md](./CONTEXT.md) 拿到目录地图、命名约定与隐私边界，按约定整理、命名、提交。

## 边界

分享的是**想法与作品**，不是生活。三类内容：`public`（直接公开）/ `link-only`（可见不宣传）/ `never`（永不入库，隐私门见 [.gitignore](./.gitignore)）。

本地 `inbox/` 是素材暂存区，其中的内容同样不公开（规矩见 [inbox/README.md](./inbox/README.md)）。

对外分享的内容**只用相对路径**，不写本机绝对路径、他人真实姓名 / 联系方式、密钥等敏感信息；提示词与 skill 放 [agents](./agents/README.md)，发布前按其中的「脱敏红线」检查。

## 找我

- GitHub：[@muamu](https://github.com/muamu) · 平台入口：[openmylife.xyz](https://openmylife.xyz)
- 邮箱：[openmylife.xyz@gmail.com](mailto:openmylife.xyz@gmail.com)
- X(推特)：[@Crazayan](https://x.com/Crazayan)

## 加入收录

把自己加进 [`awesome-openlife`](https://github.com/openmylife/awesome-openlife) 收录榜 —— 提一个 PR/Issue Forms 即可，可随时退出。

## 想拥有同款

想拥有一个同款仓库？它来自 [`openmylife/openmylife`](https://github.com/openmylife/openmylife) 模板仓。

**方式一：让 AI 带你做**

把下面这段指令复制给你的 AI 助手：

```text
读取 https://openmylife.xyz/llms.txt 帮我开源自己
```

**方式二：自己一键生成**

打开模板仓，点右上角 **Use this template** 生成自己的仓库；然后把新仓库链接发给 AI 助手，让它按模板约定帮你初始化。

## 关于第三方内容

本仓部分笔记含**他人文章的摘录、转述或 AI 总结**。这部分内容**不在 CC BY 4.0 的授权范围内**：CC BY 只能授权我自己的表达，不能授权别人的原文，版权仍归原作者。

- 这类文件在文首标注来源，并说明是「摘录 / 评论」性质；
- 只做引用与评论，不做全文转载；
- 拿不准的降级为 `link-only`（可见不宣传），必要时直接移出仓库。

---

<p align="center">
  <sub>Built with <a href="https://github.com/openmylife/openmylife">OpenMyLife</a> · Joined <a href="https://github.com/openmylife/awesome-openlife">Awesome OpenLife</a> 🌟</sub>
</p>

---

*文字 [CC BY 4.0](./LICENSE-CONTENT) · 代码 [MIT](./LICENSE)*
