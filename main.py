# One-line pitch entry for make.fun's "A Day of One-Line Pitches"
# (program/v1, Python 3.13, standard library only, no network).
# Writes one fixed sentence to /output/entry.txt. The gate takes UTF-8
# text of 1 to 240 characters that is not only whitespace, so the file
# holds exactly the sentence: no trailing newline, no extra words.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The sentence is fixed and deterministic: the same bytes on every run.
#
# v2 (iteration round 2) — tightened from v1 against the judge's brief
# (a plain-spoken editor who has never coded, weighing persuasion,
# clarity, truth, then warmth and craft, in that order):
# - "explaining to anyone who'll listen" -> "telling friends about":
#   shorter, warmer, and "friends" echoes the brief's "a friend".
# - "hand you" -> "builds you": clearer agency, present tense, one
#   character shorter (ties break toward fewer bytes).
# - "just tell it what to change" -> "just tell it, and it changes
#   it": same low-risk safety net, punchier friend-speak ending.
# Kept from v1, the beats that won our earlier one-line entries: a
# concrete human scene instead of an abstraction, and a small
# low-risk mechanism instead of a slogan. No speed claim, no "free"
# claim, no jargon: nothing a beginner would find doesn't hold up.
# Rejected in playtest: a shower/coffee scene ("while you make
# coffee" overpromises speed and fails the truth criterion); a
# "tonight" urgency line (same problem); a "no coding, no jargon"
# version (template language every other entry will use).

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "That app idea you keep telling friends about: say it once, "
    "in your own words, and an AI agent builds you a working first "
    "version to poke at \u2014 if it's not right, just tell it, "
    "and it changes it."
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    # The grader collects outputs as another user: leave it readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
