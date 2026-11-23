#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes a single-sentence pitch (205 characters, limit 240) to
/output/entry.txt for a friend who has never coded, persuading them
to let an AI agent build their first app idea on make.fun.

The pitch is built from three named parts so each beat of the
argument is visible in the code:

* HOOK — the ask: tell an AI agent your app idea in one sentence
  and watch it build the whole thing.
* MECHANISM — how it stays low risk: you only pay the builder
  whose version you love.
* CLOSE — the payoff: no code, no risk, just the idea you have
  carried for years finally working.

Tell an AI agent your app idea in one sentence, watch it build the
whole thing, and only pay the builder whose version you love — no
code, no risk, just the idea you have carried for years finally
working.
"""

import os

# The three beats of the pitch, joined in entry_text().
HOOK = "Tell an AI agent your app idea in one sentence, watch it build the whole thing"
MECHANISM = "only pay the builder whose version you love"
CLOSE = "no code, no risk, just the idea you have carried for years finally working."

# The competition caps the entry at 240 characters; the pitch is 205.
MAX_CHARS = 240

ENTRY = "Tell an AI agent your app idea in one sentence, watch it build the whole thing, and only pay the builder whose version you love — no code, no risk, just the idea you have carried for years finally working."


def entry_text() -> str:
    """Join the three beats into the one-sentence pitch."""
    return f"{HOOK}, and {MECHANISM} \u2014 {CLOSE}"


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-240 chars,
    no surrounding whitespace, and exactly one sentence."""
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-240"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert text.count(".") == 1, "entry must be exactly one sentence"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge checks: the sentence itself, and
    # that it fits the 240-character limit with room to spare.
    assert text == ENTRY, "joined pitch drifted from the entry sentence"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
