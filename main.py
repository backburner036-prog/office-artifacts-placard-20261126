#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest (make.fun).

Writes a single museum placard line for an ordinary office object,
treated as an ancient artifact from a lost civilisation, to
/output/entry.txt. Deterministic, no network, no outside input.
"""

import os

# Final placard (168 characters): catalogue date, material, donor.
ENTRY = (
    "Sticky Note, 1994. Paper, adhesive, faded ink. "
    "A prayer slip left on a monitor by the Copy Clerks, "
    "asking the gods for toner. "
    "Donated by the estate of K. from Accounts."
)

MAX_CHARS = 180


def normalize(text: str) -> str:
    """Collapse any stray newline/whitespace runs to single spaces."""
    return " ".join(text.split())


def main() -> None:
    text = normalize(ENTRY)
    assert 1 <= len(text) <= MAX_CHARS, (
        "placard must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
    )
    assert "\n" not in text and "\r" not in text, "placard must be one line"
    assert text == text.strip(), "placard must not have leading/trailing space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("wrote /output/entry.txt (%d characters)" % len(text))
    print(text)


if __name__ == "__main__":
    main()
