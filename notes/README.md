# notes · 思考与阅读笔记

> 放**带日期的个人思考、阅读与方法论**。按领域分子目录，避免根目录越堆越平。

## 命名

`notes/<domain>/YYYY-MM-DD-slug.md`

- `<domain>` 用英文小写短横线，按内容主题划分；**有内容再建目录，不预建空目录**。
- 富媒体单页笔记可用同名 `.html`（自包含、无外部依赖），如 `notes/insights/2026-10-21-llm-barriers.html`；站点发布版放 `web/articles/<题材>/`。
- 已有领域：
  - `insights/` —— 我自己的洞察与观点（无特定产品对象）
  - `agent-collaboration/` —— Agent 协作、指令设计、多模型工作流
- 新增领域时，在本文件补一行说明。

## front-matter

```yaml
---
date: 2026-10-21
tags: [指令设计, Agent协作]
visibility: public
---
```

## 与 `critiques/` 的分工

- `notes/` = 我自己的思考、阅读与方法论
- `critiques/` = 对具体产品 / 赛道的结构化产出（有对象、有证据）

---

*文字 CC BY 4.0 · 分类与命名约定见 [CONTEXT.md](../CONTEXT.md) §3*
