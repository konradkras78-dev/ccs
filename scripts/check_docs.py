"""Check local Markdown targets, conflict markers, whitespace and final newlines."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors, count = [], 0
for file in sorted(ROOT.rglob("*.md")):
    if ".git" in file.relative_to(ROOT).parts:
        continue
    text = file.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        errors.append(f"{file.relative_to(ROOT)}: missing final newline")
    for line, value in enumerate(text.splitlines(), 1):
        if value.rstrip() != value or value.startswith(("<<<<<<< ", ">>>>>>> ")):
            errors.append(f"{file.relative_to(ROOT)}:{line}: whitespace/conflict marker")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        url = urlsplit(target)
        if url.scheme or target.startswith("#"):
            continue
        path = (file.parent / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append(f"{file.relative_to(ROOT)}: missing/outside target {target}")
        count += 1
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: {count} local Markdown links; document whitespace/newlines checked")
