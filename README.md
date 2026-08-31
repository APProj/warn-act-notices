# US WARN Act Layoff Notices — normalized, daily-updated dataset

**6,729 layoff notices since 2024 · 29 states · one clean schema · CSV + JSON · updated 2026-08-31**

Every US state publishes WARN Act layoff notices differently — different sites,
formats, column names, and date conventions. This repo normalizes them into one
deduplicated dataset, refreshed daily.

## Get the data

- CSV: [`data/warn_notices.csv`](data/warn_notices.csv)
- JSON: [`data/warn_notices.json`](data/warn_notices.json)
- Coverage/freshness metadata: [`data/coverage.json`](data/coverage.json)
- Per-state CSVs: [`data/by-state/`](data/by-state/) — see table below
- Stats page: https://approj.github.io/warn-act-notices/
- RSS feed of newly-published notices: https://approj.github.io/warn-act-notices/feed.xml (48h-delayed)
- Weekly summaries (biggest layoffs, per-state totals, one page per week): https://approj.github.io/warn-act-notices/weekly/
- Monthly summaries (current month updates daily): https://approj.github.io/warn-act-notices/monthly/
- Browse layoffs by employer: https://approj.github.io/warn-act-notices/employers/
- Use it as a free layoffs API (stable raw URLs, curl/pandas/Sheets examples): [API.md](API.md)
- Machine-readable schema: [`datapackage.json`](datapackage.json) · Cite this dataset: [`CITATION.cff`](CITATION.cff) · License: [CC BY 4.0](LICENSE)

No login, no API key. Scope of the free dataset, stated plainly: notices from
**2024-01-01** onward, **48h-delayed** (newly scraped notices appear here 48 hours
after our pipeline first sees them). The full archive back to 1988
(40,257 notices) and the zero-delay feed are the commercial products
that fund the pipeline.

## Schema

| Field | Meaning |
|---|---|
| `id` | stable dedupe hash of (state, company, effective_date, employees) |
| `state` | 2-letter postal code |
| `company` | employer name as published by the state |
| `company_canonical` | cleaned employer name: legal suffixes (Inc/LLC/Corp), store numbers and site tails stripped, casing fixed — groups the same employer across states and renotices |
| `company_dba` | trade name when the state published a "dba"/"aka" alias |
| `location` | city/county/address, best effort |
| `employees_affected` | integer count, empty if the state omitted it |
| `notice_date` | ISO date the notice was received/posted |
| `effective_date` | ISO date the layoff/closure takes effect |
| `notice_type` | layoff/closure label as published |
| `first_seen` | UTC timestamp our pipeline first saw this notice |

## Coverage

| State | Notices | CSV | Source status |
|---|---:|---|---|
| [Arizona](https://approj.github.io/warn-act-notices/states/arizona.html) (AZ) | 636 | [az.csv](data/by-state/az.csv) | ok |
| [California](https://approj.github.io/warn-act-notices/states/california.html) (CA) | 16,526 | [ca.csv](data/by-state/ca.csv) | ok |
| [Colorado](https://approj.github.io/warn-act-notices/states/colorado.html) (CO) | 835 | — | ok |
| [Connecticut](https://approj.github.io/warn-act-notices/states/connecticut.html) (CT) | 27 | [ct.csv](data/by-state/ct.csv) | ok |
| [Florida](https://approj.github.io/warn-act-notices/states/florida.html) (FL) | 3,115 | — | ok |
| [Georgia](https://approj.github.io/warn-act-notices/states/georgia.html) (GA) | 281 | — | ok |
| [Iowa](https://approj.github.io/warn-act-notices/states/iowa.html) (IA) | 415 | [ia.csv](data/by-state/ia.csv) | ok |
| [Illinois](https://approj.github.io/warn-act-notices/states/illinois.html) (IL) | 4,842 | [il.csv](data/by-state/il.csv) | ok |
| [Indiana](https://approj.github.io/warn-act-notices/states/indiana.html) (IN) | 1,180 | [in.csv](data/by-state/in.csv) | ok |
| [Kansas](https://approj.github.io/warn-act-notices/states/kansas.html) (KS) | 791 | — | ok |
| [Kentucky](https://approj.github.io/warn-act-notices/states/kentucky.html) (KY) | 804 | [ky.csv](data/by-state/ky.csv) | ok |
| [Louisiana](https://approj.github.io/warn-act-notices/states/louisiana.html) (LA) | 38 | — | ok |
| [Maryland](https://approj.github.io/warn-act-notices/states/maryland.html) (MD) | 1,273 | [md.csv](data/by-state/md.csv) | ok |
| [Michigan](https://approj.github.io/warn-act-notices/states/michigan.html) (MI) | 112 | — | ok |
| [Montana](https://approj.github.io/warn-act-notices/states/montana.html) (MT) | 46 | [mt.csv](data/by-state/mt.csv) | ok |
| [Nebraska](https://approj.github.io/warn-act-notices/states/nebraska.html) (NE) | 845 | [ne.csv](data/by-state/ne.csv) | ok |
| [New Jersey](https://approj.github.io/warn-act-notices/states/new-jersey.html) (NJ) | 2,321 | [nj.csv](data/by-state/nj.csv) | ok |
| [New Mexico](https://approj.github.io/warn-act-notices/states/new-mexico.html) (NM) | 116 | — | ok |
| [New York](https://approj.github.io/warn-act-notices/states/new-york.html) (NY) | 141 | [ny.csv](data/by-state/ny.csv) | ok |
| [Oklahoma](https://approj.github.io/warn-act-notices/states/oklahoma.html) (OK) | 219 | [ok.csv](data/by-state/ok.csv) | ok |
| [Oregon](https://approj.github.io/warn-act-notices/states/oregon.html) (OR) | 1,363 | [or.csv](data/by-state/or.csv) | ok |
| [Rhode Island](https://approj.github.io/warn-act-notices/states/rhode-island.html) (RI) | 126 | [ri.csv](data/by-state/ri.csv) | ok |
| [South Carolina](https://approj.github.io/warn-act-notices/states/south-carolina.html) (SC) | 603 | [sc.csv](data/by-state/sc.csv) | ok |
| [South Dakota](https://approj.github.io/warn-act-notices/states/south-dakota.html) (SD) | 80 | [sd.csv](data/by-state/sd.csv) | ok |
| [Tennessee](https://approj.github.io/warn-act-notices/states/tennessee.html) (TN) | 1,060 | [tn.csv](data/by-state/tn.csv) | ok |
| [Utah](https://approj.github.io/warn-act-notices/states/utah.html) (UT) | 282 | [ut.csv](data/by-state/ut.csv) | ok |
| [Vermont](https://approj.github.io/warn-act-notices/states/vermont.html) (VT) | 70 | [vt.csv](data/by-state/vt.csv) | ok |
| [Washington](https://approj.github.io/warn-act-notices/states/washington.html) (WA) | 1,493 | [wa.csv](data/by-state/wa.csv) | ok |
| [Wisconsin](https://approj.github.io/warn-act-notices/states/wisconsin.html) (WI) | 617 | [wi.csv](data/by-state/wi.csv) | ok |

Each state also ships as its own CSV in [`data/by-state/`](data/by-state/) —
e.g. California layoff notices: [`data/by-state/ca.csv`](data/by-state/ca.csv).

## Biggest layoff notices — 2026-08

| Company | State | Location | Workers | Notice date |
|---|---|---|---:|---|
| Tyson Foods | IL | Hillsdale, 28424 38TH Ave. North | 2,495 | 2026-08-13 |
| Borton & Sons | WA | Yakima, Zillah, Pasco, Burbank, Prescott, Soap Lake, Othello, Mesa | 928 | 2026-08-21 |
| Tyson Fresh Meats | UT | Eagle Mountain | 723 | 2026-08-13 |
| Essendant | IL | Lincolnshire, 200 Tri-State Dr., Suite 400 | 510 | 2026-08-03 |
| Sky Chefs | NY | Queens | 471 | 2026-08-04 |
| Jabil | CA | Santa Clara County | 382 | 2026-08-21 |
| Grocery Delivery E-Services | NJ | Swedesboro | 374 | 2026-08-01 |
| Amentum | MD | 7710 Milestone Parkway Hanover, MD 21076 | 317 | 2026-08-18 |
| TikTok USDS JV | TN | Davidson | 250 | 2026-08-05 |
| Starbucks | WA | Seattle | 224 | 2026-08-20 |
| LeeMAH Electronics | CA | San Mateo County | 205 | 2026-08-17 |
| Bumble Bee Foods | CA | Los Angeles County | 197 | 2026-08-11 |
| Postal Center International | IN | Brownsburg | 151 | 2026-08-13 |
| LAZ Parking California (9610 Sky Way) | CA | Los Angeles County | 139 | 2026-08-06 |
| Gerresheimer | NJ | Vineland | 139 | 2026-08-01 |

## Monthly trend (last 12 months, this dataset)

| Month | Notices | Workers affected |
|---|---:|---:|
| 2025-09 | 188 | 21,540 |
| 2025-10 | 321 | 32,553 |
| 2025-11 | 230 | 15,889 |
| 2025-12 | 90 | 8,159 |
| 2026-01 | 273 | 23,859 |
| 2026-02 | 225 | 18,862 |
| 2026-03 | 238 | 14,514 |
| 2026-04 | 278 | 17,968 |
| 2026-05 | 234 | 32,674 |
| 2026-06 | 233 | 14,514 |
| 2026-07 | 164 | 12,746 |
| 2026-08 | 147 | 13,513 |

Machine-readable trends (per-state monthly notices + workers affected, last 24
months): [`data/trends.json`](data/trends.json) — stable raw URL for embedding
in dashboards/articles:
`https://raw.githubusercontent.com/APProj/warn-act-notices/main/data/trends.json`
(CC BY 4.0, credit "WARN Feed").

More states are added as their sources are verified. Some states publish
incomplete fields; we normalize what exists and never invent values. Precision
note: NJ publishes only the posting month, so NJ `notice_date` is month
precision (day pinned to 01, year inferred from the effective date). IL
`notice_date` is the earliest notification on record; amended IL notices carry
the latest revised headcount.

## Real-time feed & full history (commercial)

If you use layoff notices as sales/recruiting triggers, the 48h delay is the
expensive part. Commercial options:

- **[Real-time feed — $49/mo](https://approj.gumroad.com/l/warn-realtime)** — the same dataset with zero
  delay, including notices seen in the last 48h, refreshed on every pipeline
  run. Delivered as a private GitHub repo you can pull/watch.
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice
  we have back to 1988 (40,257 rows, all 29 states), CSV + JSON.

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
