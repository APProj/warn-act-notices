# US WARN Act Layoff Notices — normalized, daily-updated dataset

[![US WARN layoffs 2026](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge.json)](https://approjects-warn-act-notices.static.hf.space/yearly/index.html) [![data updated](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAPVentureEngine%2Fwarn-act-notices%2Fmain%2Fdata%2Fbadge-updated.json)](https://github.com/APVentureEngine/warn-act-notices/commits/main) — live, embeddable: [get these badges](API.md#live-badges)

**9,445 layoff notices since 2024 · 39 states · one clean schema · CSV + JSON · updated 2026-09-05**

**Browse it:** [live site, search + per-state pages](https://approjects-warn-act-notices.static.hf.space/index.html) · **Machine-readable:**
[`data/warn_notices.csv`](data/warn_notices.csv) · **Hugging Face:**
[APProjects/us-warn-act-layoffs-daily](https://huggingface.co/datasets/APProjects/us-warn-act-layoffs-daily)

Every US state publishes WARN Act layoff notices differently — different sites,
formats, column names, and date conventions. This repo normalizes them into one
deduplicated dataset, refreshed daily. Background on the law itself: the
[Worker Adjustment and Retraining Notification Act of 1988](https://en.wikipedia.org/wiki/Worker_Adjustment_and_Retraining_Notification_Act_of_1988)
on Wikipedia.

**Need to be told when a name on your list files?** The files below are yours to
poll. WARN Watch does the polling: your employer terms and states are matched on
every daily refresh and hits are pushed to a private alert page, an RSS feed, and
your Slack / Discord / Teams webhook — no login, no account here.
[Start the free 30-day trial](https://approj.gumroad.com/l/warn-free-watch) (3 employers or 1 state, no card) ·
[WARN Watch — $49/year](https://approj.gumroad.com/l/warn-watch) ·
[Full 1988+ archive — $199](https://approj.gumroad.com/l/warn-archive) (45,777 rows)

## Get the data

- CSV: [`data/warn_notices.csv`](data/warn_notices.csv)
- JSON: [`data/warn_notices.json`](data/warn_notices.json)
- Coverage/freshness metadata: [`data/coverage.json`](data/coverage.json)
- Per-state CSVs: [`data/by-state/`](data/by-state/) — see table below
- **Newly added in the last 7 days:** [`data/latest.csv`](data/latest.csv) / [`data/latest.json`](data/latest.json) — stable raw URLs for "new WARN notices" alerting and dashboards (no delay)
- Stats page: https://approjects-warn-act-notices.static.hf.space/index.html
- RSS feed of newly-published notices: https://approjects-warn-act-notices.static.hf.space/feed.xml (no delay)
- Per-state RSS feeds (one state per feed — pipe a single state into Slack/Feedly/Zapier): OPML bundle https://approjects-warn-act-notices.static.hf.space/feeds/feeds.opml, or `feeds/<state>.xml`, e.g. https://approjects-warn-act-notices.static.hf.space/feeds/california.xml
- Weekly summaries (biggest layoffs, per-state totals, one page per week): https://approjects-warn-act-notices.static.hf.space/weekly/index.html
- Monthly summaries (current month updates daily): https://approjects-warn-act-notices.static.hf.space/monthly/index.html
- Yearly totals (current year is a running total, updated daily): https://approjects-warn-act-notices.static.hf.space/yearly/index.html
- Browse layoffs by employer: https://approjects-warn-act-notices.static.hf.space/employers/index.html
- Instant employer search (free tier): https://approjects-warn-act-notices.static.hf.space/search.html
- How this compares to WARNTracker, Intellizence, warn-scraper & state portals: https://approjects-warn-act-notices.static.hf.space/compare.html
- Use it as a free layoffs API (stable raw URLs, curl/pandas/Sheets examples): [API.md](API.md)
- Hugging Face mirror (same free tier, `load_dataset` / pandas ready, re-uploaded every refresh): [APProjects/us-warn-act-layoffs-daily](https://huggingface.co/datasets/APProjects/us-warn-act-layoffs-daily)
- Live explorer on Hugging Face Spaces (search employers, newest notices, per-state freshness; reads this repo directly): [APProjects/us-layoff-notices-explorer](https://huggingface.co/spaces/APProjects/us-layoff-notices-explorer)
- Machine-readable schema: [`datapackage.json`](datapackage.json) · Cite this dataset: [`CITATION.cff`](CITATION.cff) · License: [CC BY 4.0](LICENSE)

No login, no API key. Scope of the free dataset, stated plainly: notices from
**2024-01-01** onward, **with no delay** (every notice is published on the refresh that first sees it). The full archive back to 1988
(45,777 notices) and per-customer WARN Watch alerts are the commercial products
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
| [Alaska](https://approjects-warn-act-notices.static.hf.space/states/alaska.html) (AK) | 66 | 4 | [ak.csv](data/by-state/ak.csv) | 2026-09-05 00:10 UTC | 2026-07-06 | behind cadence — not yet investigated |
| [Alabama](https://approjects-warn-act-notices.static.hf.space/states/alabama.html) (AL) | 1,061 | 77 | [al.csv](data/by-state/al.csv) | 2026-09-05 00:10 UTC | 2026-08-31 | current |
| [Arizona](https://approjects-warn-act-notices.static.hf.space/states/arizona.html) (AZ) | 636 | 121 | [az.csv](data/by-state/az.csv) | 2026-09-05 00:11 UTC | 2026-08-21 | current |
| [California](https://approjects-warn-act-notices.static.hf.space/states/california.html) (CA) | 16,563 | 4,028 | [ca.csv](data/by-state/ca.csv) | 2026-09-05 00:20 UTC | 2026-09-02 | current |
| [Colorado](https://approjects-warn-act-notices.static.hf.space/states/colorado.html) (CO) | 835 | 177 | [co.csv](data/by-state/co.csv) | 2026-09-05 00:12 UTC | 2026-08-14 | current |
| [Connecticut](https://approjects-warn-act-notices.static.hf.space/states/connecticut.html) (CT) | 871 | 76 | [ct.csv](data/by-state/ct.csv) | 2026-09-05 00:12 UTC | 2026-06-28 | quiet: agency portal checked by hand 2026-09-02, nothing newer published |
| [District of Columbia](https://approjects-warn-act-notices.static.hf.space/states/district-of-columbia.html) (DC) | 143 | 56 | [dc.csv](data/by-state/dc.csv) | 2026-09-05 00:12 UTC | 2026-07-27 | current |
| [Delaware](https://approjects-warn-act-notices.static.hf.space/states/delaware.html) (DE) | 100 | 5 | [de.csv](data/by-state/de.csv) | 2026-09-05 00:12 UTC | 2026-08-10 | current |
| [Florida](https://approjects-warn-act-notices.static.hf.space/states/florida.html) (FL) | 3,115 | 746 | [fl.csv](data/by-state/fl.csv) | 2026-09-05 00:23 UTC | 2026-08-28 | current |
| [Georgia](https://approjects-warn-act-notices.static.hf.space/states/georgia.html) (GA) | 283 | 227 | [ga.csv](data/by-state/ga.csv) | 2026-09-05 00:21 UTC | 2026-09-04 | current |
| [Iowa](https://approjects-warn-act-notices.static.hf.space/states/iowa.html) (IA) | 417 | 81 | [ia.csv](data/by-state/ia.csv) | 2026-09-05 00:12 UTC | 2026-09-01 | current |
| [Illinois](https://approjects-warn-act-notices.static.hf.space/states/illinois.html) (IL) | 4,845 | 349 | [il.csv](data/by-state/il.csv) | 2026-09-05 00:12 UTC | 2026-09-02 | current |
| [Indiana](https://approjects-warn-act-notices.static.hf.space/states/indiana.html) (IN) | 1,182 | 262 | [in.csv](data/by-state/in.csv) | 2026-09-05 00:12 UTC | 2026-09-02 | current |
| [Kansas](https://approjects-warn-act-notices.static.hf.space/states/kansas.html) (KS) | 791 | 34 | [ks.csv](data/by-state/ks.csv) | 2026-09-05 00:13 UTC | 2026-05-01 | quiet: agency portal checked by hand 2026-09-02, nothing newer published |
| [Kentucky](https://approjects-warn-act-notices.static.hf.space/states/kentucky.html) (KY) | 804 | 38 | [ky.csv](data/by-state/ky.csv) | 2026-09-05 00:13 UTC | 2026-08-10 | current |
| [Louisiana](https://approjects-warn-act-notices.static.hf.space/states/louisiana.html) (LA) | 38 | 38 | [la.csv](data/by-state/la.csv) | 2026-09-05 00:21 UTC | 2026-08-26 | current |
| [Maryland](https://approjects-warn-act-notices.static.hf.space/states/maryland.html) (MD) | 1,274 | 329 | [md.csv](data/by-state/md.csv) | 2026-09-05 00:13 UTC | 2026-08-31 | current |
| [Maine](https://approjects-warn-act-notices.static.hf.space/states/maine.html) (ME) | 85 | 17 | [me.csv](data/by-state/me.csv) | 2026-09-04 00:05 UTC | 2026-08-04 | current |
| [Michigan](https://approjects-warn-act-notices.static.hf.space/states/michigan.html) (MI) | 114 | 114 | [mi.csv](data/by-state/mi.csv) | 2026-09-05 00:18 UTC | 2026-09-04 | current |
| [Mississippi](https://approjects-warn-act-notices.static.hf.space/states/mississippi.html) (MS) | 136 | 43 | [ms.csv](data/by-state/ms.csv) | 2026-09-05 00:23 UTC | 2026-05-11 | current; agency posts in batches (see state page) |
| [Montana](https://approjects-warn-act-notices.static.hf.space/states/montana.html) (MT) | 46 | 18 | [mt.csv](data/by-state/mt.csv) | 2026-09-05 00:18 UTC | 2026-07-21 | current |
| [North Carolina](https://approjects-warn-act-notices.static.hf.space/states/north-carolina.html) (NC) | 294 | 185 | [nc.csv](data/by-state/nc.csv) | 2026-09-05 00:23 UTC | 2026-08-13 | current |
| [Nebraska](https://approjects-warn-act-notices.static.hf.space/states/nebraska.html) (NE) | 845 | 29 | [ne.csv](data/by-state/ne.csv) | 2026-09-05 00:18 UTC | 2026-08-26 | current |
| [New Jersey](https://approjects-warn-act-notices.static.hf.space/states/new-jersey.html) (NJ) | 2,322 | 314 | [nj.csv](data/by-state/nj.csv) | 2026-09-05 00:18 UTC | 2026-09-01 | current |
| [New Mexico](https://approjects-warn-act-notices.static.hf.space/states/new-mexico.html) (NM) | 116 | 12 | [nm.csv](data/by-state/nm.csv) | 2026-09-05 00:18 UTC | 2026-06-29 | quiet: agency portal checked by hand 2026-09-02, nothing newer published |
| [New York](https://approjects-warn-act-notices.static.hf.space/states/new-york.html) (NY) | 142 | 142 | [ny.csv](data/by-state/ny.csv) | 2026-09-05 00:18 UTC | 2026-08-04 | current |
| [Oklahoma](https://approjects-warn-act-notices.static.hf.space/states/oklahoma.html) (OK) | 219 | 29 | [ok.csv](data/by-state/ok.csv) | 2026-09-05 00:18 UTC | 2026-08-17 | current |
| [Oregon](https://approjects-warn-act-notices.static.hf.space/states/oregon.html) (OR) | 1,369 | 202 | [or.csv](data/by-state/or.csv) | 2026-09-05 00:18 UTC | 2026-09-01 | current |
| [Pennsylvania](https://approjects-warn-act-notices.static.hf.space/states/pennsylvania.html) (PA) | 309 | 256 | [pa.csv](data/by-state/pa.csv) | 2026-09-05 00:18 UTC | 2026-08-31 | current |
| [Rhode Island](https://approjects-warn-act-notices.static.hf.space/states/rhode-island.html) (RI) | 126 | 27 | [ri.csv](data/by-state/ri.csv) | 2026-09-05 00:18 UTC | 2026-06-29 | quiet: agency portal checked by hand 2026-09-02, nothing newer published |
| [South Carolina](https://approjects-warn-act-notices.static.hf.space/states/south-carolina.html) (SC) | 604 | 135 | [sc.csv](data/by-state/sc.csv) | 2026-09-05 00:18 UTC | 2026-08-28 | current |
| [South Dakota](https://approjects-warn-act-notices.static.hf.space/states/south-dakota.html) (SD) | 80 | 16 | [sd.csv](data/by-state/sd.csv) | 2026-09-05 00:18 UTC | 2026-08-10 | current |
| [Tennessee](https://approjects-warn-act-notices.static.hf.space/states/tennessee.html) (TN) | 1,061 | 98 | [tn.csv](data/by-state/tn.csv) | 2026-09-05 00:19 UTC | 2026-09-02 | current |
| [Texas](https://approjects-warn-act-notices.static.hf.space/states/texas.html) (TX) | 2,358 | 573 | [tx.csv](data/by-state/tx.csv) | 2026-09-05 00:23 UTC | 2026-06-23 | current; agency posts in batches (see state page) |
| [Utah](https://approjects-warn-act-notices.static.hf.space/states/utah.html) (UT) | 282 | 51 | [ut.csv](data/by-state/ut.csv) | 2026-09-05 00:19 UTC | 2026-08-13 | current |
| [Vermont](https://approjects-warn-act-notices.static.hf.space/states/vermont.html) (VT) | 70 | 16 | [vt.csv](data/by-state/vt.csv) | 2026-09-05 00:19 UTC | 2026-06-17 | quiet: agency portal checked by hand 2026-09-02, nothing newer published |
| [Washington](https://approjects-warn-act-notices.static.hf.space/states/washington.html) (WA) | 1,500 | 281 | [wa.csv](data/by-state/wa.csv) | 2026-09-05 00:20 UTC | 2026-09-03 | current |
| [Wisconsin](https://approjects-warn-act-notices.static.hf.space/states/wisconsin.html) (WI) | 617 | 201 | [wi.csv](data/by-state/wi.csv) | 2026-09-05 00:20 UTC | 2026-08-24 | current |
| [West Virginia](https://approjects-warn-act-notices.static.hf.space/states/west-virginia.html) (WV) | 58 | 38 | [wv.csv](data/by-state/wv.csv) | 2026-09-05 00:23 UTC | 2026-08-19 | current |

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

## Biggest layoff notices — last 30 days (2026-08-06 to 2026-09-05)

| Company | State | Location | Workers | Notice date (or layoff date where the state publishes none) |
|---|---|---|---:|---|
| Tyson Foods | IL | Hillsdale, 28424 38TH Ave. North | 2,495 | 2026-08-13 |
| JBS Souderton | PA | Souderton, Montgomery | 1,485 | layoff 2026-08-14 |
| Borton & Sons | WA | Yakima, Zillah, Pasco, Burbank, Prescott, Soap Lake, Othello, Mesa | 928 | 2026-08-21 |
| 24Hr Homecare | CA | Los Angeles County | 738 | 2026-08-31 |
| Tyson Fresh Meats | UT | Eagle Mountain | 723 | 2026-08-13 |
| Republic National Distributing Company (RNDC) | MI | Delta, Grand Traverse, Kent, Saginaw, Wayne | 641 | layoff 2026-08-17 |
| Gilbert Orchards | WA | Yakima, Franklin and Grant Counties | 518 | 2026-09-03 |
| Jabil | CA | Santa Clara County | 382 | 2026-08-21 |
| Amentum | MD | 7710 Milestone Parkway Hanover, MD 21076 | 382 (2 phases) | 2026-08-18 |
| Uber Technologies | IL | Chicago, 433 West Van Buren St. | 363 | 2026-09-02 |
| Republic National Distributing | GA | National Dr SW Atlanta, Cobb County | 321 | 2026-08-26 |
| Renewal by Andersen | CA | Orange County, Los Angeles County | 284 (3 phases) | 2026-09-01 |
| Healthcare SC | SC | Fairfield | 254 | layoff 2026-08-28 |
| PayPal | CA | Santa Clara County | 251 | 2026-09-01 |
| Sundquist Fruit | WA | Yakima and Franklin Counties | 243 | 2026-09-02 |

_Grouped per notice (a phased notice with several layoff dates counts once, workers summed). 5 row(s) in this window whose state record names only a facility, not an employer, are omitted here but kept in the CSV as published. 3 row(s) are dated by the layoff/closure date and marked "layoff": Michigan, Pennsylvania and South Carolina publish no notice date at all._

## Monthly trend (last 12 months, this dataset)

| Month | Notices | Workers affected |
|---|---:|---:|
| 2025-09 | 250 | 29,309 |
| 2025-10 | 412 | 42,952 |
| 2025-11 | 282 | 24,820 |
| 2025-12 | 133 | 11,787 |
| 2026-01 | 340 | 32,217 |
| 2026-02 | 325 | 26,092 |
| 2026-03 | 306 | 21,550 |
| 2026-04 | 345 | 29,639 |
| 2026-05 | 265 | 42,082 |
| 2026-06 | 332 | 18,544 |
| 2026-07 | 206 | 17,853 |
| 2026-08 | 223 | 20,264 |
| 2026-09 _(month to date, 5 days)_ | 25 | 2,992 |

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

- **[WARN Watch — $49/year, one payment](https://approjects-warn-act-notices.static.hf.space/watch.html)** — up to 25 employer
  terms plus whole-state watches across all 39 covered states, matched on
  every daily refresh for 365 days; hits land on a private alert page + RSS feed
  and, if you paste a webhook URL at checkout, your Slack / Discord / Teams
  channel (no login, no email required).
  [What it checks and its limits](https://approjects-warn-act-notices.static.hf.space/watch.html) · [free 30-day trial](https://approj.gumroad.com/l/warn-free-watch) · [buy](https://approj.gumroad.com/l/warn-watch).
- **[Full historical archive — $199 one-time](https://approj.gumroad.com/l/warn-archive)** — every notice
  we have back to 1988 (45,777 rows, all 39 states), CSV + JSON.

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
