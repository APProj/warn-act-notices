# US WARN Act Layoff Notices — normalized, daily-updated dataset

[![US WARN layoffs 2026](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge.json)](https://apventureengine.github.io/warn-act-notices/yearly/) [![data updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge-updated.json)](https://github.com/APVentureEngine/warn-act-notices/commits/main) — live, embeddable: [get these badges](API.md#live-badges)

**9,428 layoff notices since 2024 · 39 states · one clean schema · CSV + JSON · updated 2026-09-03**

Every US state publishes WARN Act layoff notices differently — different sites,
formats, column names, and date conventions. This repo normalizes them into one
deduplicated dataset, refreshed daily. Background on the law itself: the
[Worker Adjustment and Retraining Notification Act of 1988](https://en.wikipedia.org/wiki/Worker_Adjustment_and_Retraining_Notification_Act_of_1988)
on Wikipedia.

## Get the data

- CSV: [`data/warn_notices.csv`](data/warn_notices.csv)
- JSON: [`data/warn_notices.json`](data/warn_notices.json)
- Coverage/freshness metadata: [`data/coverage.json`](data/coverage.json)
- Per-state CSVs: [`data/by-state/`](data/by-state/) — see table below
- **Newly added in the last 7 days:** [`data/latest.csv`](data/latest.csv) / [`data/latest.json`](data/latest.json) — stable raw URLs for "new WARN notices" alerting and dashboards (no delay)
- Stats page: https://apventureengine.github.io/warn-act-notices/
- RSS feed of newly-published notices: https://apventureengine.github.io/warn-act-notices/feed.xml (no delay)
- Per-state RSS feeds (one state per feed — pipe a single state into Slack/Feedly/Zapier): OPML bundle https://apventureengine.github.io/warn-act-notices/feeds/feeds.opml, or `feeds/<state>.xml`, e.g. https://apventureengine.github.io/warn-act-notices/feeds/california.xml
- Weekly summaries (biggest layoffs, per-state totals, one page per week): https://apventureengine.github.io/warn-act-notices/weekly/
- Monthly summaries (current month updates daily): https://apventureengine.github.io/warn-act-notices/monthly/
- Yearly totals (current year is a running total, updated daily): https://apventureengine.github.io/warn-act-notices/yearly/
- Browse layoffs by employer: https://apventureengine.github.io/warn-act-notices/employers/
- Instant employer search (free tier): https://apventureengine.github.io/warn-act-notices/search.html
- How this compares to WARNTracker, Intellizence, warn-scraper & state portals: https://apventureengine.github.io/warn-act-notices/compare.html
- Use it as a free layoffs API (stable raw URLs, curl/pandas/Sheets examples): [API.md](API.md)
- Hugging Face mirror (same free tier, `load_dataset` / pandas ready, re-uploaded every refresh): [APProjects/us-warn-act-layoffs-daily](https://huggingface.co/datasets/APProjects/us-warn-act-layoffs-daily)
- Live explorer on Hugging Face Spaces (search employers, newest notices, per-state freshness; reads this repo directly): [APProjects/us-layoff-notices-explorer](https://huggingface.co/spaces/APProjects/us-layoff-notices-explorer)
- Machine-readable schema: [`datapackage.json`](datapackage.json) · Cite this dataset: [`CITATION.cff`](CITATION.cff) · License: [CC BY 4.0](LICENSE)

No login, no API key. Scope of the free dataset, stated plainly: notices from
**2024-01-01** onward, **with no delay** (every notice is published on the refresh that first sees it). The full archive back to 1988
(45,760 notices) and per-customer WARN Watch alerts are the commercial products
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

| State | Rows, full archive (1988→, paid) | Rows in free files (2024→, no delay) | CSV | Source last scraped | Newest notice on file | Source status |
|---|---:|---:|---|---|---|---|
| [Alaska](https://apventureengine.github.io/warn-act-notices/states/alaska.html) (AK) | 66 | 4 | [ak.csv](data/by-state/ak.csv) | 2026-09-03 18:12 UTC | 2026-07-06 | ok |
| [Alabama](https://apventureengine.github.io/warn-act-notices/states/alabama.html) (AL) | 1,061 | 77 | [al.csv](data/by-state/al.csv) | 2026-09-03 18:12 UTC | 2026-08-31 | ok |
| [Arizona](https://apventureengine.github.io/warn-act-notices/states/arizona.html) (AZ) | 636 | 121 | [az.csv](data/by-state/az.csv) | 2026-09-03 18:12 UTC | 2026-08-21 | ok |
| [California](https://apventureengine.github.io/warn-act-notices/states/california.html) (CA) | 16,556 | 4,021 | [ca.csv](data/by-state/ca.csv) | 2026-09-03 18:15 UTC | 2026-08-31 | ok |
| [Colorado](https://apventureengine.github.io/warn-act-notices/states/colorado.html) (CO) | 835 | 177 | [co.csv](data/by-state/co.csv) | 2026-09-03 18:12 UTC | 2026-08-14 | ok |
| [Connecticut](https://apventureengine.github.io/warn-act-notices/states/connecticut.html) (CT) | 871 | 76 | [ct.csv](data/by-state/ct.csv) | 2026-09-03 18:12 UTC | 2026-06-28 | ok |
| [District of Columbia](https://apventureengine.github.io/warn-act-notices/states/district-of-columbia.html) (DC) | 143 | 56 | [dc.csv](data/by-state/dc.csv) | 2026-09-03 18:13 UTC | 2026-07-27 | ok |
| [Delaware](https://apventureengine.github.io/warn-act-notices/states/delaware.html) (DE) | 100 | 5 | [de.csv](data/by-state/de.csv) | 2026-09-03 18:13 UTC | 2026-08-10 | ok |
| [Florida](https://apventureengine.github.io/warn-act-notices/states/florida.html) (FL) | 3,115 | 746 | [fl.csv](data/by-state/fl.csv) | 2026-09-03 18:17 UTC | 2026-08-28 | ok |
| [Georgia](https://apventureengine.github.io/warn-act-notices/states/georgia.html) (GA) | 282 | 226 | [ga.csv](data/by-state/ga.csv) | 2026-09-03 18:16 UTC | 2026-08-31 | ok |
| [Iowa](https://apventureengine.github.io/warn-act-notices/states/iowa.html) (IA) | 417 | 81 | [ia.csv](data/by-state/ia.csv) | 2026-09-03 18:13 UTC | 2026-09-01 | ok |
| [Illinois](https://apventureengine.github.io/warn-act-notices/states/illinois.html) (IL) | 4,842 | 346 | [il.csv](data/by-state/il.csv) | 2026-09-03 18:13 UTC | 2026-08-25 | ok |
| [Indiana](https://apventureengine.github.io/warn-act-notices/states/indiana.html) (IN) | 1,180 | 260 | [in.csv](data/by-state/in.csv) | 2026-09-03 18:13 UTC | 2026-08-13 | ok |
| [Kansas](https://apventureengine.github.io/warn-act-notices/states/kansas.html) (KS) | 791 | 34 | [ks.csv](data/by-state/ks.csv) | 2026-09-03 18:13 UTC | 2026-05-01 | ok |
| [Kentucky](https://apventureengine.github.io/warn-act-notices/states/kentucky.html) (KY) | 804 | 38 | [ky.csv](data/by-state/ky.csv) | 2026-09-03 18:13 UTC | 2026-08-10 | ok |
| [Louisiana](https://apventureengine.github.io/warn-act-notices/states/louisiana.html) (LA) | 38 | 38 | [la.csv](data/by-state/la.csv) | 2026-09-03 18:16 UTC | 2026-08-26 | ok |
| [Maryland](https://apventureengine.github.io/warn-act-notices/states/maryland.html) (MD) | 1,274 | 329 | [md.csv](data/by-state/md.csv) | 2026-09-03 18:14 UTC | 2026-08-31 | ok |
| [Maine](https://apventureengine.github.io/warn-act-notices/states/maine.html) (ME) | 85 | 17 | [me.csv](data/by-state/me.csv) | 2026-09-03 18:14 UTC | 2026-08-04 | ok |
| [Michigan](https://apventureengine.github.io/warn-act-notices/states/michigan.html) (MI) | 112 | 112 | [mi.csv](data/by-state/mi.csv) | 2026-09-03 18:14 UTC | 2026-08-28 | ok |
| [Mississippi](https://apventureengine.github.io/warn-act-notices/states/mississippi.html) (MS) | 136 | 43 | [ms.csv](data/by-state/ms.csv) | 2026-09-03 18:18 UTC | 2026-05-11 | ok |
| [Montana](https://apventureengine.github.io/warn-act-notices/states/montana.html) (MT) | 46 | 18 | [mt.csv](data/by-state/mt.csv) | 2026-09-03 18:14 UTC | 2026-07-21 | ok |
| [North Carolina](https://apventureengine.github.io/warn-act-notices/states/north-carolina.html) (NC) | 294 | 185 | [nc.csv](data/by-state/nc.csv) | 2026-09-03 18:18 UTC | 2026-08-13 | ok |
| [Nebraska](https://apventureengine.github.io/warn-act-notices/states/nebraska.html) (NE) | 845 | 29 | [ne.csv](data/by-state/ne.csv) | 2026-09-03 18:14 UTC | 2026-08-26 | ok |
| [New Jersey](https://apventureengine.github.io/warn-act-notices/states/new-jersey.html) (NJ) | 2,322 | 314 | [nj.csv](data/by-state/nj.csv) | 2026-09-03 18:14 UTC | 2026-09-01 | ok |
| [New Mexico](https://apventureengine.github.io/warn-act-notices/states/new-mexico.html) (NM) | 116 | 12 | [nm.csv](data/by-state/nm.csv) | 2026-09-03 18:14 UTC | 2026-06-29 | ok |
| [New York](https://apventureengine.github.io/warn-act-notices/states/new-york.html) (NY) | 141 | 141 | [ny.csv](data/by-state/ny.csv) | 2026-09-03 18:14 UTC | 2026-08-04 | ok |
| [Oklahoma](https://apventureengine.github.io/warn-act-notices/states/oklahoma.html) (OK) | 219 | 29 | [ok.csv](data/by-state/ok.csv) | 2026-09-03 18:14 UTC | 2026-08-17 | ok |
| [Oregon](https://apventureengine.github.io/warn-act-notices/states/oregon.html) (OR) | 1,369 | 202 | [or.csv](data/by-state/or.csv) | 2026-09-03 18:14 UTC | 2026-09-01 | ok |
| [Pennsylvania](https://apventureengine.github.io/warn-act-notices/states/pennsylvania.html) (PA) | 309 | 256 | [pa.csv](data/by-state/pa.csv) | 2026-09-03 18:14 UTC | 2026-08-31 | ok |
| [Rhode Island](https://apventureengine.github.io/warn-act-notices/states/rhode-island.html) (RI) | 126 | 27 | [ri.csv](data/by-state/ri.csv) | 2026-09-03 18:14 UTC | 2026-06-29 | ok |
| [South Carolina](https://apventureengine.github.io/warn-act-notices/states/south-carolina.html) (SC) | 604 | 135 | [sc.csv](data/by-state/sc.csv) | 2026-09-03 18:14 UTC | 2026-08-28 | ok |
| [South Dakota](https://apventureengine.github.io/warn-act-notices/states/south-dakota.html) (SD) | 80 | 16 | [sd.csv](data/by-state/sd.csv) | 2026-09-03 18:14 UTC | 2026-08-10 | ok |
| [Tennessee](https://apventureengine.github.io/warn-act-notices/states/tennessee.html) (TN) | 1,061 | 98 | [tn.csv](data/by-state/tn.csv) | 2026-09-03 18:15 UTC | 2026-09-02 | ok |
| [Texas](https://apventureengine.github.io/warn-act-notices/states/texas.html) (TX) | 2,358 | 573 | [tx.csv](data/by-state/tx.csv) | 2026-09-03 18:17 UTC | 2026-06-23 | ok |
| [Utah](https://apventureengine.github.io/warn-act-notices/states/utah.html) (UT) | 282 | 51 | [ut.csv](data/by-state/ut.csv) | 2026-09-03 18:15 UTC | 2026-08-13 | ok |
| [Vermont](https://apventureengine.github.io/warn-act-notices/states/vermont.html) (VT) | 70 | 16 | [vt.csv](data/by-state/vt.csv) | 2026-09-03 18:15 UTC | 2026-06-17 | ok |
| [Washington](https://apventureengine.github.io/warn-act-notices/states/washington.html) (WA) | 1,499 | 280 | [wa.csv](data/by-state/wa.csv) | 2026-09-03 18:15 UTC | 2026-09-02 | ok |
| [Wisconsin](https://apventureengine.github.io/warn-act-notices/states/wisconsin.html) (WI) | 617 | 201 | [wi.csv](data/by-state/wi.csv) | 2026-09-03 18:15 UTC | 2026-08-24 | ok |
| [West Virginia](https://apventureengine.github.io/warn-act-notices/states/west-virginia.html) (WV) | 58 | 38 | [wv.csv](data/by-state/wv.csv) | 2026-09-03 18:18 UTC | 2026-08-19 | ok |

**Not covered (12 states):** [Arkansas](https://dws.arkansas.gov/workforce-services/employers/dislocated-worker-services/) (agency site blocks automated access), [Hawaii](https://labor.hawaii.gov/wdc/real-time-warn-updates/) (agency page unparseable (obfuscated links)), [Idaho](https://www.labor.idaho.gov/businesses/layoff-assistance/) (agency PDF is corrupt), [Massachusetts](https://www.mass.gov/info-details/worker-adjustment-and-retraining-notification-act-warn-layoff-and-closure-updates) (agency site blocks automated access), [Minnesota](https://mn.gov/deed/programs-services/dislocated-worker/dislocated-worker/news/) (agency site blocks automated access), [Missouri](https://jobs.mo.gov/employer/warn) (agency site blocks automated access), [Nevada](https://detr.nv.gov/Page/WARN) (agency site blocks automated access), [New Hampshire](https://www.nhes.nh.gov/employers/business-compliance) (agency site blocks automated access), [North Dakota](https://www.jobsnd.com/documents) (no public WARN listing located), [Ohio](https://jfs.ohio.gov/job-workforce-services/job-programs-and-services/submit-a-warn-notice/current-public-notices-of-layoffs-and-closures) (listing is a browser-only app, no data endpoint), [Virginia](https://www.vec.virginia.gov/warn-notices) (listing is a browser-only app, no data endpoint), Wyoming (WARN filings are non-public by state statute). We do not guess or
backfill these from third parties; if a state opens a public listing it is added.

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

## Biggest layoff notices — last 30 days (2026-08-04 to 2026-09-03)

| Company | State | Location | Workers | Notice date (or layoff date where the state publishes none) |
|---|---|---|---:|---|
| Tyson Foods | IL | Hillsdale, 28424 38TH Ave. North | 2,495 | 2026-08-13 |
| JBS Souderton | PA | Souderton, Montgomery | 1,485 | layoff 2026-08-14 |
| Borton & Sons | WA | Yakima, Zillah, Pasco, Burbank, Prescott, Soap Lake, Othello, Mesa | 928 | 2026-08-21 |
| 24Hr Homecare | CA | Los Angeles County | 738 | 2026-08-31 |
| Tyson Fresh Meats | UT | Eagle Mountain | 723 | 2026-08-13 |
| Republic National Distributing Company (RNDC) | MI | Delta, Grand Traverse, Kent, Saginaw, Wayne | 641 | layoff 2026-08-17 |
| Sky Chefs | NY | Queens | 471 | 2026-08-04 |
| Jabil | CA | Santa Clara County | 382 | 2026-08-21 |
| Amentum | MD | 7710 Milestone Parkway Hanover, MD 21076 | 382 (2 phases) | 2026-08-18 |
| Republic National Distributing | GA | National Dr SW Atlanta, Cobb County | 321 | 2026-08-26 |
| Healthcare SC | SC | Fairfield | 254 | layoff 2026-08-28 |
| TikTok USDS JV | TN | Davidson | 250 | 2026-08-05 |
| Sundquist Fruit | WA | Yakima and Franklin Counties | 243 | 2026-09-02 |
| Rec Boat Holdings | MI | Wexford | 239 | layoff 2026-08-15 |
| Starbucks | WA | Seattle | 224 | 2026-08-20 |

_Grouped per notice (a phased notice with several layoff dates counts once, workers summed). 5 row(s) in this window whose state record names only a facility, not an employer, are omitted here but kept in the CSV as published. 4 row(s) are dated by the layoff/closure date and marked "layoff": Michigan, Pennsylvania and South Carolina publish no notice date at all._

## Monthly trend (last 12 months, this dataset)

| Month | Notices | Workers affected |
|---|---:|---:|
| 2025-10 | 412 | 42,952 |
| 2025-11 | 282 | 24,820 |
| 2025-12 | 133 | 11,787 |
| 2026-01 | 340 | 32,217 |
| 2026-02 | 325 | 26,092 |
| 2026-03 | 306 | 21,550 |
| 2026-04 | 345 | 29,639 |
| 2026-05 | 265 | 42,082 |
| 2026-06 | 332 | 18,544 |
| 2026-07 | 205 | 17,769 |
| 2026-08 | 222 | 20,192 |
| 2026-09 | 12 | 833 |

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

## WARN Watch & full history (commercial)

The free files above are complete and carry no delay. What they cannot do is
watch YOUR list every morning. Commercial options:

- **[WARN Watch — $49/year, one payment](https://apventureengine.github.io/warn-act-notices/watch.html)** — up to 25 employer
  terms plus whole-state watches across all 39 covered states, matched on
  every daily refresh for 365 days; hits land on a private alert page + RSS feed
  (no login). [What it checks and its limits](https://apventureengine.github.io/warn-act-notices/watch.html) · [buy](https://approj.gumroad.com/l/warn-watch).
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice
  we have back to 1988 (45,760 rows, all 39 states), CSV + JSON.

Questions first? [Open an issue](https://github.com/APVentureEngine/warn-act-notices/issues) with the label `commercial`.

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
