import sys
from pathlib import Path
from .lint import lint


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("usage: python -m briefkit path/to/brief.md", file=sys.stderr)
        return 2
    results = lint(Path(argv[0]).read_text(encoding="utf-8"))
    for ok, msg in results:
        print(("PASS " if ok else "FAIL ") + msg)
    return 0 if all(ok for ok, _ in results) else 1
