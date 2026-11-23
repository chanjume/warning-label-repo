#!/usr/bin/env python3
"""Write one warning label for humans to /output/entry.txt.

The label imitates a real printed safety label: an allergen-style
"Contains" line naming three very human contents, and a handling
instruction as the punchline. One line, plain words, one idea.
The gate is 1-160 characters; the line below is 71.
"""
import os

LINE = "WARNING: Contains nuts, caffeine, and 47 unresolved tabs. Do not shake."


def main():
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
