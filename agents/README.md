# agents · AI Agent 使用产物

> 放「拿来就能用」的 Agent 产物：角色设定、工作流提示词、好玩有趣的提示词、skill 技能插件。
> 不是 Agent 本身，也不是对 Agent 产品的评测（评测放 [`critiques/`](../critiques/README.md)）。

---

## 目录

| 目录 | 放什么 | 命名 |
|---|---|---|
| [`roles/`](./roles/) | 角色设定 / 人格 / 系统提示词 | `<slug>.md` |
| [`workflows/`](./workflows/) | 可复用的工作流提示词 / SOP | `<slug>.md` |
| [`fun/`](./fun/) | 好玩、实验性、脑洞提示词 | `<slug>.md` |
| [`skills/`](./skills/) | Agent Skills 格式的技能插件 | `<skill-name>/SKILL.md` |

---

## 文件约定

- 提示词类 front-matter：

  ```yaml
  ---
  date: 2026-10-22
  kind: role          # role | workflow | fun
  tags: [Agent, 角色设定]
  visibility: public  # public | link-only
  ---
  ```

- skill 类 front-matter：`name` / `description` / `version`，结构见 [`skills/README.md`](./skills/README.md)。
- **用稳定 slug，不带日期前缀**：这些是可复用产物，不是按日归档的笔记；日期写 front-matter。
- 每个文件顶部先用 1–3 句话说清：**它是什么 / 适合谁 / 怎么用**。
- 标注适用模型 / 版本 / 环境；不确定的地方写「待验证」。
- 提示词里用 `<占位符>` 标出需要替换的部分，不要写死个人配置。

---

## 脱敏红线（发布前必过）

- **路径**：只用相对路径或公开 URL；不写本机绝对路径（盘符路径、`file:///`、用户目录）。
- **身份**：不写朋友 / 他人真实姓名、昵称、联系方式；用「朋友 A」「前同事」等化名，除非本人明确同意公开。
- **敏感信息**：不写密钥 / Token、聊天记录截图、未公开交易数据、公司内部信息。
- **事实**：数字级事实（star 数、价格、性能）标注口径与日期，复核后再发布。
- **拿不准**：降级为 `link-only`，或先不发布。

---

## 怎么用

- **角色 / 工作流 / 趣味提示词**：复制对应 `.md` 里的提示词，按你的场景替换 `<占位符>`。
- **skill**：把 `skills/<name>/` 整个目录放进你的 Agent 技能目录，或按该技能的 `SKILL.md` 手动安装。

---

## 现有内容

- [`skill-evolution`](./skills/skill-evolution/SKILL.md) —— 把刚完成的工作流提炼为可复用技能，并按使用反馈持续进化。

---

## 与其它目录的分工

| 目录 | 放什么 |
|---|---|
| `notes/` | 我的思考、阅读与方法论 |
| `critiques/` | 对他人产品的报告 / 评测 / 建议 |
| `agents/` | **可直接复用的 Agent 产物**（提示词、角色、工作流、skill） |
| `products/` | 我自己做的产品（build in public） |

---

*文字 CC BY 4.0 · 代码与脚本 MIT（见仓库根目录协议文件）*
