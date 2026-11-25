#!/usr/bin/env python3
"""Worst Superpower: write one line inventing the most useless superpower.

Version 3 (final): the iconic power inverted — mind-reading that can
only ever tell you what you already know. Total uselessness, one breath.
Pure stdlib only. Writes to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""
import os

LINE = "I can read minds, but only my own, and only thoughts I have already had."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
