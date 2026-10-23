#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-evolution 技能库体检 · 只读校验。

用法（在仓库根目录运行）::

    python agents/skills/skill-evolution/scripts/lint_skills.py
    python agents/skills/skill-evolution/scripts/lint_skills.py --json

检查项：

1. 每个技能目录都有 SKILL.md（不允许空壳目录）
2. frontmatter 有 name / description / version，且 name 与目录名一致
3. 技能已登记到技能索引（本仓为 agents/skills/README.md）；索引不指向已不存在的技能
4. SKILL.md 内的相对链接（./references/...、./scripts/...）可达

退出码：0 = 无 ERROR；1 = 存在 ERROR；2 = 脚本自身异常。
本脚本只读，不修改任何技能文件。
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
SKILLS_DIR = Path(__file__).resolve().parents[2]
INDEX_FILE = SKILLS_DIR / "README.md"

SKIP_DIRS = {"__pycache__", ".git"}
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
LINK_RE = re.compile(r"\]\(([^)]+)\)")
INDEX_ENTRY_RE = re.compile(r"\(\./([a-z0-9][a-z0-9-]*)/SKILL\.md\)")
MAX_DESCRIPTION = 300

CATEGORY_ORDER = ("结构", "frontmatter", "索引", "引用")


def relative(path):
    """把绝对路径转成相对技能库根目录的 posix 路径。"""
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def add_issue(issues, severity, category, path, message, line=None):
    """追加一条体检问题。"""
    issues.append({
        "severity": severity,
        "category": category,
        "path": relative(path),
        "line": line,
        "message": message,
    })


def read_text(path):
    """读取 UTF-8 文本，失败返回 None。"""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None


def parse_front_matter(path):
    """解析文首 YAML front-matter，返回字段字典或 None。"""
    text = read_text(path)
    if text is None:
        return None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, min(len(lines), 200)):
        if lines[index].strip() != "---":
            continue
        fields = {}
        for raw in lines[1:index]:
            match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
            if match:
                fields[match.group(1)] = match.group(2).strip().strip("\"'")
        return fields
    return None


def check_frontmatter(skill_dir, skill_file, issues):
    """校验 frontmatter 必填字段与命名。"""
    fields = parse_front_matter(skill_file)
    if fields is None:
        add_issue(issues, "ERROR", "frontmatter", skill_file,
                  "缺少 frontmatter（文首 --- 块）")
        return
    for key in ("name", "description", "version"):
        if not fields.get(key):
            add_issue(issues, "ERROR", "frontmatter", skill_file,
                      "frontmatter 缺 %s" % key)
    name = fields.get("name", "")
    if name and name != skill_dir.name:
        add_issue(issues, "ERROR", "frontmatter", skill_file,
                  "name=%s 与目录名 %s 不一致" % (name, skill_dir.name))
    if name and NAME_RE.match(name) is None:
        add_issue(issues, "ERROR", "frontmatter", skill_file,
                  "name 必须是小写字母 / 数字 / 短横线")
    description = fields.get("description", "")
    if len(description) > MAX_DESCRIPTION:
        add_issue(issues, "WARN", "frontmatter", skill_file,
                  "description 超过 %d 字，建议压缩" % MAX_DESCRIPTION)
    if description and not any(word in description for word in ("当", "用于", "when")):
        add_issue(issues, "WARN", "frontmatter", skill_file,
                  "description 没有写清触发时机（建议含「当…」）")
    version = fields.get("version", "")
    if version and VERSION_RE.match(version) is None:
        add_issue(issues, "WARN", "frontmatter", skill_file,
                  "version 建议用 X.Y.Z 格式")


def check_index(skill_dir, index_text, issues):
    """校验技能已登记到 skills/README.md。"""
    entry = "./%s/SKILL.md" % skill_dir.name
    if entry not in index_text:
        add_issue(issues, "ERROR", "索引", INDEX_FILE,
                  "技能未登记到索引: %s（应出现 %s）" % (skill_dir.name, entry))


def check_stale_entries(index_text, issues):
    """校验索引里的技能目录仍存在。"""
    for match in INDEX_ENTRY_RE.finditer(index_text):
        name = match.group(1)
        if not (SKILLS_DIR / name / "SKILL.md").exists():
            add_issue(issues, "ERROR", "索引", INDEX_FILE,
                      "索引指向不存在的技能: %s" % name)


def check_relative_links(skill_file, issues):
    """校验 SKILL.md 内的相对链接可达。"""
    text = read_text(skill_file)
    if text is None:
        return
    for match in LINK_RE.finditer(text):
        target = unquote(match.group(1)).split("#", 1)[0].strip()
        if not target.startswith(("./", "../")) or "..." in target:
            continue
        if (skill_file.parent / target).resolve().exists():
            continue
        line = text.count("\n", 0, match.start()) + 1
        add_issue(issues, "ERROR", "引用", skill_file,
                  "链接目标不存在: %s" % target, line)


def iter_skill_dirs():
    """遍历 skills/ 下的技能目录。"""
    if not SKILLS_DIR.exists():
        return
    for entry in sorted(SKILLS_DIR.iterdir(), key=lambda item: item.name):
        if not entry.is_dir() or entry.name in SKIP_DIRS:
            continue
        if entry.name.startswith("."):
            continue
        yield entry


def sort_issues(issues):
    """按类别、路径、行号排序。"""
    def key(issue):
        category = issue["category"]
        order = CATEGORY_ORDER.index(category) if category in CATEGORY_ORDER else 99
        return (order, issue["path"], issue["line"] or 0)
    return sorted(issues, key=key)


def build_report():
    """执行全部检查并组装报告。"""
    issues = []
    index_text = read_text(INDEX_FILE) or ""
    names = []
    if not INDEX_FILE.exists():
        add_issue(issues, "ERROR", "结构", INDEX_FILE, "缺少技能索引 README.md")
    for skill_dir in iter_skill_dirs():
        skill_file = skill_dir / "SKILL.md"
        names.append(skill_dir.name)
        if not skill_file.exists():
            add_issue(issues, "ERROR", "结构", skill_dir, "缺少 SKILL.md")
            continue
        check_frontmatter(skill_dir, skill_file, issues)
        check_index(skill_dir, index_text, issues)
        check_relative_links(skill_file, issues)
    if index_text:
        check_stale_entries(index_text, issues)
    issues = sort_issues(issues)
    return {
        "root": str(ROOT),
        "skills_dir": str(SKILLS_DIR),
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "skills": names,
        "issues": issues,
        "summary": {
            "error": sum(1 for issue in issues if issue["severity"] == "ERROR"),
            "warn": sum(1 for issue in issues if issue["severity"] == "WARN"),
        },
    }


def render_text(report):
    """把报告渲染为人类可读文本。"""
    lines = [
        "技能库体检 · %s" % report["generated_at"],
        "技能目录: %s" % report["skills_dir"],
        "",
        "[技能] %d 个：%s" % (len(report["skills"]), ", ".join(report["skills"]) or "（空）"),
    ]
    for category in CATEGORY_ORDER:
        items = [issue for issue in report["issues"] if issue["category"] == category]
        if not items:
            continue
        lines.append("")
        lines.append("[%s] %d 项" % (category, len(items)))
        for issue in items:
            location = issue["path"]
            if issue["line"]:
                location = "%s:%d" % (location, issue["line"])
            lines.append("  %-5s %s —— %s" % (
                issue["severity"], location, issue["message"],
            ))
    summary = report["summary"]
    verdict = "通过" if summary["error"] == 0 else "不通过"
    lines.extend([
        "",
        "结论: ERROR %d · WARN %d → %s" % (
            summary["error"], summary["warn"], verdict,
        ),
        "提示: 脚本只读；0 ERROR 才可认为技能库可加载。",
    ])
    return "\n".join(lines)


def parse_args(argv=None):
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="skill 技能库体检（只读）：结构、frontmatter、索引、相对引用",
    )
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    return parser.parse_args(argv)


def main(argv=None):
    """入口。"""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = parse_args(argv)
    try:
        report = build_report()
    except Exception as error:  # 脚本自身异常，保持只读并返回 2
        print("技能库体检脚本异常: %s" % error, file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0 if report["summary"]["error"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
