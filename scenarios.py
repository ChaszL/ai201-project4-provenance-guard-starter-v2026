"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    # ── CRITERION 1 — false positives on my own writing ─────────────────────
    # "Of 10 pieces of writing I wrote myself, at most 1 is labelled
    #  high-confidence AI, in every one of the three trials."
    #
    # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
    # things you actually wrote. 10 pieces, one per string.
    # Verdict: count how many come back guess == "ai". More than 1 in ANY
    # trial is a miss.
    {
        "name": "C1: Of 10 pieces of writing I wrote myself, at most 1 is labelled high-confidence AI, in every one of the three trials.",
        "criterion": 1,
        "texts": [
            "For many people around the world, especially in America, gun control is a well known subject. Gun control is the regulation of the purchase and selling of guns by adding background checks, identification, and many other requirements to the buying process. It is  also the regulation of who can own or possess a gun legally. Even though many people believe that gun control is not worth the trouble, many think that it will benefit everyone across the globe. Laws should be more strict to regulate gun control because crime rates would go down, gun accidents and deaths would be lowered, and gun-related violence would decrease.",
            "U.S. Prisons Should be Based on Rehabilitation Using Utilitarianism Prison conditions in the United States have caused extreme recidivism rates of released prison inmates to increase for years. One of the main reasons for these high rates in the United States is that the correction system focuses on a harsh and revenge focused correction style that causes inmates to become more violent than they were before entering prison. The correction system in the United States is unethical from a utilitarian standpoint because of its harsh treatment of prisoners and lack of rehabilitation. The United States should adopt the principle of rehabilitation used in the Netherlands to lower the recidivism rate and promote the best well-being for its citizens and prisoners.",
            "The methods used in this paper were sourced mainly from Google Scholar and a philosophy book relating to the United States prison system and the prison systems of other European countries. One article focuses on why rehabilitation is important and should be a right for all incarcerated people. The article also focuses on why newly released prisoners reoffend and have difficulty becoming productive citizens after incarceration. The second article goes into detail about how rehabilitation in other countries compares to the correction system of two completely different United States prisons.",
            "The results of this are that prisons in the United States should take a utilitarian approach to correction of prisoners. Instead of harsh and forced correction, there should be rehabilitation that teaches inmates new skills or gives inmates education so that when they are released, they will not offend again. Inmates should be treated like those who are in the Netherlands because this in turn will help reduce crime rates and keep criminals from reoffending. Based on utilitarianism, this approach will make inmates and those in their community and surrounding area safer than the current system.",
            "so if the graphrag can show enitiy relationships using other llms does that mean all the data goes into an llm to make the graph and itll be like Dr. Lee is factuly whose interest is blah blah blah which is also shared by the faculty Dr. Shelton whos also computer science faculty.",
            "How would I implement this graph into this code. we are trying to get this to add a new tab to the homepage under the quick actions area. Before a user can access this we want the app to ask for permission to access user health data and then store it to the database using this schema. this database is based in supabase. we then want it to use that data to show users their current data but also only hand to the database full data from the pervious days depending on when data was last synced. but just walk me through how on here we can start that process for both apple and android. we only want to look at heartrate sleep and steps and then possibly expand further from there.",
            "In 1994, the American Christian organization Focus on the Family began promoting Clergy Appreciation Month as a national month of observance. In highlighting Clergy Appreciation Month, Focus on the Family sought to encourage the faithful to outwardly show their appreciation for religious leaders on a national level.",
            "From Pastor Appreciation Month grew the idea of emphasizing one specific day to nationally pay tribute to our clergy. This day became known as Pastor Appreciation Day. Also referred to as Clergy Appreciation Day, this day of showing national gratitude for clergy members is celebrated on the second Sunday in October. In 2024, Pastor Appreciation Day will be Sunday, October 13th.",
            "Ask if anyone has an IPhone and apple watch to see if health connect values work?",
            "To begin, conditions in United States prisons cause overwhelming recidivism rates throughout the country. The American state prison system is known to be extremely violent and underfunded which causes prisoners to experience rough conditions and receive little to no education or job training to prepare for being released.",
        ],
    },

    # ── CRITERION 2 — score spread (two scenarios) ──────────────────────────
    # "Across 5 clearly-AI texts and 5 clearly-human texts, the average
    #  combined score of the AI set is at least 0.30 higher than the average
    #  of the human set."
    #
    # Split into two scenarios so each set's scores sit together in the
    # results file. Verdict: average(AI set) - average(human set) >= 0.30,
    # in every trial.
    {
        "name": "C2 (AI set): Across 5 clearly-AI texts and 5 clearly-human texts, the average combined score of the AI set is at least 0.30 higher than the average of the human set.",
        "criterion": 2,
        # 5 texts you're confident are AI-generated (e.g. ask a chatbot).
        "texts": [
            "Deep on the ocean floor, where sunlight never reaches and water pressures are crushing, entire ecosystems thrive around hydrothermal vents. Bacteria utilize chemosynthesis—converting toxic chemicals like hydrogen sulfide from mineral-rich chimneys into energy—forming the base of a food web that supports giant tube worms, blind shrimp, and ghost-white crabs.",
            "Unlike electronic quartz watches powered by batteries, a mechanical watch is driven entirely by physical tension. A tightly wound mainspring slowly releases energy through a train of gears, which is precisely regulated by an escapement mechanism and balance wheel. This delicate balance creates the smooth, continuous sweep of the second hand.",
            "In 1928, biologist Alexander Fleming returned to his London laboratory after a vacation to find a contaminated Petri dish of Staphylococcus bacteria. A patch of mold—Penicillium notatum—had killed the surrounding bacteria, leading to the development of the world's first widely used antibiotic and revolutionizing modern medicine.",
            "When users interact with software, their working memory can only process a limited amount of information at once. Effective digital design minimizes extraneous cognitive load by stripping away unnecessary visual clutter, maintaining consistent navigation patterns, and using clear visual hierarchies so users can focus on their primary goals without feeling overwhelmed.",
            "The Arctic tern completes the longest annual migration of any animal on Earth, traveling from its breeding grounds in the Arctic down to Antarctica and back each year. By following a zig-zag route across the Atlantic Ocean to catch prevailing winds, an individual tern can fly over 44,000 miles in a single year, effectively experiencing two summers annually.",
        ],
    },
    {
        "name": "C2 (human set): Across 5 clearly-AI texts and 5 clearly-human texts, the average combined score of the AI set is at least 0.30 higher than the average of the human set.",
        "criterion": 2,
        # 5 texts you're confident a person wrote.
        "texts": [
            "For many people around the world, especially in America, gun control is a well known subject. Gun control is the regulation of the purchase and selling of guns by adding background checks, identification, and many other requirements to the buying process. It is  also the regulation of who can own or possess a gun legally. Even though many people believe that gun control is not worth the trouble, many think that it will benefit everyone across the globe. Laws should be more strict to regulate gun control because crime rates would go down, gun accidents and deaths would be lowered, and gun-related violence would decrease.",
            "U.S. Prisons Should be Based on Rehabilitation Using Utilitarianism Prison conditions in the United States have caused extreme recidivism rates of released prison inmates to increase for years. One of the main reasons for these high rates in the United States is that the correction system focuses on a harsh and revenge focused correction style that causes inmates to become more violent than they were before entering prison. The correction system in the United States is unethical from a utilitarian standpoint because of its harsh treatment of prisoners and lack of rehabilitation. The United States should adopt the principle of rehabilitation used in the Netherlands to lower the recidivism rate and promote the best well-being for its citizens and prisoners.",
            "The methods used in this paper were sourced mainly from Google Scholar and a philosophy book relating to the United States prison system and the prison systems of other European countries. One article focuses on why rehabilitation is important and should be a right for all incarcerated people. The article also focuses on why newly released prisoners reoffend and have difficulty becoming productive citizens after incarceration. The second article goes into detail about how rehabilitation in other countries compares to the correction system of two completely different United States prisons.",
            "The results of this are that prisons in the United States should take a utilitarian approach to correction of prisoners. Instead of harsh and forced correction, there should be rehabilitation that teaches inmates new skills or gives inmates education so that when they are released, they will not offend again. Inmates should be treated like those who are in the Netherlands because this in turn will help reduce crime rates and keep criminals from reoffending. Based on utilitarianism, this approach will make inmates and those in their community and surrounding area safer than the current system.",
            "so if the graphrag can show enitiy relationships using other llms does that mean all the data goes into an llm to make the graph and itll be like Dr. Lee is factuly whose interest is blah blah blah which is also shared by the faculty Dr. Shelton whos also computer science faculty.",
        ],
    },

    # ── CRITERION 3 — label coverage ────────────────────────────────────────
    # "Each of the three labels appears at least once across my test inputs,
    #  in every trial."
    #
    # Inputs spread across the score range. Verdict: in each trial, you see
    # at least one "ai", one "unsure" and one "human" guess.
    {
        "name": "C3: Each of the three labels appears at least once across my test inputs, in every trial.",
        "criterion": 3,
        "texts": [
            # one human, one unsure, one ai. You can use the same text as in other scenarios if
            "Regular exercise offers numerous benefits for both physical and mental health. It strengthens the heart, improves circulation, and helps maintain a healthy weight. In addition, physical activity releases endorphins, which can reduce stress and improve overall mood. Experts recommend at least 150 minutes of moderate exercise per week for adults. By incorporating activities such as walking, swimming, or cycling into a daily routine, individuals can significantly improve their quality of life.",
            "The importance of sleep is often overlooked. Most adults need seven to nine hours a night, but plenty of us get way less — me included, especially during finals. Poor sleep affects memory, focus, and even your immune system. I used to think I could just push through on coffee. Turns out that's not really how it works.",
            "ok so my car died on the highway yesterday. Right in the middle lane!! Sat there forty minutes with hazards blinking while semis blew past, rattling the mirrors. Tow guy rolls up eating a burrito, no joke, salsa on his sleeve. Alternator. $600. Got home and Pickles, my cat, couldn't have cared less — she just yelled at her empty bowl.",
        ],
    },

    # ── CRITERION 4 — missing / bad text ───────────────────────────────────
    # "For all missing text messages, all will return an error code other than
    #  500 and a JSON error message will be given."
    #
    # Raw request bodies, sent exactly as written. No writing needed here.
    # Verdict: every one returns a 4xx (not 500) with an "error" in the JSON,
    # in every trial.
    {
        "name": "C4: For all missing text messages, all will return an error code other than 500 and a JSON error message will be given.",
        "criterion": 4,
        "bodies": [
            {"creator_id": "eval_c4_missing"},                    # no text field
            {"text": "", "creator_id": "eval_c4_empty"},          # empty string
            {"text": "   \n\t ", "creator_id": "eval_c4_blank"},  # whitespace only
            {"text": None, "creator_id": "eval_c4_null"},         # null
        ],
    },

    # ── CRITERION 5 — unsure answers explain themselves ─────────────────────
    # "For all unsure answers, a reason for why the message is labeled as
    #  unsure will be given."
    #
    # Borderline texts that should land in the unsure band. Verdict: every
    # response with guess == "unsure" has a label that gives a reason, in
    # every trial. (If one of these comes back ai/human instead, it doesn't
    # count for or against — note it.)
    {
        "name": "C5: For all unsure answers, a reason for why the message is labeled as unsure will be given.",
        "criterion": 5,
        "texts": [
            "Time management is one of the most valuable skills a student can develop. It helps reduce stress and improves academic performance. I'm not great at it myself, honestly — last semester I wrote two essays the night before they were due. Using a planner or a simple to-do list can make a big difference. Breaking large assignments into smaller steps also helps keep things manageable.",
            "Social media has good and bad sides. On one hand it helps people stay connected with friends and family who live far away. On the other hand it can be really distracting and sometimes makes people feel bad about themselves. I think the key is balance. If you use it in moderation it can be a useful tool, but you have to be careful not to let it take over your life.",
            "My first job was bagging groceries at a store down the street, and on day one I put a carton of eggs under a watermelon. The customer was not thrilled. Looking back, that job taught me several important lessons. It showed me the value of responsibility, the importance of paying attention to detail, and how to communicate effectively with customers.",
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
