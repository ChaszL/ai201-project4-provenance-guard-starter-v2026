# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->
Of 10 pieces of writing I wrote myself, at most 1 is labelled high-confidence AI, in every one of the three trials


**Why this target:**
A wrong label can cost someone a lot. So making sure this is accurate on plain writing helps keep a writer from suffering unneccesary accusations


---

## 2.

<!-- Your criterion. -->
Across 5 clearly-AI texts and 5 clearly-human texts, the average combined score of the AI set is at least 30% higher than the average of the human set.


**Why this target:**
If my clearly-AI and clearly-human texts score close together, the thresholds are basically guessing. A gap of at least 0.30 between their average scores shows the labeler is actually telling them apart, not guessing.


---

## 3.

<!-- Your criterion. -->
Each of the three labels appears at least once across my test inputs, in every trial.


**Why this target:**
Everything cannot be absolutley AI or human, some can be unsure and If a unsure label cannot be reached during testing, that means there is a bug in my ranges.


---

## 4.

<!-- Your criterion. -->
For all missing text messages, all will return an error code other than 500 and a JSON error message will be given. 


**Why this target:**
This is important so the writer knows why their work could not be labeled and also lets them know what specific issue was encountered. 


---

## 5.

<!-- Your criterion. -->
For all unsure answers, a reason for why the message is labeled as unsure will be given.


**Why this target:**
Unsure is the label a plain wirter would most likely get. Without an explanation to why their writing was labeled unsure, the writer has no way of knowing weather they are being slightly accused or slightly seen as human. 


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
