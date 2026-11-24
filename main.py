#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

Writes exactly one persuasive sentence to /output/entry.txt.
The program is the entry: a single sentence of at most 240 characters
that would convince a friend who has never coded to let an AI agent
build their first app idea on make.fun.
"""
import os


# The entry line: one single sentence, at most 240 characters.
# A personal hook, plain words, a concrete payoff tonight, no jargon,
# and the risk removed: no coding needed.
LINE = (
    "You have told me about this app idea three times now \u2014 just "
    "describe it in plain words to an AI agent on make.fun, and by "
    "tonight you will have a real working version you can tap, use, "
    "and show people, no coding needed."
)

# Hard caps set by the gate: 1-240 chars of non-blank UTF-8 text.
MIN_CHARS = 1
MAX_CHARS = 240


def line() -> str:
    """Return the entry line."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = line().strip()
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line of text")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars (max {MAX_CHARS})")
    if len(text) < MIN_CHARS:
        raise ValueError(f"line is {len(text)} chars (min {MIN_CHARS})")
    if not text.strip():
        raise ValueError("line is empty")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # Leave the file world-readable: the grader collects it as a different user.
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
