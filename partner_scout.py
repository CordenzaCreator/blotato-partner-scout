#!/usr/bin/env python3
"""
Partner Scout — a tiny partner sourcing automation, built from scratch.

What it does:
  1. Reads a CSV of creators/agencies found in public (name, platform, niche,
     followers, posts_about_ai_automation, has_business_audience, contact).
  2. Scores each one for partner fit (0-100) with plain, explainable rules.
  3. Writes a ranked shortlist CSV and one personal outreach draft per
     A-tier candidate. Drafts only — a human approves before anything sends.

Run:  python3 partner_scout.py creators.csv
Out:  shortlist.csv, outreach/<name>.md
"""
import csv, sys, os

def score(row):
    s = 0
    followers = int(row.get("followers") or 0)
    posts = int(row.get("posts_about_ai_automation") or 0)
    if followers >= 100_000: s += 25
    elif followers >= 25_000: s += 20
    elif followers >= 5_000: s += 12
    elif followers >= 1_000: s += 6
    s += min(posts * 5, 30)                       # proof they already teach this
    if (row.get("has_business_audience") or "").lower() == "yes": s += 25
    if (row.get("sells_services") or "").lower() == "yes": s += 10  # agency/freelancer = clients to refer
    if row.get("contact"): s += 10               # reachable = actionable
    return s

def tier(s):
    return "A" if s >= 70 else "B" if s >= 45 else "C"

def draft(row, s):
    return f"""Subject: Partner invite for {row['name']}

Hi {row['name'].split()[0]},

Your {row['platform']} content on {row['niche']} is exactly what our partners
succeed with. I run partner sourcing for a content automation program: we give
creators and agencies a referral kit, a live build session, and rewards at each
milestone. First step is one build together, not a pitch call.

Open to a look?

— Jaleel (fit score {s}/100, tier A)
"""

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "creators.csv"
    rows = list(csv.DictReader(open(path)))
    for r in rows:
        r["score"] = score(r); r["tier"] = tier(r["score"])
    rows.sort(key=lambda r: -r["score"])
    with open("shortlist.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    os.makedirs("outreach", exist_ok=True)
    n = 0
    for r in rows:
        if r["tier"] == "A":
            name = r["name"].lower().replace(" ", "_")
            open(f"outreach/{name}.md", "w").write(draft(r, r["score"])); n += 1
    print(f"Scored {len(rows)} candidates. A-tier: {sum(1 for r in rows if r['tier']=='A')}, "
          f"B-tier: {sum(1 for r in rows if r['tier']=='B')}, C-tier: {sum(1 for r in rows if r['tier']=='C')}. "
          f"Wrote shortlist.csv and {n} outreach drafts (human approval required).")

if __name__ == "__main__":
    main()
