---
date: 2026-10-27
kind: report
domains: [ai-industry]
visibility: public
tags:
  - 模型榜单
  - 编码能力
  - SWE-bench
  - Terminal-Bench
  - 口径对照
---

# 前沿编码模型榜与代际对照

> 完整报告见 [index.html](./index.html)。五十六个模型、八个 Opus 版本、四套互不相通的榜单口径，同一款模型在不同榜上可以差 30 分。

- **对象**：2025-05 → 2026-10 公开可查的前沿编码模型与四个基准（SWE-bench Verified / SWE-bench Pro / Terminal-Bench 2.1 / Terminal-Bench 4.0）
- **窗口**：数据截至 2026-10-29；Verified 于 2026-09-01 停跑。初版 2026-10-27（51 个模型），10-29 补录 Gemini 4 Carbon、Kimi K3.1 Pro、Muse Wonder / Full、Claude Haiku 5.5 共 5 个
- **核心判断**：口径先于排名——官方集第一 61.5（Muse Spark 1.1）与厂商自报聚合榜第一 89.9（Opus 5.5）之间没有换算关系；开源已经在 Terminal-Bench 4.0 上登顶（Kimi K3.1 Pro 的 AA 复跑 67.2），但在 SWE-bench Pro 上仍落后一个代际；基准在轮换，表里大量「—」是模型没赶上那一代基准，而不是没查
- **方法**：按公开厂商公告、独立复跑（Vals / Artificial Analysis）、基准方官方榜与第三方自建 harness 四类来源分别标注，逐行写明出处口径；不采信无对应关系的第三方数字
- **已知冲突**：TB 4.0 前三名（Kimi K3.1 Pro / Gemini 4 Carbon / Opus 5.5）各有自报与复跑两套数，3 分差距在 harness 摆幅内，不足以分胜负，详见报告 §06
- **版本**：自包含单页 HTML（表格标签页 + 同系列悬停联动 + 阶梯 SVG）；文中数值按原稿保留
- **口径提示**：文中分数为百分比，保留一位小数；`—` 表示未公布、未参与或已出评测窗口，不代表 0 分。所有分数均来自第三方榜单整理，**未逐条回到一手来源复核**，引用前请以厂商公告与榜单原始页面为准
- **状态**：public（数字待复核）
- **利益相关**：无商业合作；基于公开信息整理与评论，不构成投资建议
