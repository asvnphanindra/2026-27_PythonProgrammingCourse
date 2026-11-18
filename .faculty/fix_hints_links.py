"""Fix leftover hints.md# links (HTML lab tables + observation back-links)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

UNITS = {
    "1": "unit1-python-fundamentals.md",
    "2": "unit2-control-structures-and-strings.md",
    "3": "unit3-lists-tuples-sets-and-functions.md",
    "4": "unit4-dictionaries-and-exception-handling.md",
    "5": "unit5-object-oriented-programming.md",
}


def file_for(anchor: str) -> str:
    m = re.match(r"unit-(\d)", anchor)
    if not m:
        raise ValueError(anchor)
    return UNITS[m.group(1)]


def main() -> None:
    # HTML hrefs in lab-task pages
    lab2 = ROOT / "docs" / "lab-tasks" / "unit2-control-structures-and-strings.md"
    text = lab2.read_text(encoding="utf-8")
    new, n = re.subn(
        r'href="\.\./hints\.md#(unit-[^"]+)"',
        lambda m: f'href="../hints/{file_for(m.group(1))}#{m.group(1)}"',
        text,
    )
    lab2.write_text(new, encoding="utf-8")
    print(f"Updated {n} HTML hint hrefs in {lab2.relative_to(ROOT)}")

    # Observation back-links
    obs_dir = ROOT / ".faculty" / "observations"
    total = 0
    for path in obs_dir.glob("*.md"):
        if path.name == "INDEX.md":
            continue
        t = path.read_text(encoding="utf-8")

        def repl(m: re.Match[str]) -> str:
            nonlocal total
            anchor = m.group(1)
            total += 1
            return f"(../../docs/hints/{file_for(anchor)}#{anchor})"

        nt = re.sub(r"\(\.\./\.\./docs/hints\.md#(unit-[^)]+)\)", repl, t)
        # Also point back to the unit lab page when still on generic README
        nt2 = re.sub(
            r"\[Back to lab tasks\]\(\.\./\.\./docs/lab-tasks/README\.md\)",
            lambda _m, p=path: _lab_back_for_obs(p),
            nt,
        )
        if nt2 != t:
            path.write_text(nt2, encoding="utf-8")
            print(f"Updated {path.relative_to(ROOT)}")
    print(f"Retargeted {total} observation hint links")


def _lab_back_for_obs(path: Path) -> str:
    name = path.name
    if name.startswith("u1"):
        lab = "unit1-python-fundamentals.md"
    elif name.startswith("u2"):
        lab = "unit2-control-structures-and-strings.md"
    elif name.startswith("u3"):
        lab = "unit3-lists-tuples-sets-and-functions.md"
    elif name.startswith("u4"):
        lab = "unit4-dictionaries-and-exception-handling.md"
    elif name.startswith("u5"):
        lab = "unit5-object-oriented-programming.md"
    else:
        lab = "README.md"
    return f"[Back to lab tasks](../../docs/lab-tasks/{lab})"


if __name__ == "__main__":
    main()
