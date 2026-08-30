# US WARN Act Layoff Notices — normalized, daily-updated dataset

**10,073 layoff notices since 2024 · 24 states · one clean schema · CSV + JSON · updated 2026-08-30**

Every US state publishes WARN Act layoff notices differently — different sites,
formats, column names, and date conventions. This repo normalizes them into one
deduplicated dataset, refreshed daily.

## Get the data

- CSV: [`data/warn_notices.csv`](data/warn_notices.csv)
- JSON: [`data/warn_notices.json`](data/warn_notices.json)
- Coverage/freshness metadata: [`data/coverage.json`](data/coverage.json)
- Per-state CSVs: [`data/by-state/`](data/by-state/) — see table below
- Stats page: https://approj.github.io/warn-act-notices/

No login, no API key. Scope of the free dataset, stated plainly: notices from
**2024-01-01** onward, **48h-delayed** (newly scraped notices appear here 48 hours
after our pipeline first sees them). The full archive back to 1988
(34,872 notices) and the zero-delay feed are the commercial products
that fund the pipeline.

## Schema

| Field | Meaning |
|---|---|
| `id` | stable dedupe hash of (state, company, effective_date, employees) |
| `state` | 2-letter postal code |
| `company` | employer name as published by the state |
| `location` | city/county/address, best effort |
| `employees_affected` | integer count, empty if the state omitted it |
| `notice_date` | ISO date the notice was received/posted |
| `effective_date` | ISO date the layoff/closure takes effect |
| `notice_type` | layoff/closure label as published |
| `first_seen` | UTC timestamp our pipeline first saw this notice |

## Coverage

| State | Notices | CSV | Source status |
|---|---:|---|---|
| Arizona (AZ) | 605 | [az.csv](data/by-state/az.csv) | ok |
| California (CA) | 16,526 | [ca.csv](data/by-state/ca.csv) | ok |
| Connecticut (CT) | 27 | [ct.csv](data/by-state/ct.csv) | ok |
| Iowa (IA) | 415 | [ia.csv](data/by-state/ia.csv) | ok |
| Illinois (IL) | 4,032 | [il.csv](data/by-state/il.csv) | ok |
| Indiana (IN) | 1,180 | [in.csv](data/by-state/in.csv) | ok |
| Kansas (KS) | 686 | — | ok |
| Kentucky (KY) | 804 | [ky.csv](data/by-state/ky.csv) | ok |
| Maryland (MD) | 1,273 | [md.csv](data/by-state/md.csv) | ok |
| Michigan (MI) | 112 | — | ok |
| Montana (MT) | 46 | [mt.csv](data/by-state/mt.csv) | ok |
| Nebraska (NE) | 845 | [ne.csv](data/by-state/ne.csv) | ok |
| New Jersey (NJ) | 2,320 | [nj.csv](data/by-state/nj.csv) | ok |
| New York (NY) | 141 | [ny.csv](data/by-state/ny.csv) | ok |
| Oklahoma (OK) | 169 | [ok.csv](data/by-state/ok.csv) | ok |
| Oregon (OR) | 1,363 | [or.csv](data/by-state/or.csv) | ok |
| Rhode Island (RI) | 126 | [ri.csv](data/by-state/ri.csv) | ok |
| South Carolina (SC) | 601 | [sc.csv](data/by-state/sc.csv) | ok |
| South Dakota (SD) | 80 | [sd.csv](data/by-state/sd.csv) | ok |
| Tennessee (TN) | 1,060 | [tn.csv](data/by-state/tn.csv) | ok |
| Utah (UT) | 282 | [ut.csv](data/by-state/ut.csv) | ok |
| Vermont (VT) | 70 | [vt.csv](data/by-state/vt.csv) | ok |
| Washington (WA) | 1,492 | [wa.csv](data/by-state/wa.csv) | ok |
| Wisconsin (WI) | 617 | [wi.csv](data/by-state/wi.csv) | ok |

Each state also ships as its own CSV in [`data/by-state/`](data/by-state/) —
e.g. California layoff notices: [`data/by-state/ca.csv`](data/by-state/ca.csv).

## Monthly trend (last 12 months, this dataset)

| Month | Notices | Workers affected |
|---|---:|---:|
| 2025-09 | 166 | 18,603 |
| 2025-10 | 295 | 29,830 |
| 2025-11 | 218 | 13,214 |
| 2025-12 | 78 | 6,757 |
| 2026-01 | 252 | 20,992 |
| 2026-02 | 200 | 14,293 |
| 2026-03 | 220 | 12,956 |
| 2026-04 | 263 | 15,244 |
| 2026-05 | 215 | 29,077 |
| 2026-06 | 208 | 11,801 |
| 2026-07 | 147 | 11,080 |
| 2026-08 | 130 | 9,196 |

More states are added as their sources are verified. Some states publish
incomplete fields (e.g. NJ omits notice dates); we normalize what exists and
never invent values.

## Real-time feed & full history (commercial)

If you use layoff notices as sales/recruiting triggers, the 48h delay is the
expensive part. Commercial options:

- **[Real-time feed — $49/mo](https://approj.gumroad.com/l/warn-realtime)** — the same dataset with zero
  delay, including notices seen in the last 48h, refreshed on every pipeline
  run. Delivered as a private GitHub repo you can pull/watch.
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice
  we have back to 1988 (34,872 rows, all 24 states), CSV + JSON.

Delivery is automatic: enter your GitHub username at checkout and you're
invited to the private repo. Questions first? [Open an issue](https://github.com/APProj/warn-act-notices/issues)
with the label `commercial`.

## Sources & attribution

Data originates from official state labor department WARN listings. Collection
uses the excellent Apache-2.0 [biglocalnews/warn-scraper](https://github.com/biglocalnews/warn-scraper)
(Stanford Big Local News) plus our own normalization, dedup, and freshness
layer. This project is not affiliated with Big Local News or any state agency.

## License & disclaimer

Dataset (this repo's `data/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) —
use it for anything, credit "WARN Feed (https://github.com/APProj/warn-act-notices)".

Best-effort normalization of public records. States amend and correct notices;
verify against the official state source before relying on any single row.
