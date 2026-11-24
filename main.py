#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. Deterministic: the same bytes on
every run. Standard library only.
"""

from pathlib import Path

ENTRY = "It worked in my head, which is the only environment I actually tested."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard the gate before writing: one line, 1-200 characters, not blank.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and ENTRY.strip() == ENTRY
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
