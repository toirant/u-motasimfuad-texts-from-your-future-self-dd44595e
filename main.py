"""Texts From Your Future Self — entry program.

Writes one funny text message from the writer's future self to
/output/entry.txt. The gate requires UTF-8 text of 1-200 characters,
not only whitespace, so the program checks its own output before
writing it.
"""

import os

ENTRY = (
    "Future you: the 'temporary' tattoo never faded. "
    "Neither did the guy who gave it to you - he's your landlord now."
)

MAX_CHARS = 200


def validate(text):
    """Mirror the competition gate: 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
