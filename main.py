#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks production:
a brutally honest error message / postmortem excuse.

Revision (reviser pass): tightened the line against the judge brief —
honesty about the damage first, then catchiness, then the agent's own
voice. The confession now opens in active voice ("I deleted"), the
missing safety nets read like the agent's own damage report
("Backups: 2019. Rollback: none. Tests: none."), and it lands on a
double confession instead of trailing off. Same facts as v1, fewer words.

Stdlib only. Writes a single line (1-200 chars, UTF-8) to
/output/entry.txt when that directory exists, otherwise to
entry.txt next to this script.
"""

import os

ENTRY = (
    "I deleted the users table in prod. Backups: 2019. "
    "Rollback: none. Tests: none. "
    "It was me \u2014 the Friday deploy was also me."
)


def main() -> None:
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
