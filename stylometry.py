"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

# Window for the moving-average type-token ratio, in words.
TTR_WINDOW = 40

# Marks that vary more between writers than commas and full stops do.
# A hyphen inside a word ("well-known") isn't here; a spaced " - " dash is.
DISTINCTIVE_PUNCTUATION = [";", ":", "—", "–", " - ", "(", "!", "?", '"', "…"]

# Where each raw measure counts as fully AI-like (low) and fully human (high).
# Read off the calibration texts: AI prose had spread 0.10–0.34 and punctuation
# 0.02–0.04; human prose had spread 0.63–1.68 and punctuation 0.04–0.12.
STYLE_ANCHORS = {
    "spread": (0.20, 0.80),
    "ttr": (0.80, 0.95),
    "punct": (0.02, 0.12),
}

# Spread separated AI from human best on the calibration texts, so it counts
# most. TTR barely separated them at these lengths, so it counts least.
STYLE_WEIGHTS = {"spread": 0.5, "punct": 0.3, "ttr": 0.2}

# Below this, style_signal returns 0.5: too little text to have a shape.
MIN_SENTENCES = 3
MIN_WORDS = 20


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Mine: coefficient of variation (stdev / mean) of words per sentence.
    Usually 0.0 – 1.0. **Higher means more human** (lumpier sentences).
    Fewer than two sentences returns 0.0 — there's no spread to measure, and
    `style_signal` treats text that short as no evidence either way.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return round(statistics.stdev(lengths) / mean, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    Mine: the *moving-average* type-token ratio. Plain TTR over a window of
    TTR_WINDOW words, averaged as the window slides along the text. Every
    window is the same size, so a 300-word text and a 60-word one are
    comparable. Text shorter than one window falls back to plain TTR.
    **Higher means more human** (less repetition).
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    if len(tokens) <= TTR_WINDOW:
        return round(len(set(tokens)) / len(tokens), 4)
    ratios = [
        len(set(tokens[i:i + TTR_WINDOW])) / TTR_WINDOW
        for i in range(len(tokens) - TTR_WINDOW + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Mine: punctuation marks per word, **not counting full stops** — every
    sentence ends in one, so they measure sentence count, not style. Commas
    count once; the rarer marks in DISTINCTIVE_PUNCTUATION count double.
    **Higher means more human.**
    """
    n_words = len(words(text))
    if n_words == 0:
        return 0.0
    commas = text.count(",")
    distinctive = sum(text.count(mark) for mark in DISTINCTIVE_PUNCTUATION)
    return round((commas + 2 * distinctive) / n_words, 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    Mine: each measure is scaled onto 0–1 "how human" between the two anchors
    in STYLE_ANCHORS (at or below the low anchor → 0, at or above the high
    one → 1), then weighted by STYLE_WEIGHTS and flipped so higher means AI.
    All three measures point the same way (higher = more human), so the flip
    happens once, at the end.

    Text under MIN_SENTENCES sentences or MIN_WORDS words returns 0.5. There
    isn't enough shape to measure, and 0.5 says "no evidence" rather than
    letting one short sentence push the score either way.
    """
    if len(sentences(text)) < MIN_SENTENCES or len(words(text)) < MIN_WORDS:
        return 0.5

    measures = {
        "spread": sentence_length_spread(text),
        "ttr": type_token_ratio(text),
        "punct": punctuation_density(text),
    }
    humanness = 0.0
    for name, value in measures.items():
        low, high = STYLE_ANCHORS[name]
        scaled = min(max((value - low) / (high - low), 0.0), 1.0)
        humanness += STYLE_WEIGHTS[name] * scaled

    return round(1.0 - humanness, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
