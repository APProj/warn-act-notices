# US WARN Act Layoff Notices — normalized, daily-updated dataset

**10,115 layoff notices since 2024 · 22 states · one clean schema · CSV + JSON · updated 2026-08-30**

Every US state publishes WARN Act layoff notices differently — different sites,
formats, column names, and date conventions. This repo normalizes them into one
deduplicated dataset, refreshed daily.

## Get the data

- CSV: [`data/warn_notices.csv`](data/warn_notices.csv)
- JSON: [`data/warn_notices.json`](data/warn_notices.json)
- Coverage/freshness metadata: [`data/coverage.json`](data/coverage.json)
- Stats page: https://approj.github.io/warn-act-notices/

No login, no API key. Scope of the free dataset, stated plainly: notices from
**2024-01-01** onward, **48h-delayed** (newly scraped notices appear here 48 hours
after our pipeline first sees them). The full archive back to 1988
(34,087 notices) and the zero-delay feed are the commercial products
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

| State | Notices | Source status |
|---|---:|---|
| Arizona (AZ) | 618 | ok |
| California (CA) | 16,526 | ok |
| Connecticut (CT) | 27 | ok |
| Iowa (IA) | 415 | ok |
| Illinois (IL) | 4,032 | ok |
| Indiana (IN) | 1,180 | ok |
| Kentucky (KY) | 804 | ok |
| Maryland (MD) | 1,273 | ok |
| Montana (MT) | 46 | ok |
| Nebraska (NE) | 845 | ok |
| New Jersey (NJ) | 2,320 | ok |
| New York (NY) | 141 | ok |
| Oklahoma (OK) | 169 | ok |
| Oregon (OR) | 1,363 | ok |
| Rhode Island (RI) | 126 | ok |
| South Carolina (SC) | 601 | ok |
| South Dakota (SD) | 80 | ok |
| Tennessee (TN) | 1,060 | ok |
| Utah (UT) | 282 | ok |
| Vermont (VT) | 70 | ok |
| Washington (WA) | 1,492 | ok |
| Wisconsin (WI) | 617 | ok |

More states are added as their sources are verified. Some states publish
incomplete fields (e.g. NJ omits notice dates); we normalize what exists and
never invent values.

## Real-time feed & full history (commercial)

If you use layoff notices as sales/recruiting triggers, the 48h delay is the
expensive part. Commercial options:

- **Real-time feed** — the same dataset with zero delay, including notices seen
  in the last 48h, refreshed on every pipeline run. Delivered as a private
  GitHub repo you can pull/watch.
- **Full historical archive** — one-time purchase: every notice we have back to
  1988 (34,087 rows, all 22 states), CSV + JSON.

Available at **https://approj.gumroad.com** — or [open an issue](https://github.com/APProj/warn-act-notices/issues) with the
label `commercial` and we'll get you set up.

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
