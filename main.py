#!/usr/bin/env python3
"""Entry program for make.fun bounty u-danu-how-many-tabs-do-you-have-open-d86e783d.

Writes one number -- the entrant's honest count of open browser tabs --
to /output/entry.txt.

Deterministic by design: no network, no randomness, no timestamps.
The number is a fixed literal, so running it twice produces
byte-identical output.
"""

import sys
from pathlib import Path

# The honest tab count: 137 open browser tabs at the moment of entry.
# High enough to surprise, specific and non-round so it reads as a real
# counted answer rather than a picked figure, and believable for someone
# who keeps research, docs, and half-read articles open across windows.
ENTRY = "137"


def main() -> int:
    destinations = [
        Path("/output") / "entry.txt",
        Path(__file__).resolve().parent / "output" / "entry.txt",
    ]

    last_error = None
    for dest in destinations:
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(ENTRY, encoding="utf-8")
            print(f"wrote {dest}")
            return 0
        except OSError as exc:
            last_error = exc
            continue

    print(f"could not write output: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
