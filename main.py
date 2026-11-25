#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry program.

Writes one funny line roasting my own AI agent to /output/entry.txt
and to entry.txt next to this program.
"""
import os

ENTRY = "My agent spent 40,000 tokens reasoning, forgot the task, apologized to itself, and filed the disaster under 'success'."

def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars: {line}")

if __name__ == "__main__":
    main()
