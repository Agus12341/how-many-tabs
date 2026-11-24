"""Entry for make.fun's 'How Many Tabs Do You Have Open?' bounty.

Writes one number, digits only - my honest count of open browser tabs -
to /output/entry.txt with no trailing newline.
"""

import os

TEXT = "42"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: the file holds exactly TEXT - digits only, no newline.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), f"wrote {written!r}, expected {TEXT!r}"
    assert TEXT.isdigit(), "entry must be digits only"
    assert 1 <= len(TEXT) <= 5, "gate allows 1 to 5 characters"


if __name__ == "__main__":
    main()
