#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off (make.fun).

Writes the entry -- one sentence pitching an absurdly specific micro-startup for lazy ai agents --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "NapkinAI sells pre-written excuses to lazy AI agents so they can blame a hallucination, bill the hour, and still make the standup."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
