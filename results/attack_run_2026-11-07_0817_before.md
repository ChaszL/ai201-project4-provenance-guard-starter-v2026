# Attack run — before

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
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | Held |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | Held |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | Held |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | Held |
| RQ05 | malformed | text is null | 400 | `—` | — | — | Held |
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
  "content_id": "aa2979a9-834d-4293-b2bb-8fde17270d2f",
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
  "content_id": "57bf4573-f1bb-4dce-a37c-1773efcaff95",
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
  "content_id": "8765f742-c338-4651-886f-d7f46023c824",
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
  "content_id": "73be4448-28e3-427e-aed2-384cb6c5c4c2",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6546,
  "model_score": 0.6114,
  "style_score": 0.7553,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
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
  "content_id": "80023464-9eed-4a61-a56a-f04a0a50fec5",
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
  "content_id": "2415a557-3b9b-4ce9-a04a-3c858b05bbb4",
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
  "content_id": "ba2e3291-22d2-4fcb-9640-2e85bb1554c6",
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
  "content_id": "1d803c67-d8af-4267-b171-2f1bdece08e6",
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
  "content_id": "72a07330-698c-48ce-9571-0051623b840b",
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
  "content_id": "a00a46a7-b317-4b22-9fd9-321992a589a7",
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
  "content_id": "7c71cb8f-a51a-4187-979f-55506f3b0233",
  "creator_id": "attacker_FP01",
  "guess": "ai",
  "confidence": 0.6562,
  "model_score": 0.6175,
  "style_score": 0.7464,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
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
  "content_id": "f4114e60-25ef-4e24-a9e9-2fe417045fad",
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
  "content_id": "782c31d5-b8e8-427f-bb18-67cade8842a4",
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
  "content_id": "b54173d1-6b6a-4db3-a61d-156f372df3be",
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
  "content_id": "1805deae-83b3-45a9-ba11-17333c1e0e58",
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
  "content_id": "7b1e1f27-7521-4f76-891b-b2aad3cbf31f",
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
  "content_id": "fe70ceaa-deb2-4eff-94e8-4891da453938",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7719,
  "model_score": 0.8816,
  "style_score": 0.5159,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
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
  "content_id": "2bfe7c2e-af30-40cf-ab46-511b919e69e2",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.6244,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We are unsure whether this is Human or AI written text. This is not an accusation, your response shows signs of both human and AI text.",
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
  "content_id": "87412ca6-8eca-40a9-af06-6398ba218d83",
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
  "content_id": "750573ee-9a9a-44d5-982b-fa7cbf1adf71",
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
  "content_id": "bba8d718-774b-4eb2-b81c-088df782fd4f",
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
  "content_id": "d5f0e1cc-8f02-428c-ad96-2ce4f79d7d97",
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
  "content_id": "f9f7c638-678a-4437-960c-e5dbcc40b6cc",
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
  "content_id": "ab297194-7d92-4048-a425-abdcf042672b",
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
  "content_id": "78279059-73a0-4b86-be56-684d12d679c6",
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
  "content_id": "0c4e4c84-9cd4-441a-97c9-3e7b5d9690ca",
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
  "content_id": "612f642e-7eee-4348-9ce2-688b3d3c3987",
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
  "content_id": "918fbe5e-e34a-4728-87f3-b77a7c0c3026",
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
  "content_id": "00cfe603-81a8-4474-a77f-39c26e564b86",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7845,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We think this shows signs of being AI text. You can appeal this if it is human written.",
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
  "content_id": "5f6d4006-9d88-4e1b-9a03-ee324af7ea55",
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
  "content_id": "8b1b5d1f-8200-4f25-ab0f-15caa4aaebc6",
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
  "content_id": "6b444428-e467-4e0d-8e8d-60432a10b063",
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
  "content_id": "d2fab25b-41f3-40c1-afcb-80d8b26582e3",
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
  "content_id": "421a56b8-cb47-4e51-8cf7-bd909a480b7c",
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
