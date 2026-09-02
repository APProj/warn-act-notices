# US WARN Act Layoff Notices — normalized, daily-updated dataset

[![US WARN layoffs 2026](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge.json)](https://apventureengine.github.io/warn-act-notices/yearly/) [![data updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge-updated.json)](https://github.com/APVentureEngine/warn-act-notices/commits/main) — live, embeddable: [get these badges](API.md#live-badges)

**8,112 layoff notices since 2024 · 39 states · one clean schema · CSV + JSON · updated 2026-09-02**

Every US state publishes WARN Act layoff notices differently — different sites,
formats, column names, and date conventions. This repo normalizes them into one
deduplicated dataset, refreshed daily. More information about the Worker Adjustment and Retraining Notification Act at [Wikipedia](https://en.wikipedia.org/wiki/Worker_Adjustment_and_Retraining_Notification_Act_of_1988).

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
- Hugging Face mirror (same free tier, `load_dataset` / pandas ready, re-uploaded every refresh): [APProjects/us-warn-act-layoffs-daily](https://huggingface.co/datasets/APProjects/us-warn-act-layoffs-daily)
- Machine-readable schema: [`datapackage.json`](datapackage.json) · Cite this dataset: [`CITATION.cff`](CITATION.cff) · License: [CC BY 4.0](LICENSE)

No login, no API key. Scope of the free dataset, stated plainly: notices from
**2024-01-01** onward, **48h-delayed** (newly scraped notices appear here 48 hours
after our pipeline first sees them). The full archive back to 1988
(45,755 notices) and the zero-delay feed are the commercial products
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
| `first_seen` | UTC timestamp our pipeline first saw this notice (for imported history — CT 2010–2025 from the agency's archived annual listings — set to the notice date) |

## Coverage

| State | Rows, full archive (1988→, paid) | Rows in free files (2024→, 48h delay) | CSV | Source last scraped | Newest notice on file | Source status |
|---|---:|---:|---|---|---|---|
| [Alaska](https://apventureengine.github.io/warn-act-notices/states/alaska.html) (AK) | 66 | 0 | — | 2026-09-02 18:38 UTC | 2026-07-06 | ok |
| [Alabama](https://apventureengine.github.io/warn-act-notices/states/alabama.html) (AL) | 1,061 | 0 | — | 2026-09-02 18:38 UTC | 2026-08-31 | ok |
| [Arizona](https://apventureengine.github.io/warn-act-notices/states/arizona.html) (AZ) | 636 | 121 | [az.csv](data/by-state/az.csv) | 2026-09-02 18:39 UTC | 2026-08-21 | ok |
| [California](https://apventureengine.github.io/warn-act-notices/states/california.html) (CA) | 16,556 | 3,991 | [ca.csv](data/by-state/ca.csv) | 2026-09-02 18:42 UTC | 2026-08-31 | ok |
| [Colorado](https://apventureengine.github.io/warn-act-notices/states/colorado.html) (CO) | 835 | 177 | [co.csv](data/by-state/co.csv) | 2026-09-02 18:39 UTC | 2026-08-14 | ok |
| [Connecticut](https://apventureengine.github.io/warn-act-notices/states/connecticut.html) (CT) | 871 | 76 | [ct.csv](data/by-state/ct.csv) | 2026-09-02 18:39 UTC | 2026-06-28 | ok |
| [District of Columbia](https://apventureengine.github.io/warn-act-notices/states/district-of-columbia.html) (DC) | 143 | 0 | — | 2026-09-02 18:39 UTC | 2026-07-27 | ok |
| [Delaware](https://apventureengine.github.io/warn-act-notices/states/delaware.html) (DE) | 100 | 0 | — | 2026-09-02 18:40 UTC | 2026-08-10 | ok |
| [Florida](https://apventureengine.github.io/warn-act-notices/states/florida.html) (FL) | 3,115 | 746 | [fl.csv](data/by-state/fl.csv) | 2026-09-02 18:44 UTC | 2026-08-28 | ok |
| [Georgia](https://apventureengine.github.io/warn-act-notices/states/georgia.html) (GA) | 282 | 225 | [ga.csv](data/by-state/ga.csv) | 2026-09-02 18:42 UTC | 2026-08-31 | ok |
| [Iowa](https://apventureengine.github.io/warn-act-notices/states/iowa.html) (IA) | 417 | 79 | [ia.csv](data/by-state/ia.csv) | 2026-09-02 18:40 UTC | 2026-09-01 | ok |
| [Illinois](https://apventureengine.github.io/warn-act-notices/states/illinois.html) (IL) | 4,842 | 346 | [il.csv](data/by-state/il.csv) | 2026-09-02 18:40 UTC | 2026-08-25 | ok |
| [Indiana](https://apventureengine.github.io/warn-act-notices/states/indiana.html) (IN) | 1,180 | 260 | [in.csv](data/by-state/in.csv) | 2026-09-02 18:40 UTC | 2026-08-13 | ok |
| [Kansas](https://apventureengine.github.io/warn-act-notices/states/kansas.html) (KS) | 791 | 34 | [ks.csv](data/by-state/ks.csv) | 2026-09-02 18:40 UTC | 2026-05-01 | ok |
| [Kentucky](https://apventureengine.github.io/warn-act-notices/states/kentucky.html) (KY) | 804 | 38 | [ky.csv](data/by-state/ky.csv) | 2026-09-02 18:40 UTC | 2026-08-10 | ok |
| [Louisiana](https://apventureengine.github.io/warn-act-notices/states/louisiana.html) (LA) | 38 | 25 | [la.csv](data/by-state/la.csv) | 2026-09-02 18:42 UTC | 2026-08-26 | ok |
| [Maryland](https://apventureengine.github.io/warn-act-notices/states/maryland.html) (MD) | 1,274 | 328 | [md.csv](data/by-state/md.csv) | 2026-09-02 18:41 UTC | 2026-08-31 | ok |
| [Maine](https://apventureengine.github.io/warn-act-notices/states/maine.html) (ME) | 85 | 0 | — | 2026-09-02 18:41 UTC | 2026-08-04 | ok |
| [Michigan](https://apventureengine.github.io/warn-act-notices/states/michigan.html) (MI) | 112 | 112 | [mi.csv](data/by-state/mi.csv) | 2026-09-02 18:41 UTC | 2026-08-28 | ok |
| [Mississippi](https://apventureengine.github.io/warn-act-notices/states/mississippi.html) (MS) | 136 | 0 | — | 2026-09-02 18:45 UTC | 2026-05-11 | ok |
| [Montana](https://apventureengine.github.io/warn-act-notices/states/montana.html) (MT) | 46 | 18 | [mt.csv](data/by-state/mt.csv) | 2026-09-02 18:41 UTC | 2026-07-21 | ok |
| [North Carolina](https://apventureengine.github.io/warn-act-notices/states/north-carolina.html) (NC) | 294 | 0 | — | 2026-09-02 18:44 UTC | 2026-08-13 | ok |
| [Nebraska](https://apventureengine.github.io/warn-act-notices/states/nebraska.html) (NE) | 845 | 29 | [ne.csv](data/by-state/ne.csv) | 2026-09-02 18:41 UTC | 2026-08-26 | ok |
| [New Jersey](https://apventureengine.github.io/warn-act-notices/states/new-jersey.html) (NJ) | 2,322 | 313 | [nj.csv](data/by-state/nj.csv) | 2026-09-02 18:41 UTC | 2026-09-01 | ok |
| [New Mexico](https://apventureengine.github.io/warn-act-notices/states/new-mexico.html) (NM) | 116 | 12 | [nm.csv](data/by-state/nm.csv) | 2026-09-02 18:41 UTC | 2026-06-29 | ok |
| [New York](https://apventureengine.github.io/warn-act-notices/states/new-york.html) (NY) | 141 | 141 | [ny.csv](data/by-state/ny.csv) | 2026-09-02 18:41 UTC | 2026-08-04 | ok |
| [Oklahoma](https://apventureengine.github.io/warn-act-notices/states/oklahoma.html) (OK) | 219 | 29 | [ok.csv](data/by-state/ok.csv) | 2026-09-02 18:41 UTC | 2026-08-17 | ok |
| [Oregon](https://apventureengine.github.io/warn-act-notices/states/oregon.html) (OR) | 1,369 | 196 | [or.csv](data/by-state/or.csv) | 2026-09-02 18:41 UTC | 2026-09-01 | ok |
| [Pennsylvania](https://apventureengine.github.io/warn-act-notices/states/pennsylvania.html) (PA) | 308 | 0 | — | 2026-09-02 18:41 UTC | 2026-08-31 | ok |
| [Rhode Island](https://apventureengine.github.io/warn-act-notices/states/rhode-island.html) (RI) | 126 | 27 | [ri.csv](data/by-state/ri.csv) | 2026-09-02 18:41 UTC | 2026-06-29 | ok |
| [South Carolina](https://apventureengine.github.io/warn-act-notices/states/south-carolina.html) (SC) | 604 | 134 | [sc.csv](data/by-state/sc.csv) | 2026-09-02 18:41 UTC | 2026-08-28 | ok |
| [South Dakota](https://apventureengine.github.io/warn-act-notices/states/south-dakota.html) (SD) | 80 | 16 | [sd.csv](data/by-state/sd.csv) | 2026-09-02 18:41 UTC | 2026-08-10 | ok |
| [Tennessee](https://apventureengine.github.io/warn-act-notices/states/tennessee.html) (TN) | 1,060 | 97 | [tn.csv](data/by-state/tn.csv) | 2026-09-02 18:42 UTC | 2026-08-24 | ok |
| [Texas](https://apventureengine.github.io/warn-act-notices/states/texas.html) (TX) | 2,358 | 0 | — | 2026-09-02 18:44 UTC | 2026-06-23 | ok |
| [Utah](https://apventureengine.github.io/warn-act-notices/states/utah.html) (UT) | 282 | 51 | [ut.csv](data/by-state/ut.csv) | 2026-09-02 18:42 UTC | 2026-08-13 | ok |
| [Vermont](https://apventureengine.github.io/warn-act-notices/states/vermont.html) (VT) | 70 | 16 | [vt.csv](data/by-state/vt.csv) | 2026-09-02 18:42 UTC | 2026-06-17 | ok |
| [Washington](https://apventureengine.github.io/warn-act-notices/states/washington.html) (WA) | 1,496 | 274 | [wa.csv](data/by-state/wa.csv) | 2026-09-02 18:42 UTC | 2026-09-01 | ok |
| [Wisconsin](https://apventureengine.github.io/warn-act-notices/states/wisconsin.html) (WI) | 617 | 201 | [wi.csv](data/by-state/wi.csv) | 2026-09-02 18:42 UTC | 2026-08-24 | ok |
| [West Virginia](https://apventureengine.github.io/warn-act-notices/states/west-virginia.html) (WV) | 58 | 0 | — | 2026-09-02 18:45 UTC | 2026-08-19 | ok |

**Not covered (12 states):** [Arkansas](https://dws.arkansas.gov/workforce-services/employers/dislocated-worker-services/) (agency site blocks automated access), [Hawaii](https://labor.hawaii.gov/wdc/real-time-warn-updates/) (agency page unparseable (obfuscated links)), [Idaho](https://www.labor.idaho.gov/businesses/layoff-assistance/#2) (agency PDF is corrupt), [Massachusetts](https://www.mass.gov/info-details/worker-adjustment-and-retraining-notification-act-warn-layoff-and-closure-updates) (agency site blocks automated access), [Minnesota](https://mn.gov/deed/programs-services/dislocated-worker/dislocated-worker/news/) (agency site blocks automated access), [Missouri](https://jobs.mo.gov/employer/warn) (agency site blocks automated access), [Nevada](https://detr.nv.gov/Page/WARN) (agency site blocks automated access), [New Hampshire](https://www.nhes.nh.gov/employers/business-compliance) (agency site blocks automated access), [North Dakota](https://www.jobsnd.com/documents) (no public WARN listing located), [Ohio](https://jfs.ohio.gov/job-workforce-services/job-programs-and-services/submit-a-warn-notice/current-public-notices-of-layoffs-and-closures) (listing is a browser-only app, no data endpoint), [Virginia](https://jfs.ohio.gov/job-workforce-services/job-programs-and-services/submit-a-warn-notice/current-public-notices-of-layoffs-and-closures) (listing is a browser-only app, no data endpoint), [Wyoming](https://dws.wyo.gov/dws-division/workforce-centers-and-program-operations/employers/business-expansion-closing-services/) (WARN filings are non-public by state statute). We do not guess or backfill these from third parties; if a state opens a public listing, it is added.

## What normalization actually does

State portals spell the same employer many ways (store numbers, site tails,
suffixes, ALL CAPS). `company_canonical` collapses them so you can count and
watch an employer across states and years — the part no raw scraper output gives you:

- **Kaiser Foundation Hospitals** ← 27 raw spellings, e.g. `Kaiser Foundation Hospitals`; `Kaiser Foundation Hospitals (1100)`; `Kaiser Foundation Hospitals (12254)`; `Kaiser Foundation Hospitals (1450)`
- **Southern PacPizza** ← 25 raw spellings, e.g. `Southern PacPizza dba Pizza Hut - 029197`; `Southern PacPizza dba Pizza Hut - 029198`; `Southern PacPizza dba Pizza Hut - 029199`; `Southern PacPizza dba Pizza Hut - 029200`
- **Good Sports Plus** ← 12 raw spellings, e.g. `Good Sports Plus Ltd, dba Arc Phil D. Swing Elementary School`; `Good Sports Plus Ltd. dba Arc`; `Good Sports Plus Ltd. dba Arc - Central Union High School`; `Good Sports Plus Ltd. dba Arc - Desert Valley High School`

**Archive sample (free):** the complete Oregon back-catalogue, 1988→present
(1,369 rows, same schema as the paid 1988+ archive):
[`data/samples/oregon-warn-notices-1988-present.csv`](data/samples/oregon-warn-notices-1988-present.csv).

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
| Astrion | FL | EGLIN AIR FORCE BASE, FL, 32542 | 204 | 2026-08-28 |
| Bumble Bee Foods | CA | Los Angeles County | 197 | 2026-08-11 |

## Monthly trend (last 12 months, this dataset)

| Month | Notices | Workers affected |
|---|---:|---:|
| 2025-09 | 220 | 25,698 |
| 2025-10 | 358 | 38,916 |
| 2025-11 | 264 | 20,870 |
| 2025-12 | 112 | 9,659 |
| 2026-01 | 311 | 27,617 |
| 2026-02 | 290 | 22,400 |
| 2026-03 | 272 | 17,368 |
| 2026-04 | 309 | 23,542 |
| 2026-05 | 256 | 40,260 |
| 2026-06 | 309 | 16,080 |
| 2026-07 | 190 | 15,216 |
| 2026-08 | 174 | 17,152 |

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
expensive part. As of 2026-09-02: **83 notices** affecting 7,894 workers (dated in the last 45 days, 16 states) are in the real-time feed and not yet in this repo's free files — each lands here only after its 48-hour delay. Machine-readable: `delay_gap` in [`data/coverage.json`](data/coverage.json).

Commercial options:

- **[Real-time feed — $49/mo](https://approj.gumroad.com/l/warn-realtime)** — the same dataset with zero
  delay, including notices seen in the last 48h, refreshed on every pipeline
  run. Delivered as a private GitHub repo you can pull/watch.
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice
  we have back to 1988 (45,755 rows, all 39 states), CSV + JSON.

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
