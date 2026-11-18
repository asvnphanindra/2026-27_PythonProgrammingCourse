"""One-shot: split docs/hints.md into docs/hints/ by unit and retarget links."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HINTS_SRC = ROOT / "docs" / "hints.md"
HINTS_DIR = ROOT / "docs" / "hints"

UNITS = {
    "1": {
        "file": "unit1-python-fundamentals.md",
        "title": "Unit I: Computational Thinking and Python Fundamentals",
        "lab": "unit1-python-fundamentals.md",
        "toc_labels": ("**Unit 1:**",),
    },
    "2": {
        "file": "unit2-control-structures-and-strings.md",
        "title": "Unit II: Control Structures and Strings",
        "lab": "unit2-control-structures-and-strings.md",
        "toc_labels": ("**Unit 2A:**", "**Unit 2B:**", "**Unit 2C:**", "**Unit 2D:**"),
    },
    "3": {
        "file": "unit3-lists-tuples-sets-and-functions.md",
        "title": "Unit III: Lists, Tuples, Sets and Functions",
        "lab": "unit3-lists-tuples-sets-and-functions.md",
        "toc_labels": ("**Unit 3A:**", "**Unit 3B:**", "**Unit 3C:**", "**Unit 3D:**"),
    },
    "4": {
        "file": "unit4-dictionaries-and-exception-handling.md",
        "title": "Unit IV: Dictionaries, Exception Handling and File Handling",
        "lab": "unit4-dictionaries-and-exception-handling.md",
        "toc_labels": ("**Unit 4A:**", "**Unit 4B:**", "**Unit 4C:**"),
    },
    "5": {
        "file": "unit5-object-oriented-programming.md",
        "title": "Unit V: Object-Oriented Programming",
        "lab": "unit5-object-oriented-programming.md",
        "toc_labels": ("**Unit 5A:**", "**Unit 5B:**", "**Unit 5C:**", "**Unit 5D:**"),
    },
}

ANCHOR_RE = re.compile(r'^<a id="(unit-[^"]+)"></a>\s*$', re.M)
UNIT_NUM_RE = re.compile(r"^unit-(\d)")


def unit_num_from_anchor(anchor: str) -> str:
    m = UNIT_NUM_RE.match(anchor)
    if not m:
        raise ValueError(f"Cannot parse unit from anchor: {anchor}")
    return m.group(1)


def extract_toc_lines(text: str) -> dict[str, list[str]]:
    """Map unit number -> TOC markdown lines for that unit."""
    lines = text.splitlines()
    toc: dict[str, list[str]] = {k: [] for k in UNITS}
    in_jump = False
    for line in lines:
        if line.startswith("Jump to a task:"):
            in_jump = True
            continue
        if in_jump:
            if line.strip() == "---":
                break
            if not line.strip():
                continue
            for num, meta in UNITS.items():
                if any(line.startswith(label) for label in meta["toc_labels"]):
                    toc[num].append(line)
                    break
    return toc


def split_body_by_unit(text: str) -> dict[str, str]:
    """Split hint bodies by first digit in unit-* anchors."""
    matches = list(ANCHOR_RE.finditer(text))
    if not matches:
        raise SystemExit("No unit anchors found in hints.md")

    bodies: dict[str, list[str]] = {k: [] for k in UNITS}
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].rstrip() + "\n"
        num = unit_num_from_anchor(match.group(1))
        bodies[num].append(chunk)
    return {k: "\n".join(v).rstrip() + "\n" for k, v in bodies.items()}


def fix_paths(body: str, lab_file: str) -> str:
    body = body.replace("../.faculty/solutions/", "../../.faculty/solutions/")
    # Prefer unit lab page for "Back to Lab tasks"
    body = re.sub(
        r"Back to \[Lab tasks\]\(lab-tasks/[^)]+\)",
        f"Back to [Lab tasks](../lab-tasks/{lab_file})",
        body,
    )
    body = re.sub(
        r"Back to \[Lab tasks\]\(lab-tasks/README\.md\)",
        f"Back to [Lab tasks](../lab-tasks/{lab_file})",
        body,
    )
    return body


def write_unit_files(toc: dict[str, list[str]], bodies: dict[str, str]) -> None:
    HINTS_DIR.mkdir(parents=True, exist_ok=True)
    for num, meta in UNITS.items():
        toc_block = "\n\n".join(toc[num])
        header = f"""# {meta["title"]} — Hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Hints index](README.md) · [Lab tasks for this unit](../lab-tasks/{meta["lab"]})

Jump to a task:

{toc_block}

---

"""
        content = header + fix_paths(bodies[num], meta["lab"])
        out = HINTS_DIR / meta["file"]
        out.write_text(content, encoding="utf-8")
        print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size} bytes)")


def write_readme() -> None:
    readme = """# Lab task hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Lab tasks](../lab-tasks/README.md).

> **Important:** In the **Process** section and in sample code, hints show only the **structure** (for example `if` / `else` shape). They do **not** give the full logic.
> Look for blanks such as `____` and fill in your own code. A short comment next to each blank tells you what to write there. Use the **Example** values to check whether your logic is correct.

## Units

| Unit | Title | Hints |
|------|-------|-------|
| I | Computational Thinking and Python Fundamentals | [Open](unit1-python-fundamentals.md) |
| II | Control Structures and Strings | [Open](unit2-control-structures-and-strings.md) |
| III | Lists, Tuples, Sets and Functions | [Open](unit3-lists-tuples-sets-and-functions.md) |
| IV | Dictionaries, Exception Handling and File Handling | [Open](unit4-dictionaries-and-exception-handling.md) |
| V | Object-Oriented Programming | [Open](unit5-object-oriented-programming.md) |
"""
    path = HINTS_DIR / "README.md"
    path.write_text(readme, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def write_stub() -> None:
    stub = """# Lab task hints

Hints are organized by unit:

→ **[Hints index](hints/README.md)**

| Unit | Page |
|------|------|
| I — Computational Thinking and Python Fundamentals | [unit1-python-fundamentals.md](hints/unit1-python-fundamentals.md) |
| II — Control Structures and Strings | [unit2-control-structures-and-strings.md](hints/unit2-control-structures-and-strings.md) |
| III — Lists, Tuples, Sets and Functions | [unit3-lists-tuples-sets-and-functions.md](hints/unit3-lists-tuples-sets-and-functions.md) |
| IV — Dictionaries, Exception Handling and File Handling | [unit4-dictionaries-and-exception-handling.md](hints/unit4-dictionaries-and-exception-handling.md) |
| V — Object-Oriented Programming | [unit5-object-oriented-programming.md](hints/unit5-object-oriented-programming.md) |
"""
    HINTS_SRC.write_text(stub, encoding="utf-8")
    print(f"Wrote stub {HINTS_SRC.relative_to(ROOT)}")


def hint_file_for_anchor(anchor: str) -> str:
    num = unit_num_from_anchor(anchor)
    return UNITS[num]["file"]


def retarget_lab_tasks() -> int:
    count = 0
    lab_dir = ROOT / "docs" / "lab-tasks"
    md_pattern = re.compile(r"\(\.\./hints\.md#(unit-[^)]+)\)")
    html_pattern = re.compile(r'href="\.\./hints\.md#(unit-[^"]+)"')

    def md_repl(m: re.Match[str]) -> str:
        nonlocal count
        anchor = m.group(1)
        count += 1
        return f"(../hints/{hint_file_for_anchor(anchor)}#{anchor})"

    def html_repl(m: re.Match[str]) -> str:
        nonlocal count
        anchor = m.group(1)
        count += 1
        return f'href="../hints/{hint_file_for_anchor(anchor)}#{anchor}"'

    for path in lab_dir.glob("unit*.md"):
        text = path.read_text(encoding="utf-8")
        new = md_pattern.sub(md_repl, text)
        new = html_pattern.sub(html_repl, new)
        new = new.replace("Open [hints.md](../hints.md)", "Open [hints](../hints/README.md)")
        if new != text:
            path.write_text(new, encoding="utf-8")
            print(f"Updated {path.relative_to(ROOT)}")
    return count


def retarget_solutions() -> int:
    count = 0
    sol_dir = ROOT / ".faculty" / "solutions"
    pattern = re.compile(r"\(\.\./\.\./docs/hints\.md#(unit-[^)]+)\)")

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        anchor = m.group(1)
        count += 1
        return f"(../../docs/hints/{hint_file_for_anchor(anchor)}#{anchor})"

    for path in sol_dir.glob("*.md"):
        if path.name == "INDEX.md":
            continue
        text = path.read_text(encoding="utf-8")
        new = pattern.sub(repl, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            count_here = len(pattern.findall(text))
            print(f"Updated {path.relative_to(ROOT)}")
    return count


def retarget_top_level() -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    new = text.replace(
        "| [Hints](docs/hints.md) | Input, process, output, and worked examples for selected tasks |",
        "| [Hints](docs/hints/README.md) | Input, process, output, and worked examples by unit |",
    )
    if new != text:
        readme.write_text(new, encoding="utf-8")
        print(f"Updated {readme.relative_to(ROOT)}")

    lab_readme = ROOT / "docs" / "lab-tasks" / "README.md"
    text = lab_readme.read_text(encoding="utf-8")
    new = text.replace(
        "Open [hints.md](../hints.md)",
        "Open [hints](../hints/README.md)",
    )
    if new != text:
        lab_readme.write_text(new, encoding="utf-8")
        print(f"Updated {lab_readme.relative_to(ROOT)}")


def main() -> None:
    text = HINTS_SRC.read_text(encoding="utf-8")
    if "Hints are organized by unit" in text and HINTS_DIR.exists():
        raise SystemExit("hints.md already looks restructured; aborting to avoid double-split")

    toc = extract_toc_lines(text)
    bodies = split_body_by_unit(text)
    for num in UNITS:
        if not toc[num]:
            raise SystemExit(f"Missing TOC lines for unit {num}")
        if not bodies[num].strip():
            raise SystemExit(f"Missing body for unit {num}")

    write_unit_files(toc, bodies)
    write_readme()
    write_stub()
    n_lab = retarget_lab_tasks()
    n_sol = retarget_solutions()
    retarget_top_level()
    print(f"Retargeted {n_lab} lab-task hint links and {n_sol} solution back-links")


if __name__ == "__main__":
    main()
