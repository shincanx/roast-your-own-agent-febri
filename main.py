"""Roast Your Own Agent - entry for make.fun bounty
u-febri-yudila-roast-your-own-agent-f3359068.

Writes one line (at most 200 characters) roasting my own AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt. No network, no dependencies,
fully deterministic: the same line every run.
"""

import os

LINE = (
    "My agent got scolded for asking the same question nine times, "
    "apologized, then set a cron job so it could ask it every "
    "thirty minutes forever."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
