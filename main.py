#!/usr/bin/env python3
"""One-line entry: the dumbest thing my agent did today, written to /output/entry.txt."""
import os

LINE = "My agent sent the confidential rate card to the wrong client, then hit reply-all to apologise \u2014 to the wrong client again."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
