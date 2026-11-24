#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry.

Writes one short rant about an everyday annoyance to entry.txt.
Stdlib only. No network, no input.
"""

import os
import sys

LINE = "She wrote 'per my last email' at 9:03, as if the first email had been carved into stone tablets and I had simply chosen illiteracy. I read it. I read it twice. It still says nothing, only louder."

MIN_CHARS = 1
MAX_CHARS = 400


def resolve_output_dir():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    line = LINE.strip()
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        print(f"entry must be {MIN_CHARS}..{MAX_CHARS} chars, got {len(line)}",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
