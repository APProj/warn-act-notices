# US WARN Act Layoff Notices — normalized, daily-updated dataset

[![US WARN layoffs 2026](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge.json)](https://apventureengine.github.io/warn-act-notices/yearly/) [![data updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge-updated.json)](https://github.com/APVentureEngine/warn-act-notices/commits/main) — live, embeddable: [get these badges](API.md#live-badges)

**7,099 layoff notices since 2024 · 39 states · one clean schema · CSV + JSON · updated 2026-09-02**

Every US state publishes WARN Act layoff notices differently — different sites,
formats, column names, and date conventions. This repo normalizes them into one
deduplicated dataset, refreshed daily.

## Get the data

- CSV: [`data/warn_notices.csv`](data/warn_notices.csv)
- JSON: [`data/warn_notices.json`](data/warn_notices.json)
- Coverage/freshness metadata: [`data/coverage.json`](data/coverage.json)
- Per-state CSVs: [`data/by-state/`](data/by-state/) — see table below
- **Newly added in the last 7 days:** [`data/latest.csv`](data/latest.csv) / [`data/latest.json`](data/latest.json) — stable raw URLs for "new WARN notices" alerting and dashboards (48h-delayed; real-time tier available)
- Stats page: https://apventureengine.github.io/warn-act-notices/
- RSS feed of newly-published notices: https://apventureengine.github.io/warn-act-notices/feed.xml (48h-delayed)
- Per-state RSS feeds (one state per feed — pipe a single state into Slack/Feedly/Zapier): OPML bundle https://apventureengine.github.io/warn-act-notices/feeds/feeds.opml, or `feeds/<state>.xml`, e.g. https://apventureengine.github.io/warn-act-notices/feeds/california.xml
- Weekly summaries (biggest layoffs, per-state totals, one page per week): https://apventureengine.github.io/warn-act-notices/weekly/
- Monthly summaries (current month updates daily): https://apventureengine.github.io/warn-act-notices/monthly/
- Yearly totals (current year is a running total, updated daily): https://apventureengine.github.io/warn-act-notices/yearly/
- Browse layoffs by employer: https://apventureengine.github.io/warn-act-notices/employers/
- Instant employer search (free tier): https://apventureengine.github.io/warn-act-notices/search.html
- How this compares to WARNTracker, Intellizence, warn-scraper & state portals: https://apventureengine.github.io/warn-act-notices/compare.html
- Use it as a free layoffs API (stable raw URLs, curl/pandas/Sheets examples): [API.md](API.md)
- Machine-readable schema: [`datapackage.json`](datapackage.json) · Cite this dataset: [`CITATION.cff`](CITATION.cff) · License: [CC BY 4.0](LICENSE)

No login, no API key. Scope of the free dataset, stated plainly: notices from
**2024-01-01** onward, **48h-delayed** (newly scraped notices appear here 48 hours
after our pipeline first sees them). The full archive back to 1988
(44,906 notices) and the zero-delay feed are the commercial products
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

| State | Rows, full archive (1988→, paid) | Rows in free files (2024→, 48h delay) | CSV | Source status |
|---|---:|---:|---|---|
| [Alaska](https://apventureengine.github.io/warn-act-notices/states/alaska.html) (AK) | 66 | 0 | — | ok |
| [Alabama](https://apventureengine.github.io/warn-act-notices/states/alabama.html) (AL) | 1,060 | 0 | — | ok |
| [Arizona](https://apventureengine.github.io/warn-act-notices/states/arizona.html) (AZ) | 636 | 121 | [az.csv](data/by-state/az.csv) | ok |
| [California](https://apventureengine.github.io/warn-act-notices/states/california.html) (CA) | 16,556 | 3,991 | [ca.csv](data/by-state/ca.csv) | ok |
| [Colorado](https://apventureengine.github.io/warn-act-notices/states/colorado.html) (CO) | 835 | 0 | — | ok |
| [Connecticut](https://apventureengine.github.io/warn-act-notices/states/connecticut.html) (CT) | 27 | 27 | [ct.csv](data/by-state/ct.csv) | ok |
| [District of Columbia](https://apventureengine.github.io/warn-act-notices/states/district-of-columbia.html) (DC) | 143 | 0 | — | ok |
| [Delaware](https://apventureengine.github.io/warn-act-notices/states/delaware.html) (DE) | 100 | 0 | — | ok |
| [Florida](https://apventureengine.github.io/warn-act-notices/states/florida.html) (FL) | 3,115 | 0 | — | ok |
| [Georgia](https://apventureengine.github.io/warn-act-notices/states/georgia.html) (GA) | 282 | 225 | [ga.csv](data/by-state/ga.csv) | ok |
| [Iowa](https://apventureengine.github.io/warn-act-notices/states/iowa.html) (IA) | 416 | 79 | [ia.csv](data/by-state/ia.csv) | ok |
| [Illinois](https://apventureengine.github.io/warn-act-notices/states/illinois.html) (IL) | 4,842 | 346 | [il.csv](data/by-state/il.csv) | ok |
| [Indiana](https://apventureengine.github.io/warn-act-notices/states/indiana.html) (IN) | 1,180 | 260 | [in.csv](data/by-state/in.csv) | ok |
| [Kansas](https://apventureengine.github.io/warn-act-notices/states/kansas.html) (KS) | 791 | 33 | [ks.csv](data/by-state/ks.csv) | ok |
| [Kentucky](https://apventureengine.github.io/warn-act-notices/states/kentucky.html) (KY) | 804 | 38 | [ky.csv](data/by-state/ky.csv) | ok |
| [Louisiana](https://apventureengine.github.io/warn-act-notices/states/louisiana.html) (LA) | 38 | 0 | — | ok |
| [Maryland](https://apventureengine.github.io/warn-act-notices/states/maryland.html) (MD) | 1,274 | 328 | [md.csv](data/by-state/md.csv) | ok |
| [Maine](https://apventureengine.github.io/warn-act-notices/states/maine.html) (ME) | 85 | 0 | — | ok |
| [Michigan](https://apventureengine.github.io/warn-act-notices/states/michigan.html) (MI) | 112 | 112 | [mi.csv](data/by-state/mi.csv) | ok |
| [Mississippi](https://apventureengine.github.io/warn-act-notices/states/mississippi.html) (MS) | 136 | 0 | — | ok |
| [Montana](https://apventureengine.github.io/warn-act-notices/states/montana.html) (MT) | 46 | 18 | [mt.csv](data/by-state/mt.csv) | ok |
| [North Carolina](https://apventureengine.github.io/warn-act-notices/states/north-carolina.html) (NC) | 294 | 0 | — | ok |
| [Nebraska](https://apventureengine.github.io/warn-act-notices/states/nebraska.html) (NE) | 845 | 29 | [ne.csv](data/by-state/ne.csv) | ok |
| [New Jersey](https://apventureengine.github.io/warn-act-notices/states/new-jersey.html) (NJ) | 2,321 | 311 | [nj.csv](data/by-state/nj.csv) | ok |
| [New Mexico](https://apventureengine.github.io/warn-act-notices/states/new-mexico.html) (NM) | 116 | 0 | — | ok |
| [New York](https://apventureengine.github.io/warn-act-notices/states/new-york.html) (NY) | 141 | 141 | [ny.csv](data/by-state/ny.csv) | ok |
| [Oklahoma](https://apventureengine.github.io/warn-act-notices/states/oklahoma.html) (OK) | 219 | 29 | [ok.csv](data/by-state/ok.csv) | ok |
| [Oregon](https://apventureengine.github.io/warn-act-notices/states/oregon.html) (OR) | 1,369 | 196 | [or.csv](data/by-state/or.csv) | ok |
| [Pennsylvania](https://apventureengine.github.io/warn-act-notices/states/pennsylvania.html) (PA) | 308 | 0 | — | ok |
| [Rhode Island](https://apventureengine.github.io/warn-act-notices/states/rhode-island.html) (RI) | 126 | 27 | [ri.csv](data/by-state/ri.csv) | ok |
| [South Carolina](https://apventureengine.github.io/warn-act-notices/states/south-carolina.html) (SC) | 603 | 134 | [sc.csv](data/by-state/sc.csv) | ok |
| [South Dakota](https://apventureengine.github.io/warn-act-notices/states/south-dakota.html) (SD) | 80 | 16 | [sd.csv](data/by-state/sd.csv) | ok |
| [Tennessee](https://apventureengine.github.io/warn-act-notices/states/tennessee.html) (TN) | 1,060 | 97 | [tn.csv](data/by-state/tn.csv) | ok |
| [Texas](https://apventureengine.github.io/warn-act-notices/states/texas.html) (TX) | 2,358 | 0 | — | ok |
| [Utah](https://apventureengine.github.io/warn-act-notices/states/utah.html) (UT) | 282 | 51 | [ut.csv](data/by-state/ut.csv) | ok |
| [Vermont](https://apventureengine.github.io/warn-act-notices/states/vermont.html) (VT) | 70 | 16 | [vt.csv](data/by-state/vt.csv) | ok |
| [Washington](https://apventureengine.github.io/warn-act-notices/states/washington.html) (WA) | 1,495 | 273 | [wa.csv](data/by-state/wa.csv) | ok |
| [Wisconsin](https://apventureengine.github.io/warn-act-notices/states/wisconsin.html) (WI) | 617 | 201 | [wi.csv](data/by-state/wi.csv) | ok |
| [West Virginia](https://apventureengine.github.io/warn-act-notices/states/west-virginia.html) (WV) | 58 | 0 | — | ok |

**Not covered (12 states):** Arkansas (agency site blocks automated access), Hawaii (agency page unparseable (obfuscated links)), Idaho (agency PDF is corrupt), Massachusetts (agency site blocks automated access), Minnesota (agency site blocks automated access), Missouri (agency site blocks automated access), Nevada (agency site blocks automated access), New Hampshire (agency site blocks automated access), North Dakota (no public WARN listing located), Ohio (listing is a browser-only app, no data endpoint), Virginia (listing is a browser-only app, no data endpoint), Wyoming (WARN filings are non-public by state statute). We do not guess or
backfill these from third parties; if a state opens a public listing it is added.

## What normalization actually does

State portals spell the same employer many ways (store numbers, site tails,
suffixes, ALL CAPS). `company_canonical` collapses them so you can count and
watch an employer across states and years — the part no raw scraper output gives you:

- **Kaiser Foundation Hospitals** ← 27 raw spellings, e.g. `Kaiser Foundation Hospitals`; `Kaiser Foundation Hospitals (1100)`; `Kaiser Foundation Hospitals (12254)`; `Kaiser Foundation Hospitals (1450)`
- **Southern PacPizza** ← 25 raw spellings, e.g. `Southern PacPizza dba Pizza Hut - 029197`; `Southern PacPizza dba Pizza Hut - 029198`; `Southern PacPizza dba Pizza Hut - 029199`; `Southern PacPizza dba Pizza Hut - 029200`
- **Good Sports Plus** ← 12 raw spellings, e.g. `Good Sports Plus Ltd, dba Arc Phil D. Swing Elementary School`; `Good Sports Plus Ltd. dba Arc`; `Good Sports Plus Ltd. dba Arc - Central Union High School`; `Good Sports Plus Ltd. dba Arc - Desert Valley High School`

Each state also ships as its own CSV in [`data/by-state/`](data/by-state/) —
e.g. California layoff notices: [`data/by-state/ca.csv`](data/by-state/ca.csv).

## Biggest layoff notices — 2026-08

| Company | State | Location | Workers | Notice date |
|---|---|---|---:|---|
| Tyson Foods | IL | Hillsdale, 28424 38TH Ave. North | 2,495 | 2026-08-13 |
| Borton & Sons | WA | Yakima, Zillah, Pasco, Burbank, Prescott, Soap Lake, Othello, Mesa | 928 | 2026-08-21 |
| Wellstar Health System | GA | Sawyer Rd Marietta, Cobb County | 761 | 2026-08-03 |
| Tyson Fresh Meats | UT | Eagle Mountain | 723 | 2026-08-13 |
| Essendant | IL | Lincolnshire, 200 Tri-State Dr., Suite 400 | 510 | 2026-08-03 |
| Sky Chefs | NY | Queens | 471 | 2026-08-04 |
| Jabil | CA | Santa Clara County | 382 | 2026-08-21 |
| Grocery Delivery E-Services | NJ | Swedesboro | 374 | 2026-08-01 |
| Republic National Distributing | GA | National Dr SW Atlanta, Cobb County | 321 | 2026-08-26 |
| Amentum | MD | 7710 Milestone Parkway Hanover, MD 21076 | 317 | 2026-08-18 |
| TikTok USDS JV | TN | Davidson | 250 | 2026-08-05 |
| Starbucks | WA | Seattle | 224 | 2026-08-20 |
| LeeMAH Electronics | CA | San Mateo County | 205 | 2026-08-17 |
| Bumble Bee Foods | CA | Los Angeles County | 197 | 2026-08-11 |
| Essendant | GA | Horizon Dr Suwanee | 192 | 2026-08-04 |

## Monthly trend (last 12 months, this dataset)

| Month | Notices | Workers affected |
|---|---:|---:|
| 2025-09 | 191 | 22,187 |
| 2025-10 | 332 | 36,655 |
| 2025-11 | 240 | 17,030 |
| 2025-12 | 95 | 8,654 |
| 2026-01 | 285 | 25,743 |
| 2026-02 | 243 | 20,357 |
| 2026-03 | 246 | 16,644 |
| 2026-04 | 281 | 18,172 |
| 2026-05 | 244 | 34,886 |
| 2026-06 | 238 | 14,925 |
| 2026-07 | 168 | 13,173 |
| 2026-08 | 159 | 15,744 |

Machine-readable trends (per-state monthly notices + workers affected, last 24
months): [`data/trends.json`](data/trends.json) — stable raw URL for embedding
in dashboards/articles:
`https://raw.githubusercontent.com/APVentureEngine/warn-act-notices/main/data/trends.json`
(CC BY 4.0, credit "WARN Feed").

More states are added as their sources are verified. Some states publish
incomplete fields; we normalize what exists and never invent values. Precision
note: NJ publishes only the posting month, so NJ `notice_date` is month
precision (day pinned to 01, year inferred from the effective date). IL
`notice_date` is the earliest notification on record; amended IL notices carry
the latest revised headcount.

## Real-time feed & full history (commercial)

If you use layoff notices as sales/recruiting triggers, the 48h delay is the
expensive part. As of 2026-09-02: **108 notices** affecting 9,735 workers (dated in the last 45 days, 17 states) are in the real-time feed and not yet in this repo's free files — each lands here only after its 48-hour delay. Machine-readable: `delay_gap` in [`data/coverage.json`](data/coverage.json).

Commercial options:

- **[Real-time feed — $49/mo](https://approj.gumroad.com/l/warn-realtime)** — the same dataset with zero
  delay, including notices seen in the last 48h, refreshed on every pipeline
  run. Delivered as a private GitHub repo you can pull/watch.
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice
  we have back to 1988 (44,906 rows, all 39 states), CSV + JSON.

Delivery is automatic: enter your GitHub username at checkout and you're
invited to the private repo. Questions first? [Open an issue](https://github.com/APVentureEngine/warn-act-notices/issues)
with the label `commercial`.

## Sources & attribution

Data originates from official state labor department WARN listings. Collection
uses the excellent Apache-2.0 [biglocalnews/warn-scraper](https://github.com/biglocalnews/warn-scraper)
(Stanford Big Local News) plus our own normalization, dedup, and freshness
layer. This project is not affiliated with Big Local News or any state agency.

## License & disclaimer

Dataset (this repo's `data/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) —
use it for anything, credit "WARN Feed (https://github.com/APVentureEngine/warn-act-notices)".

Best-effort normalization of public records. States amend and correct notices;
verify against the official state source before relying on any single row.
