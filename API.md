# Using WARN Feed as a free layoffs API (no key, no login)

Every file in this repo is served over plain HTTPS with stable URLs. If you
need US WARN Act layoff notices in a script, dashboard, spreadsheet or LLM
agent, you can treat these raw URLs as a read-only API. No API key, no rate
paperwork, CC BY 4.0 (credit "WARN Feed", link this repo).

**Freshness contract:** data refreshes daily; the free tier is 48h-delayed and
covers 2024-present. Zero-delay + full 1988+ history are the
[paid tiers](#zero-delay--full-history) that fund the pipeline.

## Endpoints (stable raw URLs)

| What | URL |
|---|---|
| All notices (CSV) | `https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/warn_notices.csv` |
| All notices (JSON array) | `https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/warn_notices.json` |
| One state (CSV) | `https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/by-state/ca.csv` (any covered state's 2-letter code) |
| Coverage + freshness metadata | `https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/coverage.json` |
| Monthly trends, last 24 months | `https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/trends.json` |
| Newly added, last 7 days (CSV) | `https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/latest.csv` |
| Newly added, last 7 days (JSON + metadata) | `https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/latest.json` |
| New-notice RSS feed | `https://approj.github.io/warn-act-notices/feed.xml` |

`latest.json` carries `count` and `generated_at`, so an alerting script can poll
it daily and act only when `count` changes — the cheapest possible "new layoff
notices" trigger. It is empty when no rows cleared the 48h delay window in the
last 7 days (the paid real-time tier has no delay).

Schema for every record is documented in the [README](README.md#schema) and in
machine-readable form in [`datapackage.json`](datapackage.json).

## Examples

**curl + jq — latest 5 notices:**

```bash
curl -s https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/warn_notices.json \
  | jq 'sort_by(.notice_date) | reverse | .[:5] | .[] | {state, company, employees_affected, notice_date}'
```

**Python / pandas — layoffs by state since June:**

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/warn_notices.csv")
recent = df[df.notice_date >= "2026-06-01"]
print(recent.groupby("state").employees_affected.sum().sort_values(ascending=False))
```

**Google Sheets:**

```
=IMPORTDATA("https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/by-state/ca.csv")
```

**Watch for new notices (RSS):** point any feed reader or automation
(Slack RSS app, Zapier, n8n) at
`https://approj.github.io/warn-act-notices/feed.xml`.

## Notes & fair use

- Raw URLs are served by GitHub's CDN; cache on your side and please don't
  poll more than hourly — the dataset changes at most daily.
- `coverage.json` tells you programmatically which states are covered and how
  fresh each source is — check it before assuming a state is included.
- States amend notices; treat single rows as best-effort public records.

## Zero-delay & full history

If layoff notices are a sales/recruiting trigger for you, the 48h delay is the
expensive part:

- **[Real-time feed — $49/mo](https://approj.gumroad.com/l/warn-realtime)** — zero delay, refreshed every
  pipeline run, delivered as a private GitHub repo you can pull or watch.
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice back
  to 1988, all covered states, CSV + JSON.
