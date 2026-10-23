# CONTEXT · 给 AI 的上下文

> **本文件面向 AI Agent，不面向人类阅读。** 人类读者请看 [README.md](./README.md)。
> 一句话：这是「尚盐（muamu）」的个人开源仓库 —— 用 git 版本化 TA 的思考、经验与作品。
> 人类向左（README）、AI 向右（本文件），是「开源自己」的核心结构。

---

## 1. 这个仓库是什么

把个人的想法、经验、作品与经历**公开、版本化、可被搜索、可被引用**。
同一份精力，两端产出：**GitHub 沉淀 + 自媒体曝光**。公开过程本身就是产品。

## 2. 我是谁

- 账号：`muamu`（GitHub 个人账号）—— 组织 `openmylife` 只放官方仓库，个人资产留在本人账号下
- 一句话画像：（待填）
- 我在做的事 / 关注的事：（待填）
- 起算时间：`2026-10`

## 3. 目录地图

| 目录 | 放什么 | 命名 | front-matter |
|---|---|---|---|
| `notes/` | 思考与阅读笔记（按领域分目录，含 `insights/` 洞察集；富媒体可用自包含 HTML） | `<domain>/YYYY-MM-DD-slug.md`（富媒体可用同名 `.html`） | `date` / `tags` / `visibility` |
| `agents/` | AI Agent 使用产物：角色 / 工作流 / 趣味提示词 / skill | `roles/<slug>.md`、`workflows/<slug>.md`、`fun/<slug>.md`；`skills/<name>/SKILL.md` | `date` / `kind` / `tags` / `visibility`；skill 用 `name` / `description` / `version` |
| `critiques/` | 对他人产品的报告 / 评测 / 建议 | `<domain>/YYYY-MM-slug.md`；HTML 报告用 `<domain>/<YYYY-MM-slug>/index.html` | +`kind` / `domains` |
| `career/` | 职业与方法论 | `YYYY-MM-slug.md` | `date` / `tags` / `visibility` |
| `products/` | 我做过的产品（build in public） | `<product>/` + 顶层 `README.md` | — |
| `stories/` | 非常规经历复盘 | `YYYY-MM-slug.md` | `date` / `tags` / `visibility` |
| `ideas/` | 灵感备忘录（随手记） | `YYYY-MM-DD-slug.md` | `date` / `tags` / `visibility` |
| `inbox/` | **本地收件箱**：未分类草稿 / 原始素材 —— **内容不入库**，只提交本目录的 `README.md` | 随手丢，不定期清 | — |
| `templates/` | 可复用空模板 | 固定 | — |

## 4. 术语表

- **开源自己**：用开源软件的方式运营个人 —— 版本化 / 公开 / 允许 fork / 接受 issue / 持续 commit。
- **commit**：存一次档；**仓库**：你的个人档案本；**fork**：复制一份改成自己的；**PR**：把你自己加进名单。
- **visibility**：`public`（直接公开）| `link-only`（可见不宣传）。
- **两份文档**：`README.md` 给人类看（建立品牌）；本文件 `CONTEXT.md` 给 AI 读（数字分身）。

## 5. 隐私边界（AI 必须遵守）

- **永不入库**：他人隐私、证件、住址、财务细节、在谈 offer、交易细节、买家身份 → 写入 `.gitignore`。
- **公开公司财报分析**放 `critiques/finance/`，只写公开信息；个人财务 / 交易细节仍为 `never`，`.gitignore` 只为前者开了窄例外。
- **`inbox/` 中的原始素材默认不公开**（见 [inbox/README.md](./inbox/README.md)）；整理后才按 §3 命名约定移入对应目录。
- 拿不准 → **降级为 `link-only`**，并向本人确认。
- **对外分享脱敏**：内容只用相对路径；不写本机绝对路径（盘符、`file:///`、用户目录）、他人真实姓名 / 昵称 / 联系方式、聊天记录截图、密钥 / Token、未公开交易数据、公司内部信息。提及朋友 / 他人用「朋友 A」「前同事」等化名，除非本人明确同意公开。
- 评测**必须披露利益相关**；引用他人内容只引用 + 给出处。
- **数字级事实**（star 数、营收、下载量）标注「待复核」，复核后才可对外。

## 6. 写作规范

- 每篇文首必填 front-matter：`date` / `tags` / `visibility`；`critiques/` 另加 `kind` 与 `domains`；`agents/` 提示词另加 `kind`。
- **对外内容只用相对路径**；提示词 / skill 放 `agents/`，发布前按 [agents/README.md](./agents/README.md) 的「脱敏红线」检查。
- **保留原始日期**，不做二次精修；第一版允许丑，先公开再完善。
- 不编造事实；引用要给出来源。
- 第三方原文摘录与 AI 总结：文首标注来源 + 「摘录 / 评论」，不纳入 CC BY（见 [LICENSE-CONTENT](./LICENSE-CONTENT)）。

## 7. 更新节奏

- **建议每周 1 更**，宁少勿断。公开是储蓄，不是消耗。

---

## 8. 参考

- 平台入口与上手教程：[openmylife.xyz](https://openmylife.xyz)
- [llms.txt](./llms.txt) —— AI 可读入口
- 模板仓：[openmylife/openmylife](https://github.com/openmylife/openmylife)
- 收录仓：[awesome-openlife](https://github.com/openmylife/awesome-openlife)

---

> 把本文件交给你的 AI：「读 CONTEXT.md，按约定帮我整理并提交下一篇。」
