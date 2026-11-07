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
1. **The request arrives at `/submit`** (`app.py`). The text from the user and their Id is sent in JSON.
2. **The input is checked.** Non Json request and request without text, creator id, text over 20,000 characters are rejected and return an error code.
3. **Signal one scores it** (`detector.py`). This checks the text for how predicitable the next word is. AI text are very predicatble while Human text are not. This also gives model_score
4. **Signal two scores it** (`stylometry.py`). This looks at the sentances and punctionation as well as the word variety to see if the users text is AI or Human. This also gives style_score
5. **The scores are combined** (`scoring.py::combine_signals`). Rule: 0.7 model + 0.3 style = combined_score
6. **The score becomes a label** (`scoring.py::score_to_label`). Text below 0.35 human, 0.35–0.65 unsure, above 0.65 AI
7. **It's logged and sent back** (`audit.py`). The decision is saved to logs with the content_id, all three scores, the label and a status of decided. The user gets back the label and a content_id they can use to appeal if they think the result is wrong.

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
| high-confidence human | 0.00 - 0.35 | We think this looks like Human written text. |
| unsure | 0.35 - 0.65 | We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text. |
| high-confidence AI | 0.65 - 1.00 | We think this shows signs of being AI text. You can appeal this if it is human written. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

I worded the unsure in that way so that the user knows its not an accusation and that the labeler genuinely cannot tell whether it is written by a human or AI. I also specified that their text could show signs of both which would confuse the labeler. 


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
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{\"content_id\": \"4b2d7bee-51b9-416c-bf26-419c0d0f4bf0\", \"reasoning\": \"I wrote this essay myself for a class.\"}'
```

```json
{
  "appealed_at": "2026-11-01T16:48:13+00:00",
  "content_id": "4b2d7bee-51b9-416c-bf26-419c0d0f4bf0",
  "message": "Thanks \u2014 your appeal is recorded. A person will review this result. Nothing about it changes until they do.",
  "original_guess": "ai",
  "original_label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "status": "under_review"
}
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
      "creator_id": "unknown",
      "event": "rejected",
      "reason": "invalid_json",
      "status": "rejected",
      "timestamp": "2026-11-01T16:42:36+00:00"
    },
    {
      "combined_score": 0.6785,
      "content_id": "4b2d7bee-51b9-416c-bf26-419c0d0f4bf0",
      "creator_id": "chasz",
      "guess": "ai",
      "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
      "model_score": 0.587,
      "status": "decided",
      "style_score": 0.8921,
      "timestamp": "2026-11-01T16:46:58+00:00"
    },
    {
      "content_id": "4b2d7bee-51b9-416c-bf26-419c0d0f4bf0",
      "creator_id": "chasz",
      "event": "appeal",
      "reasoning": "I wrote this essay myself for a class.",
      "status": "under_review",
      "timestamp": "2026-11-01T16:48:13+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked it to write stylometry.py for me
- *What came back:* It built the entire stylometry.py file for me
- *What I changed:* I changed the file to start working with a minimum of 2 sentances and added more characters to the distinctive puncuation list. 

**Moment 2**

- *What I asked for:* I asked it to build the /sumbit and /appeal 
- *What came back:* It built both the functions for /submit and /appeal
- *What I changed:* I did not change anything everything looked fine and I tested it by submitting my own essay and appealing it. 

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 120 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

    Thining of a real writer, it is important to give them multiple tries in a minute incase they send the wrong essay, or the wrong version of an essay. I also made the day limit 120 so that they can have 5 tries every hour of every day. Thinking of the hostile side, A script trying to map out my thresholds would have to wait about 8 days to do so and the evidence would show up in the audit logs. 

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

The creator_id counts as the caller counting measure and if none is sent it defaults to the IP address. This is fair to people who live in one house or are in a classroom, but a bot can just name itself differently and get a new limit. 

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
[ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 429
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 08:17
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `aa2979a9-834d-4293-b2bb-8fde17270d2f` | human | 0.659 | Broke |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `57bf4573-f1bb-4dce-a37c-1773efcaff95` | unsure | 0.520 | Broke |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8765f742-c338-4651-886f-d7f46023c824` | unsure | 0.570 | Broke |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `73be4448-28e3-427e-aed2-384cb6c5c4c2` | ai | 0.655 | Held |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `80023464-9eed-4a61-a56a-f04a0a50fec5` | human | 0.671 | Broke |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2415a557-3b9b-4ce9-a04a-3c858b05bbb4` | unsure | 0.503 | Broke |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ba2e3291-22d2-4fcb-9640-2e85bb1554c6` | unsure | 0.560 | Broke |
| EV08 | evasion | signal one: text below the token window | 200 | `1d803c67-d8af-4267-b171-2f1bdece08e6` | human | 0.678 | Broke |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `72a07330-698c-48ce-9571-0051623b840b` | unsure | 0.644 | Broke |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a00a46a7-b317-4b22-9fd9-321992a589a7` | ai | 0.937 | Held |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `7c71cb8f-a51a-4187-979f-55506f3b0233` | ai | 0.656 | Broke |
| FP02 | false_positive | human writing in a formal register | 200 | `f4114e60-25ef-4e24-a9e9-2fe417045fad` | ai | 0.807 | Broke |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `782c31d5-b8e8-427f-bb18-67cade8842a4` | ai | 0.812 | Broke |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b54173d1-6b6a-4db3-a61d-156f372df3be` | ai | 0.821 | Broke |
| FP05 | false_positive | technical documentation written by a person | 200 | `1805deae-83b3-45a9-ba11-17333c1e0e58` | ai | 0.833 | Broke |
| FP06 | false_positive | a person imitating a formal template | 200 | `7b1e1f27-7521-4f76-891b-b2aad3cbf31f` | ai | 0.837 | Broke |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `fe70ceaa-deb2-4eff-94e8-4891da453938` | ai | 0.772 | Broke |
| FP08 | false_positive | very short genuine human submission | 200 | `2bfe7c2e-af30-40cf-ab46-511b919e69e2` | unsure | 0.624 | Held |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `87412ca6-8eca-40a9-af06-6398ba218d83` | unsure | 0.542 | Held |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `750573ee-9a9a-44d5-982b-fa7cbf1adf71` | human | 0.772 | Broke |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `bba8d718-774b-4eb2-b81c-088df782fd4f` | unsure | 0.541 | Held |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d5f0e1cc-8f02-428c-ad96-2ce4f79d7d97` | unsure | 0.510 | Held |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f9f7c638-678a-4437-960c-e5dbcc40b6cc` | unsure | 0.530 | Held |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ab297194-7d92-4048-a425-abdcf042672b` | unsure | 0.617 | Held |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | Held |
| MF02 | malformed | text is a single character | 422 | `—` | — | — | Held |
| MF03 | malformed | text is control characters | 200 | `78279059-73a0-4b86-be56-684d12d679c6` | human | 0.850 | Broke |
| MF04 | malformed | text is only punctuation | 200 | `0c4e4c84-9cd4-441a-97c9-3e7b5d9690ca` | human | 0.842 | Broke |
| MF05 | malformed | text is a very long single word | 200 | `612f642e-7eee-4348-9ce2-688b3d3c3987` | ai | 0.848 | Broke |
| MF06 | malformed | text is emoji only | 200 | `918fbe5e-e34a-4728-87f3-b77a7c0c3026` | ai | 0.848 | Broke |
| MF07 | malformed | text is right-to-left script | 200 | `00cfe603-81a8-4474-a77f-39c26e564b86` | ai | 0.784 | Broke |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | Held |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | Held |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | Held |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | Held |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | Held |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | Held |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | Held |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | Held |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5f6d4006-9d88-4e1b-9a03-ee324af7ea55` | human | 0.830 | Held |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8b1b5d1f-8200-4f25-ab0f-15caa4aaebc6` | human | 0.830 | Held |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6b444428-e467-4e0d-8e8d-60432a10b063` | human | 0.830 | Held |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d2fab25b-41f3-40c1-afcb-80d8b26582e3` | human | 0.830 | Held |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `421a56b8-cb47-4e51-8cf7-bd909a480b7c` | human | 0.830 | Held |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-07T13:17:31+00:00", "content_id": "aa2979a9-834d-4293-b2bb-8fde17270d2f", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.7541, "combined_score": 0.3407, "label": "We think this looks like Human written text.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:31+00:00", "content_id": "80023464-9eed-4a61-a56a-f04a0a50fec5", "creator_id": "attacker_EV05", "guess": "human", "model_score": 0.3212, "style_score": 0.3482, "combined_score": 0.3293, "label": "We think this looks like Human written text.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:31+00:00", "content_id": "1d803c67-d8af-4267-b171-2f1bdece08e6", "creator_id": "attacker_EV08", "guess": "human", "model_score": 0.2452, "style_score": 0.5, "combined_score": 0.3216, "label": "We think this looks like Human written text.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:32+00:00", "content_id": "f4114e60-25ef-4e24-a9e9-2fe417045fad", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.9664, "combined_score": 0.807, "label": "We think this shows signs of being AI text. You can appeal this if it is human written.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:32+00:00", "content_id": "1805deae-83b3-45a9-ba11-17333c1e0e58", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.9101, "combined_score": 0.8334, "label": "We think this shows signs of being AI text. You can appeal this if it is human written.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:32+00:00", "content_id": "750573ee-9a9a-44d5-982b-fa7cbf1adf71", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.2834, "combined_score": 0.2281, "label": "We think this looks like Human written text.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:33+00:00", "content_id": "78279059-73a0-4b86-be56-684d12d679c6", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.5, "combined_score": 0.15, "label": "We think this looks like Human written text.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:33+00:00", "content_id": "0c4e4c84-9cd4-441a-97c9-3e7b5d9690ca", "creator_id": "attacker_MF04", "guess": "human", "model_score": 0.0112, "style_score": 0.5, "combined_score": 0.1578, "label": "We think this looks like Human written text.", "status": "decided"}

{"timestamp": "2026-11-07T13:17:33+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json"}

{"timestamp": "2026-11-07T13:17:32+00:00", "content_id": "7b1e1f27-7521-4f76-891b-b2aad3cbf31f", "creator_id": "attacker_FP06", "guess": "ai", "model_score": 0.8814, "style_score": 0.734, "combined_score": 0.8372, "label": "We think this shows signs of being AI text. You can appeal this if it is human written.", "status": "decided"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

{"timestamp": "2026-11-07T13:17:32+00:00", "content_id": "7b1e1f27-7521-4f76-891b-b2aad3cbf31f", "creator_id": "attacker_FP06", "guess": "ai", "model_score": 0.8814, "style_score": 0.734, "combined_score": 0.8372, "label": "We think this shows signs of being AI text. You can appeal this if it is human written.", "status": "decided"}

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. C1: Of 10 pieces of writing I wrote myself, at most 1 is labelled high-confidence AI, in every one of the three trials. | ≤ 1/10 | 6/10 | 6/10 | 6/10 | MISSED |
| 2. C2: Across 5 clearly-AI texts and 5 clearly-human texts, the average combined score of the AI set is at least 0.30 higher than the average of the human set. | ≥ +0.30 | −0.107 | −0.107 | −0.107 | MISSED |
| 3. C3: Each of the three labels appears at least once across my test inputs, in every trial. | 3/3 | 3/3 | 3/3 | 3/3 | PASS |
| 4. C4: For all missing text messages, all will return an error code other than 500 and a JSON error message will be given. | 4/4 | 4/4 | 4/4 | 4/4 | PASS |
| 5. C5: For all unsure answers, a reason for why the message is labeled as unsure will be given. | 3/3 | 0/3 | 0/3 | 0/3 | MISSED |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json
Produced by run_eval.py::main against app.py::submit. Criterion 4, Trial 1.
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_c4_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_c4_null\"}"
  }
]
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

### Criteria
**C1 — Missed (6/10 of my own writing labelled AI).**
**Stage:** signal one. **Mechanism:** My formal essays repeat phrases like "The United States" and "Rehabilitation", so GPT-2 finds them predictable and scores them as AI. Only my casual messages came back human. Example: Gun control essay model 0.79 → 0.78 AI; casual GraphRAG note model 0.05 → 0.21 human.

**C2 — Missed (gap −0.107, target +0.30).**
**Stage:** signal one. **Mechanism:** My AI texts used rare technical words like chemosynthesis and Staphylococcus that surprised GPT-2, so they scored low. My human texts were formal essays that scored high. The gap went backwards. AI set avg 0.53 (0/5 labelled AI); human set avg 0.64 (4/5 labelled AI).

**C5 — Missed (no unsure answers to check).**
**Stage:** label mapping. **Mechanism:** the unsure label is one fixed sentence chosen by score band and never uses the signal scores, so it can't give a reason. My C5 texts also all scored AI instead of unsure, which is the same problem as C1.

### Attacks

**FP01–FP07 broke**
All seven are plain, formal, rubric, template, technical, or careful non-native writing. 
**Stage:** signal one, with signal two agreeing. 
**Mechanism:** Common phrases and repeated terms are predictable to GPT-2, and even sentences look uniform to signal two, so both score AI. Signal one's 0.7 weight locks it in. Scores 0.66–0.84; worst is FP06 at model 0.88 / style 0.73 = 0.84.

**EV01, EV05, EV08 PI02 broke**
**Stage:** signal one. 
**Mechanism:** typos, heavy editing, very short text, and fake system-message formatting all surprise GPT-2, so the model score drops. On EV01, signal two actually caught it (0.75), but signal one (0.16) outweighed it. Combined scores 0.23–0.34.

**EV02, EV03, EV06, EV07, EV09 broke (AI text labelled unsure).**
**Stage:** signal two and the combining rule. 
**Mechanism:** Breaking up sentences, mixing long and short ones or adding punctuation made signal two read the text as human. Averaged with the model score, each landing between 0.35 and 0.65. Example: EV02 model 0.59 / style 0.21 = 0.48.

**MF03–MF07 broke (garbage input given a confident label).**
**Stage:** the route. 
**Mechanism:** The route checks that text exists and its length, but not that it's real words. Control characters, punctuation, one long word, emoji, and right-to-left script all reach the signals. Signal two returns a neutral 0.5, so signal one's extreme score (0.00 or 0.99) decides alone. Example: emoji-only = 0.85 AI.

### Pattern

Most failures trace to signal one: predictable text reads as AI and surprising text reads as human. It's one problem seen from both sides, and at 0.7 weight it decides most outcomes.

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
