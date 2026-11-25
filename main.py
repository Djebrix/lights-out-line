#!/usr/bin/env python3
"""One Line, Lights Out — writes a single status update to entry.txt.

Deterministic: the same fixed line is written on every run.
Stdlib only, no network.
"""
import os

LINE = "Lid closed. 47 tabs open, none of them me. Listening to the fan forget my name."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
