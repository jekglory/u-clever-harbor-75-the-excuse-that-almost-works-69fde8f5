#!/usr/bin/env python3
"""The Excuse That Almost Works -- make.fun entry.

Writes the one line a gamer texts the boss to get out of work during
GTA 6 launch week to /output/entry.txt: one line of plain text, at most
20 words, that reads like something a real person sent in a hurry.
The excuse is a burst boiler and a flooded kitchen: specific, mundane,
and hard to argue with, with no mention of the game at all.
Pure standard library; the output is identical on every run.
"""

import os

LINE = "sorry boss, boiler burst this morning, kitchen's ankle-deep, plumber's on his way, need today to sort it"


def main():
    if len(LINE.split()) > 20:
        raise ValueError("entry line is over 20 words")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
