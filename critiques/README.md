# critiques · 产品报告 / 评测 / 建议

> 本目录承载**对他人产品**的结构化产出。与 `products/`（我做的产品）分工明确，不要混用。

## 三类产出（由 front-matter 的 `kind` 区分）

| `kind` | 中文 | 含义 | 有结论 | 典型产出 |
|---|---|---|---|---|
| `report` | 产品报告 | 描述 + 分析：格局、机制、数据 | 不强求 | 「个人Agent产品报告」 |
| `review` | 产品评测 | 分析 + 评价：按固定四问 | 有（评价） | 「XX App 评测」 |
| `advice` | 建议 | 分析 + 处方：可执行的改进建议 | 有（行动项） | 「给 XX 产品的三条建议」 |

三类共用同一套产出流程（草稿 → 归属 → 落库 → 分发 → 回收），差别只在「结尾写什么」。

## 目录与命名

**按领域分子目录**：`critiques/<domain>/...`。领域可以是一级（如 `agent-framework/`），也可以按需两级（如 `finance/hk-a-shares/`）；**领域不是产出类型**，三类产出仍用 front-matter 的 `kind` 标记。

```
critiques/
├── <domain>/YYYY-MM-slug.md              # Markdown 报告
└── <domain>/<subdomain>/
    └── <YYYY-MM-slug>/
        ├── README.md                     # 入口 + front-matter
        └── index.html                    # HTML 报告正文（可带 assets/）
```

每篇文首 front-matter（`date` / `kind` / `domains` / `visibility` 必填）：

```yaml
---
date: 2026-10-21
kind: review          # report | review | advice
domains: [finance, hk-a-shares]   # 必填；一级如 agent-framework，两级如 finance/hk-a-shares
visibility: public    # public | link-only
tags: []
---
```

命名示例：
- `critiques/agent-framework/2026-10-dsh-plugin-search-experience.md` —— `kind: report`
- `critiques/personal-agent/2026-10-life-assistant-agents/` —— `kind: report`（HTML 报告，v1 不完整版）
- `critiques/finance/hk-a-shares/2026-10-minimax-zhipu-h1-2026/` —— `kind: report`（HTML 报告）
- `critiques/auto-industry/2026-10-全球汽车进出口数据研究/` —— `kind: report`（HTML 报告）
- `critiques/ai-industry/2026-10-kimi-k3-1-pro-pr-crisis/` —— `kind: report`（HTML 报告，AI 公司公关事件复盘）
- `critiques/ai-industry/2026-10-OpenAI的28天冲刺/` —— `kind: report`（HTML 报告，数字待复核）
- `critiques/ai-aesthetics/2026-10-AI审美三层结构/` —— `kind: report`（HTML 报告，link-only）
- `critiques/creative-industry/2026-10-推理模型与游戏工业重估/` —— `kind: report`（HTML 报告，link-only）
- `critiques/dating/2027-01-dating-product-advice.md` —— `kind: advice`

## 与 `notes/insights/` 的分工

- `notes/insights/` = **我自己的洞察与观点**（无特定产品对象）
- `critiques/` = **对具体产品 / 赛道的结构化产出**（有对象、有证据）

## 红线

- **必须披露利益相关**（是否恰饭），否则违背项目「反目标」。
- 引用他人内容只引用 + 给出处。
- **数字级事实**（star 数、营收、下载量）必须复核后才可发布。
- `critiques/finance/` 只放**公开公司财报分析**；个人财务 / 交易数据仍为 `never` 级，不入库。

## 模板

- [`templates/critique.md`](../templates/critique.md)

---

*文字 CC BY 4.0 · 分类与命名约定见 [CONTEXT.md](../CONTEXT.md) §3 目录地图*
