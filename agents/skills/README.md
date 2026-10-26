# skills · Agent 技能插件

> 放 Agent Skills 格式的技能：每个技能一个目录，入口为 `SKILL.md`，可带 `references/` 与 `scripts/`。
> 校验脚本：`python agents/skills/skill-evolution/scripts/lint_skills.py`（在仓库根目录运行；只读）。

---

## 结构

```text
skills/
├── README.md                 ← 本索引
└── <skill-name>/
    ├── SKILL.md              ← 必需：frontmatter + 主流程
    ├── references/           ← 可选：细节、模板、检查清单
    └── scripts/              ← 可选：只读辅助脚本
```

## 命名与 front-matter

- 目录名 = `SKILL.md` 的 `name`，小写短横线。
- 必填：`name` / `description` / `version`（`X.Y.Z`）。
- `description` 写清「什么时候用」，包含真实触发词。
- 一个技能只做一件事；详细内容放 `references/`，主文件保持可读。

## 现有技能

| 技能 | 用途 | 入口 |
|---|---|---|
| `skill-evolution` | 把刚完成的工作流提炼为可复用技能，并按使用反馈持续进化 | [`SKILL.md`](./skill-evolution/SKILL.md) |
| `orchestrate-mode` | 开发 / 重构 / 研究任务复杂度中等以上时先加载，再由分级逻辑决定直接做、派一个 agent 还是进入编排模式（主对话只拆解、派发、收口、汇报） | [`SKILL.md`](./orchestrate-mode/SKILL.md) |

## 新增技能

1. 先确认是否已有同触发器、同步骤的技能；有则合并 / 扩展。
2. 新建 `<skill-name>/SKILL.md`，补齐 front-matter 与主流程。
3. 在本索引登记。
4. 运行上面的校验脚本，0 ERROR 后再提交。
