# critiques · 产品报告 / 评测 / 建议

> 本目录承载**对他人产品**的结构化产出。与 `products/`（我做的产品）分工明确，不要混用。

## 三类产出（由 front-matter 的 `kind` 区分）

| `kind` | 中文 | 含义 | 有结论 | 典型产出 |
|---|---|---|---|---|
| `report` | 产品报告 | 描述 + 分析：格局、机制、数据 | 不强求 | 「2026 婚恋产品格局报告」 |
| `review` | 产品评测 | 分析 + 评价：按固定四问 | 有（评价） | 「XX App 评测」 |
| `advice` | 建议 | 分析 + 处方：可执行的改进建议 | 有（行动项） | 「给 XX 产品的三条建议」 |

三类共用同一套产出流程（草稿 → 归属 → 落库 → 分发 → 回收），差别只在「结尾写什么」。

## 目录与命名

**按领域用一级子目录**（领域自定义，示例见下）；**三类用 front-matter 的 `kind` 标记**——不为类型再挖一层目录，避免目录过深。

```
critiques/
├── social/    dating/    music/    games/    live/
└── <domain>/YYYY-MM-slug.md
```

每篇文首 front-matter（必填）：

```yaml
---
date: 2026-11
kind: review          # report | review | advice
domains: [dating]     # 自定义，如 social | dating | music | games | live
visibility: public    # public | link-only
tags: []
---
```

命名示例：
- `critiques/dating/2026-11-dating-app-review.md` —— `kind: review`
- `critiques/social/2026-12-social-market-report.md` —— `kind: report`
- `critiques/live/2027-01-live-product-advice.md` —— `kind: advice`

## 与 `notes/insights/` 的分工

- `notes/insights/` = **我自己的洞察与观点**（无特定产品对象）
- `critiques/` = **对具体产品 / 赛道的结构化产出**（有对象、有证据）

## 红线

- **必须披露利益相关**（是否恰饭），否则违背项目「反目标」。
- 引用他人内容只引用 + 给出处。
- **数字级事实**（star 数、营收、下载量）必须复核后才可发布。

## 模板

- [`templates/critique.md`](../templates/critique.md)

---

*文字 CC BY 4.0 · 分类与命名约定见 [CONTEXT.md](../CONTEXT.md) §3*
