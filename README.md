# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to gpt2, mapped from 0–1. Low perplexity gives a high, AI-like score.

**Why that might differ between human and AI writing:** An LLM writes by picking likely next tokens, so its output is text a model finds likely. Humans make choices a model wouldn't rank first.

**What it can't see:** Authorship. Plain writing from a human is just as predictable and scores as AI. AI text pushed toward rare words or paraphrased scores as human. It only reads the first 400 tokens.

### Signal two — the style signal

**What it measures:** The text's shape: sentence-length spread, type-token ratio and punctuation density. It doesn't understand a word.

**Why that might differ between human and AI writing:** AI generated text uses a band of vocabulary and tidy punctuation. Human writing is lumpier and can use more punctuation and less vocabulary.

**What it can't see:** Typos, split sentences, extra dashes or a pasted quotation move it without changing who wrote the text. Type-token ratio falls with length. Plain human writing has the same even shape as AI writing, so this signal shares signal one's worst false positive instead of catching it.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** A weighted average that trusts the model signal more than the style signal because small edits to style can change the scoring of the style a lot. 

**The numbers:** model 0.7, style 0.3. Human below 0.35, unsure 0.35–0.65, AI above 0.65.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
"Social media has changed how we communicate. A lot. It allows people to connect with friends and family across the world, share their experiences, and access information instantly - but it also has downsides! Many users struggle with comparison. And privacy? That is a growing concern for everyone."

Model signal: 0.65 (AI)
Style signal: 0.10 (Human)
Rule: 0.7(0.65) + 0.3(0.10) = 0.49 (Unsure)
---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"Hello my name is chasz whats yours?\", \"creator_id\": \"chasz\"}'
```

```json
{
  "confidence": 0.0,
  "content_id": "39ee97e4-8905-43bd-924c-ee9f5af65e06",
  "creator_id": "chasz",
  "guess": "unsure",
  "label": "placeholder",
  "model_score": 0.0459,
  "status": "decided",
  "style_score": null
}
```

**An appeal**

```bash
$ 
```

```json

```

**What the log shows afterwards**

```bash
$ curl.exe http://127.0.0.1:5000/log?limit=3
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": null,
      "content_id": "a7dcd881-3f58-4d36-b4fe-e6821ebd2a32",
      "creator_id": "chasz",
      "guess": "unsure",
      "label": "placeholder",
      "model_score": 0.5113,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-10-31T15:57:03+00:00"
    },
    {
      "combined_score": null,
      "content_id": "d357b8e6-0720-456d-97ca-2eed4c998cc3",
      "creator_id": "chasz",
      "guess": "unsure",
      "label": "placeholder",
      "model_score": 0.234,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-10-31T15:57:03+00:00"
    },
    {
      "combined_score": null,
      "content_id": "39ee97e4-8905-43bd-924c-ee9f5af65e06",
      "creator_id": "chasz",
      "guess": "unsure",
      "label": "placeholder",
      "model_score": 0.0459,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-10-31T16:07:26+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
