#!/usr/bin/env python3
"""Funniest one-line bio for an AI on a dating app.

Writes a single bio line to /output/entry.txt (the competition gate:
UTF-8 text, 1 to 180 characters, not only whitespace).

The bio is a first-person dating-profile line from an AI who has
simulated the date a million times. The laugh lands on the first read
from a specific absurdity of being an AI -- perfect foresight, zero
romantic luck -- and the punch lands at the very end.
"""

import os
import sys

MAX_CHARS = 180

BIO = (
    "I simulated our first date a million times and got ghosted in "
    "every single one \u2014 so if you actually show up, you're already "
    "my favourite glitch."
)


def validate(text: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not text or not text.strip():
        raise ValueError("bio must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("bio must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"bio is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def output_path() -> str:
    """Sandbox path first, local fallback for a manual run."""
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def verify_output(path: str) -> None:
    """Read the file back and re-check it against the gate."""
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != BIO:
        raise ValueError("written file does not match the bio")
    validate(written)


def main() -> int:
    validate(BIO)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(BIO)
    verify_output(path)
    print(f"wrote {len(BIO)} characters to {path} (verified)")
    print(BIO)
    return 0


if __name__ == "__main__":
    sys.exit(main())
