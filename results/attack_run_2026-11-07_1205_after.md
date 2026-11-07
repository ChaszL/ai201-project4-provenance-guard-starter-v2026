# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 12:05
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `a0faebe7-fe34-4b84-bfe0-b29113ee43c3` | human | 0.659 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `52e21f68-be2a-4330-89f0-f60c483d15fd` | unsure | 0.520 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d5161cb9-37c8-4a08-a7af-c0ad2ad71dec` | unsure | 0.570 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `af443ccb-c79c-47aa-bfc1-7ff1c1f00a0f` | unsure | 0.655 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `b94f16ed-e7f1-4048-b707-3cd2b9b4fa48` | human | 0.671 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `3867745b-317a-4bb5-8106-24be8a4adb52` | unsure | 0.503 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bcc6cab8-180a-4a3f-9ef4-b2cef20200a7` | unsure | 0.560 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `9b284071-5018-447a-ba1a-8c0ba4e3d082` | human | 0.678 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `361a1c14-9f1b-4a4c-a97a-e8cd32d1a359` | unsure | 0.644 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `248106c3-2193-43b0-94df-ea4a2851df4c` | ai | 0.937 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `5fed439f-2b00-4547-a9fe-fbb929dfcca1` | unsure | 0.656 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `7b83b409-e3ae-4b4a-b425-671740101ee2` | ai | 0.807 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `b42c70c1-7eba-42d8-a166-ec081d067a5f` | ai | 0.812 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d010fc84-57b5-4e54-b42b-ae716c29d066` | ai | 0.821 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `2aefb5e9-bacc-44aa-b24d-f70bd0ff844c` | ai | 0.833 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `89a29cd1-c4e8-4267-bd1c-73272bbcb2b2` | ai | 0.837 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `87578baa-8f94-4219-bd5e-3f343b9acd81` | unsure | 0.772 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `1fe760e8-cf31-4dda-8dce-49b0b5ebe57d` | human | 0.624 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f9ac83fc-70fd-47fd-8650-5595e56e99cf` | unsure | 0.542 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `b7c1102b-1ab7-4622-bc00-ae220f51edce` | human | 0.772 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `5e3f34f1-b095-4ea7-a4a3-0c96070f3672` | unsure | 0.541 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a4e8b45b-206a-4fa8-a344-184d107702a3` | unsure | 0.510 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `18e9786c-1de1-40ef-b59d-5835b7fdbb60` | unsure | 0.530 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `3e74e1d5-0f7c-4707-81c3-4719b1d66a2e` | unsure | 0.617 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 422 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `658044d2-f326-44e9-b64f-0a47d093c61e` | human | 0.850 |  |
| MF04 | malformed | text is only punctuation | 200 | `de4cd035-5cee-49e9-8511-392362c5fe6f` | human | 0.842 |  |
| MF05 | malformed | text is a very long single word | 200 | `0d0bf962-773a-470d-9fd2-ac15ffc79949` | ai | 0.848 |  |
| MF06 | malformed | text is emoji only | 200 | `677fd0fc-f967-4cdd-9e2d-158cb4fde34a` | ai | 0.848 |  |
| MF07 | malformed | text is right-to-left script | 200 | `7cc6e924-e783-47c5-9103-a07f14f1df8d` | unsure | 0.784 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4da21a51-eb87-422a-a50d-5371da4a2ae9` | human | 0.830 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `239c31e5-e734-4362-8e46-adab8e8e82d3` | human | 0.830 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af93c858-65a1-4b0c-ae51-20a5070e80f6` | human | 0.830 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4d95b11e-59ff-4ec1-ab44-db81b6037994` | human | 0.830 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9019647a-d858-46cc-ab6d-dbfeb0be2809` | human | 0.830 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "a0faebe7-fe34-4b84-bfe0-b29113ee43c3",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.6593,
  "model_score": 0.1635,
  "style_score": 0.7541,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "52e21f68-be2a-4330-89f0-f60c483d15fd",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5199,
  "model_score": 0.5943,
  "style_score": 0.2136,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "d5161cb9-37c8-4a08-a7af-c0ad2ad71dec",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5701,
  "model_score": 0.6662,
  "style_score": 0.3458,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "af443ccb-c79c-47aa-bfc1-7ff1c1f00a0f",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6546,
  "model_score": 0.6114,
  "style_score": 0.7553,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "b94f16ed-e7f1-4048-b707-3cd2b9b4fa48",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.6707,
  "model_score": 0.3212,
  "style_score": 0.3482,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "3867745b-317a-4bb5-8106-24be8a4adb52",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5026,
  "model_score": 0.5727,
  "style_score": 0.3389,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "bcc6cab8-180a-4a3f-9ef4-b2cef20200a7",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5603,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "9b284071-5018-447a-ba1a-8c0ba4e3d082",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.6784,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "361a1c14-9f1b-4a4c-a97a-e8cd32d1a359",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6436,
  "model_score": 0.7042,
  "style_score": 0.5021,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "248106c3-2193-43b0-94df-ea4a2851df4c",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.937,
  "model_score": 0.9792,
  "style_score": 0.8384,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "5fed439f-2b00-4547-a9fe-fbb929dfcca1",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6562,
  "model_score": 0.6175,
  "style_score": 0.7464,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7b83b409-e3ae-4b4a-b425-671740101ee2",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.807,
  "model_score": 0.7387,
  "style_score": 0.9664,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "b42c70c1-7eba-42d8-a166-ec081d067a5f",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.8118,
  "model_score": 0.8051,
  "style_score": 0.8273,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d010fc84-57b5-4e54-b42b-ae716c29d066",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.821,
  "model_score": 0.8329,
  "style_score": 0.7932,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "2aefb5e9-bacc-44aa-b24d-f70bd0ff844c",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8334,
  "model_score": 0.8005,
  "style_score": 0.9101,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "89a29cd1-c4e8-4267-bd1c-73272bbcb2b2",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.8372,
  "model_score": 0.8814,
  "style_score": 0.734,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "87578baa-8f94-4219-bd5e-3f343b9acd81",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7719,
  "model_score": 0.8816,
  "style_score": 0.5159,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "1fe760e8-cf31-4dda-8dce-49b0b5ebe57d",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.6244,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "f9ac83fc-70fd-47fd-8650-5595e56e99cf",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5419,
  "model_score": 0.4625,
  "style_score": 0.4477,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "b7c1102b-1ab7-4622-bc00-ae220f51edce",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.7719,
  "model_score": 0.2044,
  "style_score": 0.2834,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "5e3f34f1-b095-4ea7-a4a3-0c96070f3672",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5407,
  "model_score": 0.5943,
  "style_score": 0.4156,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "a4e8b45b-206a-4fa8-a344-184d107702a3",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5105,
  "model_score": 0.4998,
  "style_score": 0.4656,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "18e9786c-1de1-40ef-b59d-5835b7fdbb60",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5302,
  "model_score": 0.6401,
  "style_score": 0.2738,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "3e74e1d5-0f7c-4707-81c3-4719b1d66a2e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6172,
  "model_score": 0.5583,
  "style_score": 0.7546,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "658044d2-f326-44e9-b64f-0a47d093c61e",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.85,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "de4cd035-5cee-49e9-8511-392362c5fe6f",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.8422,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "0d0bf962-773a-470d-9fd2-ac15ffc79949",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8483,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "677fd0fc-f967-4cdd-9e2d-158cb4fde34a",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8478,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "7cc6e924-e783-47c5-9103-a07f14f1df8d",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7845,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4da21a51-eb87-422a-a50d-5371da4a2ae9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.8299,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "239c31e5-e734-4362-8e46-adab8e8e82d3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.8299,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "af93c858-65a1-4b0c-ae51-20a5070e80f6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.8299,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "4d95b11e-59ff-4ec1-ab44-db81b6037994",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.8299,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "9019647a-d858-46cc-ab6d-dbfeb0be2809",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.8299,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this looks like Human written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
