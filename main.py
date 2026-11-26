"""Write the robot band name entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a fixed string: one funny name for a band made of robots
plus a few words on its hit song, all under 200 characters.
No network, no file reads, no secrets -- the program's only job is to
deliver the entry byte-identically.
"""

import os

ENTRY = "The Roombas — hit single \"Suck It Up\", sweeping the charts one floor at a time"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
