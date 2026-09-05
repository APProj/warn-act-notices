# Using WARN Feed as a free layoffs API (no key, no login)

Every file in this repo is served over plain HTTPS with stable URLs. If you
need US WARN Act layoff notices in a script, dashboard, spreadsheet or LLM
agent, you can treat these raw URLs as a read-only API. No API key, no rate
paperwork, CC BY 4.0 (credit "WARN Feed", link this repo).

**Freshness contract:** data refreshes daily; the free tier carries no delay and
covers 2024-present. Per-customer WARN Watch alerts + full 1988+ history are the
[paid tiers](#zero-delay--full-history) that fund the pipeline.

## Endpoints (stable raw URLs)

| What | URL |
|---|---|
| All notices (CSV) | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/warn_notices.csv` |
| All notices (JSON array) | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/warn_notices.json` |
| One state (CSV) | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/by-state/ca.csv` (any covered state's 2-letter code) |
| Coverage + freshness metadata | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/coverage.json` |
| Monthly trends, last 24 months | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/trends.json` |
| Newly added, last 7 days (CSV) | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/latest.csv` |
| Newly added, last 7 days (JSON + metadata) | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/latest.json` |
| Daily snapshot as a GitHub Release (always the newest; same files, versioned by date) | `https://github.com/APVentureEngine/warn-act-notices/releases/latest/download/warn_notices.csv` — also `warn_notices.json`, `latest.csv`, `coverage.json`; every release lists the biggest notices of the fortnight in its notes |
| New-notice RSS feed | `https://approjects-warn-act-notices.static.hf.space/feed.xml` |
| Live badge: current-year layoffs (shields.io endpoint) | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/badge.json` |
| Live badge: data freshness (shields.io endpoint) | `https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/badge-updated.json` |

`latest.json` carries `count` and `generated_at`, so an alerting script can poll
it daily and act only when `count` changes — the cheapest possible "new layoff
notices" trigger. It is empty when no new notices were published in the
last 7 days.

Schema for every record is documented in the [README](README.md#schema) and in
machine-readable form in [`datapackage.json`](datapackage.json).

## Examples

**curl + jq — latest 5 notices:**

```bash
curl -s https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/warn_notices.json \
  | jq 'sort_by(.notice_date) | reverse | .[:5] | .[] | {state, company, employees_affected, notice_date}'
```

**Python / pandas — layoffs by state since June:**

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/warn_notices.csv")
recent = df[df.notice_date >= "2026-06-01"]
print(recent.groupby("state").employees_affected.sum().sort_values(ascending=False))
```

**Google Sheets:**

```
=IMPORTDATA("https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/by-state/ca.csv")
```

**Watch for new notices (RSS):** point any feed reader or automation
(Slack RSS app, Zapier, n8n) at
`https://approjects-warn-act-notices.static.hf.space/feed.xml`.

**Watch `latest.csv` for a specific employer or state (cron + curl, no dependencies):**

```bash
# Runs once a day; prints only rows that are new since the last run AND match your terms.
# Edit TERMS (regex, case-insensitive) — employer names, or a state code like ',TX,'.
TERMS='amazon|tesla|,TX,'
URL=https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/latest.csv
curl -s "$URL" -o /tmp/warn_latest.csv
touch /tmp/warn_seen.csv
grep -iE "$TERMS" /tmp/warn_latest.csv | grep -vxFf /tmp/warn_seen.csv \
  | tee -a /tmp/warn_seen.csv \
  | cut -d, -f2-4,6,8    # state, company, canonical name, employees, notice date
```

Put that in `crontab -e` as `15 9 * * * /path/to/warn_watch.sh | mail -s "WARN hits" you@example.com`
and you have a free alerting loop. If you would rather not run cron, [WARN Watch](https://approjects-warn-act-notices.static.hf.space/watch.html)
does exactly this match on every refresh and pushes hits to a private page, RSS, and a
Slack / Discord / Teams webhook — [30-day free trial, 3 employers or 1 state, no card](https://approj.gumroad.com/l/warn-free-watch).

## Live badges

Put a self-updating US layoffs counter in your own README, docs page, or
dashboard. These are standard [shields.io endpoint badges](https://shields.io/badges/endpoint-badge)
fed by this repo's data files, so they re-render automatically after every
daily refresh — no code on your side.

**Current-year running total** (notices + workers affected, matches
[yearly](https://approjects-warn-act-notices.static.hf.space/yearly/index.html)):

```markdown
[![US WARN layoffs](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPProj%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge.json)](https://github.com/APVentureEngine/warn-act-notices)
```

**Data freshness** (date of the last refresh):

```markdown
[![layoff data updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPProj%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge-updated.json)](https://github.com/APVentureEngine/warn-act-notices)
```

Both examples link the badge back here (CC BY credit satisfied); point the link
wherever you like as long as attribution appears somewhere. For custom styling
pass any extra shields parameters (`&style=flat-square`, `&logo=github`, …).

## Notes & fair use

- Raw URLs are served by GitHub's CDN; cache on your side and please don't
  poll more than hourly — the dataset changes at most daily.
- `coverage.json` tells you programmatically which states are covered and how
  fresh each source is — check it before assuming a state is included.
- States amend notices; treat single rows as best-effort public records.

## Zero-delay & full history

The free files carry no delay. If you only care about certain employers or states:

- **[WARN Watch — $49/year](https://approjects-warn-act-notices.static.hf.space/watch.html)** — up to 25 employer terms + whole-state
  watches matched on every refresh for a year; private alert page + RSS, no login.
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice back
  to 1988, all covered states, CSV + JSON.
