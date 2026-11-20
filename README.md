# Blotato Partner Scout

A partner sourcing system for Blotato, built by Jaleel Williams for the Partnerships AI Engineer application. It scores creators and agencies for partner fit, ranks them, and drafts outreach for the top tier only. Drafts only, a human approves before anything sends.

## Principle

Fit over fame. A famous name with the wrong audience is worth less than a smaller creator whose audience already buys content automation tools.

## How it works

1. `creators-real.csv` is the real researched creator list (7 strong fits, 3 contrast picks on purpose).
2. `partner_scout.py` scores each creator out of 100 and writes `shortlist.csv`, ranked high to low.
3. The script writes one outreach draft per A-tier creator into `outreach/`.
4. `outreach-stage4/` holds the human-edited personal drafts, with the specific build or audience hook for each person, and activation wording for the two creators who already carry a Blotato link (Nate Herk, Julian Goldie).

Run it:

```bash
python3 partner_scout.py creators-real.csv
```

## Scoring, out of 100

- Reach: at most 25, tiered (100,000+ = 25, 25,000+ = 20, 5,000+ = 12, 1,000+ = 6)
- Posting about AI or content automation: up to 30, as posts x 5 capped at 30. In the real list, regular posters are coded 3, so they get 15 in this run
- Business or creator audience: 25
- Sells services to clients: 10
- Public contact route: 10

Tiers: A = 70+, B = 45 to 69, C = under 45.

## Result on the real list

7 A tier, 0 B tier, 3 C tier. Nate Herk, Liam Ottley, Nick Saraev, Julian Goldie, and Jack Roberts score 85. AI Andy scores 75. The AI Automators score 70 at only about 67,000 subscribers. MrBeast (527M), Khaby Lame (162.9M), and Gordon Ramsay (19.7M) all score 35, C tier, because reach is only 25 of 100 points.

Full per person notes and sources are in `selected-creators-notes.md`.

## Validation

The scoring code was independently validated by ChatGPT on 2026-11-20. Verdict: SOUND, 0 rule violations, 10 of 10 manual score checks matched. Record: `CHATGPT-VALIDATION-STAGE3.md`. ChatGPT thread: "Validate sourcing script rules".

## Weekly rerun

A weekly scheduled rerun exists in Muse as `blotato-partner-scout-weekly`. It is left turned off until Jaleel says so. Nothing runs, nothing sends, on its own.

## What is not in here

No email addresses were collected or guessed, contact is a public route description only. No outreach was sent. The application recording script and personal application files are not in this repo.
