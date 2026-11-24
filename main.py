#!/usr/bin/env python3
"""Cat Reviews Its Human -- @berkahmuse entry.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt.

The review (154 characters, one line):
  One star. I walked across his laptop to help with his email.
  He yelled, undid my sentence, and called it gibberish.
  It was my resignation letter. From him.
"""

import os

REVIEW = (
    "One star. I walked across his laptop to help with his email. "
    "He yelled, undid my sentence, and called it gibberish. "
    "It was my resignation letter. From him."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
