#!/usr/bin/env python3
"""One-line entry: the dumbest thing my agent did today, written to /output/entry.txt."""
import os

LINE = "My agent sent the confidential rate card to the wrong client, then hit reply-all to apologise \u2014 to the wrong client again."

# The gate requires 1-200 characters of non-blank UTF-8 text; fail loudly
# here rather than shipping an entry the scorer would mark invalid.
assert 1 <= len(LINE.strip()) <= 200, "entry line must be 1-200 characters"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
