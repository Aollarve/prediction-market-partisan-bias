# Partisan Pricing Bias in U.S. Political Prediction Markets (2012–2026)

**Author:** Andres Ollarvez

> [!IMPORTANT]
> **Read the Full Working Paper:**  
> **[Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012–2026)](./partisan_pricing_bias_in_us_political_prediction_markets.md)**
>
> **Quick Links:** [Full Paper](./partisan_pricing_bias_in_us_political_prediction_markets.md) · [Supplemental Statistical Tables (S1–S9)](./supplemental_tables.md) · [455-Election Dataset (CSV)](./verified_election_markets_2012_2026.csv) · [Replication Script (`replicate_paper_tables.py`)](./replicate_paper_tables.py)

---

## Executive Summary & Headline Findings

Prediction markets such as Kalshi, Polymarket, and PredictIt are widely cited alongside election polls on the assumption that profit-seeking traders strip out partisan bias. Across **455 verified U.S. elections from 2012 to April 2026** (*G* = 51 distinct election dates), this repository documents four core empirical patterns:

1. **Pre-2016 Neutrality vs. Post-2015 Trader Markup:** Before 2016 (*N* = 60), political betting markets showed no partisan tilt (+1.37 percentage points [pp], *p* = 0.9168). Since 2016, traders have priced Republican win probabilities **+3.81 to +6.49 pp higher** than poll-implied win probabilities across every election cohort (*p* < 0.001 in each).
2. **Presidential Years vs. Midterms and Specials:** When Donald Trump was on the ballot (2016, 2020, 2024), state polls underestimated Republicans, so that trader markup beat the polls. In modern midterms and special elections (*N* = 225 across 37 dates), poll-implied win odds already leaned +11.50 pp too Republican and traders added +5.85 pp of markup on top—producing a **+17.34 pp pro-Republican bias** (*p* < 0.0001) that held both pre-*Dobbs* (+11.88 pp, *p* = 0.0104) and post-*Dobbs* (+22.47 pp, *p* < 0.0001).
3. **The Wrong-Call Test:** Holding contract prices above 50¢ constant across modern non-presidential races, Republican favorites lost **46.2% of the time (66/143)** compared to **7.3% (6/82)** for Democratic favorites (**+34.72 pp** excess upset rate, *p* < 0.0001), including **73.7% losses (28/38)** among 55%–65% Lean R favorites.
4. **State History & Brier Calibration:** Traders accurately reflect Republican winning streaks in Red States (+5.49 pp bias, *p* = 0.2359) while discounting Democratic history in Blue States (+8.63 pp markup over polls; +24.04 pp total error). Consequently, markets beat bell-curve polling benchmarks before 2016 and in presidential cycles, but trail simple poll benchmarks in modern non-presidential elections (**0.1720 vs. 0.1412 Brier**).

| Election Regime (T−1 Closing Odds) | Races (Dates) | Net Market Bias | Trader Markup Over Polls | GOP vs. Dem Fav Upset % | Market vs. Poll Brier |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Pre-2016 Control (2012–2014)** | 60 (9) | +1.37 pp (NS) | −0.93 pp (NS) | 11.5% vs. 11.8% | **0.1050** vs. 0.1107 |
| **Pres Top-of-Ticket (2016, 2020, 2024)** | 75 (3) | −9.32 pp\* | **+3.81 pp\*\*\*** | 2.4% vs. 20.6% | **0.1062** vs. 0.1098 |
| **Pres-Year Down-Ballot (2016, 2020, 2024)** | 95 (5) | −5.85 pp (NS) | **+4.24 pp\*\*\*** | 11.8% vs. 27.3% | **0.1312** vs. 0.1383 |
| **Modern Midterms (2018 & 2022)** | 175 (3) | **+20.13 pp\*** | **+6.05 pp\*\*\*** | **52.2% vs. 6.7%** | 0.1818 vs. **0.1476** |
| **Modern Specials & Off-Year (2017–2026)** | 50 (34) | +7.58 pp (NS) | **+5.14 pp\*\*\*** | **21.4% vs. 9.1%** | 0.1377 vs. **0.1189** |
| **All Modern Non-Presidential** | **225 (37)** | **+17.34 pp\*\*\*** | **+5.85 pp\*\*\*** | **46.2% vs. 7.3%** | 0.1720 vs. **0.1412** |

**[Read the full working paper →](./partisan_pricing_bias_in_us_political_prediction_markets.md)**

---

## 1. Repository Contents

| File | Description |
| :--- | :--- |
| [`partisan_pricing_bias_in_us_political_prediction_markets.md`](./partisan_pricing_bias_in_us_political_prediction_markets.md) | **Working Paper:** *Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012–2026)* — full empirical study, methodology, tables, limitations, disclosures, and references. |
| [`supplemental_tables.md`](./supplemental_tables.md) | **Supplemental Statistical Tables (Tables S1–S9):** Complete, unabbreviated multi-column statistical reference tables (with date counts *G*, date-clustered and race-level exact Student-*t* *p*-values, raw `k/n` fractions, Brier scores, the full 3×3 State Redness × Incumbency matrix, and locked 2026 pre-election trajectories). |
| [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv) | **Historical Dataset (*N* = 455):** Race-by-race dataset of 455 unique, named U.S. general, runoff, recall, and special elections (2012–April 2026) across 28 verified columns (*G* = 51 distinct election dates). |
| [`replicate_paper_tables.py`](./replicate_paper_tables.py) | **Primary Replication Script:** Zero-dependency Python script that reads `verified_election_markets_2012_2026.csv` and `midterm_2026_t7_results.json` directly from disk and reproduces every table, exact Student-*t* *p*-value, decomposition, Brier calibration score, and price-controlled wrong-call regression. |
| [`midterm_2026_battlegrounds.csv`](./midterm_2026_battlegrounds.csv) | **2026 Pre-Election Battleground Snapshot (*N* = 13):** Locked pre-election dataset of the 13 core 2026 U.S. Senate and Governor battlegrounds across 48 columns (T−14, October 27 T−7, and November 2 T−1 market odds, consensus polling averages, trader markups, structural credits, and log-odds de-biased probabilities). |
| [`midterm_2026_t7_results.json`](./midterm_2026_t7_results.json) | **2026 Pre-Election JSON Archive:** Complete JSON archive of the locked 2026 T−14, T−7, and T−1 battleground and chamber-wide projections (Senate, Governors, and U.S. House) recorded ahead of November 3, 2026. |
| [`run_t7_analysis.py`](./run_t7_analysis.py) | **2026 Pre-Election Forecast Script:** Zero-dependency Python script reproducing the 2026 T−14, T−7, and T−1 poll-conditioned log-odds de-biasing calculations and regenerating `midterm_2026_t7_results.json` and `midterm_2026_battlegrounds.csv`. |

---

## 2. Quick-Start Replication (Zero External Dependencies)

All scripts run on **Python 3.9+** using only the Python standard library (`csv`, `json`, `math`, `collections`, `statistics`). No `pip install` is required.

```bash
# 1. Reproduce all historical tables, exact Student-t p-values, Brier scores, and wrong-call regressions:
python3 replicate_paper_tables.py

# 2. Reproduce the locked 2026 T-14, T-7, and T-1 battleground and chamber forecasts:
python3 run_t7_analysis.py
```

---

## 3. Historical Dataset Codebook (`verified_election_markets_2012_2026.csv`)

Every row (*N* = 455) is uniquely identified by `(election_date, office, state_or_district)` and belongs to one of five cohorts:

1. **`Pre2016` Control Era (2012–2014, *N* = 60 across 9 dates):** 20 presidential contracts in 2012 (`Pre2016_Pres`) and 40 Senate, gubernatorial, and special elections (`Pre2016_NonPres`). Respects Intrade's March 2013 shutdown (`Intrade` recorded strictly in 2012).
2. **`Pres_Top` (2016, 2020, 2024, *N* = 75 across 3 dates):** National contract plus the 24 most liquid battleground and lean state/district contracts per cycle (25 per cycle).
3. **`Pres_Downballot` (2016, 2020, 2024, *N* = 95 across 5 dates):** Competitive Senate, gubernatorial, and U.S. House elections held in presidential cycles (22 in 2016 including the Dec 10 LA Senate runoff, 28 in 2020 including the two Jan 5, 2021 GA Senate runoffs, and 45 in Nov 2024 across Kalshi, Polymarket, and PredictIt).
4. **`Midterm_2018` & `Midterm_2022` (*N* = 175 across 3 dates):** 84 competitive Senate, governor, and House races in 2018 plus 91 competitive Senate, governor, statewide (AG/SoS), and House races in 2022 (including the Dec 6, 2022 GA Senate runoff).
5. **`Special_PreDobbs` & `Special_PostDobbs` (2017–April 2026, *N* = 50 across 34 dates):** 25 pre-*Dobbs* special and off-year elections (May 2017–June 14, 2022 across 16 dates) and 25 post-*Dobbs* special and off-year elections (June 28, 2022–April 2026 across 18 dates). Across all cohorts, `Kalshi` is recorded strictly on the 78 contracts resolved after its October 4, 2024 court-approved launch.

<details>
<summary><strong>Click to expand all 28 column definitions in <code>verified_election_markets_2012_2026.csv</code></strong></summary>

| Column Name | Type | Definition / Formula |
| :--- | :--- | :--- |
| `race_id` | Integer (`1–455`) | Sequential race identifier. |
| `election_date` | Date (`YYYY-MM-DD`) | Certified election date (cluster identifier *G* for date-clustered standard errors). |
| `cycle_group` | String | Cohort (`Pre2016_Pres`, `Pre2016_NonPres`, `Pres_Top`, `Pres_Downballot`, `Midterm_2018`, `Midterm_2022`, `Special_PreDobbs`, `Special_PostDobbs`). |
| `era` | String | `Pre2016` (*N* = 60) or `Modern` (*N* = 395). |
| `office` | String | `Pres`, `Senate`, `Senate_Spec`, `Senate_Runoff`, `Gov`, `Gov_Spec`, `Gov_OffYr`, `Statewide_AG`, `Statewide_SoS`, `Statewide_Spec`, `Statewide_OffYr`, `House`, `House_Spec`. |
| `state_or_district` | String | Two-letter state postal code, congressional district (`PA-07`), or special identifier (`WI-SupCt`). |
| `dem_candidate`, `gop_candidate` | String | Major-party (or independent/coalition) nominees. |
| `seat_status` | Categorical | `Elected_R_Inc` (elected GOP incumbent running), `Open_Appt_R` (open or appointed GOP-held seat), or `Dem_Seat` (Democratic-held seat). |
| `cook_pvi`, `cook_pvi_num` | String / Float | Cycle-specific Cook Partisan Voting Index (positive = Republican lean, negative = Democratic lean). |
| `gop_20yr_win_share` | Integer (`0–100`) | Preceding 20-year Republican win percentage in statewide Senate and gubernatorial elections. |
| `redness_tier` | Categorical | `Red_State` (≥65%), `Purple_State` (35%–65%), or `Blue_State` (≤35%). |
| `platforms` | Comma-separated | Active prediction market exchanges for the race (`IEM`, `Intrade`, `Betfair`, `PredictIt`, `Polymarket`, `Kalshi`). |
| `turnout_vep_pct` | Float | Turnout as a percentage of the Voting-Eligible Population (VEP%). |
| `diverse_or_female_dem` | Binary (`0/1`) | `1` if the Democratic nominee is female or a racial/ethnic minority, or if the jurisdiction is ≥35% non-white. |
| `poll_margin_r_minus_d` | Float | Final pre-election consensus polling average margin (`R% - D%`, in percentage points). |
| `poll_win_prob_r_55sd` | Float (`0–100`) | Poll-implied Republican win probability: `Phi(poll_margin_r_minus_d / 5.5) * 100`. |
| `mkt_t1_r` | Float (`0–100`) | Pre-election T−1 (day before Election Day) normalized Republican win probability (%). |
| `market_tier` | Categorical | `1_TossUp_45_55` (45%–55%), `2_Lean_55_65` (55%–65%), `3_Likely_65_85` (65%–85%), `4_Safe_gt85` (>85%). |
| `gop_win` | Binary (`0/1`) | Certified election outcome (`1` = Republican win, `0` = Democratic/Independent win). |
| `gop_fav`, `fav_upset` | Binary (`0/1`) | `gop_fav = 1` if `mkt_t1_r > 50`; `fav_upset = 1` if the market favorite (>50%) lost. |
| `net_market_bias_pp` | Float | `mkt_t1_r - 100 * gop_win`. |
| `poll_bias_pp` | Float | `poll_win_prob_r_55sd - 100 * gop_win`. |
| `trader_markup_pp` | Float | `mkt_t1_r - poll_win_prob_r_55sd`. |
| `brier_mkt`, `brier_poll` | Float | Squared probability error `(prob / 100 - gop_win)^2` for market and poll win probabilities. |

</details>

---

## 4. 2026 Midterm Pre-Election Battlegrounds Codebook (`midterm_2026_battlegrounds.csv`)

Contains the 13 high-liquidity 2026 U.S. Senate (9) and Governor (4) battleground contracts tracked pre-election across Kalshi and Polymarket (\$240.5M direct volume at T−1, recorded ahead of November 3, 2026):

- **Structural & Baseline Fields:** `race`, `chamber`, `inc` (`Open`, `Appt. R`, `Elected R`), `inc_mult`, `pvi`, `gop_20yr`, `gop_20yr_ratio`, `redness_alone_credit`, `incumbency_alone_credit`, `interaction_credit`, `total_gop_credit`.
- **T−14 Snapshot (Oct 20, 2026):** `t14_d`, `t14_r`, `t14_simple_d`, `t14_pref_d`, `t14_pref_r`, `t14_rating`.
- **T−7 Snapshot (Oct 27, 2026):** `t7_d`, `t7_r`, `poll_d`, `poll_r`, `vol_m`, `poll_margin_r`, `poll_win_d`, `poll_win_r`, `t7_trader_markup_r`, `t14_to_t7_shift_r`, `logit_shift_d`, `t7_simple_d`, `t7_pref_d`, `t7_pref_r`, `t7_rating`.
- **T−1 Snapshot (Nov 2, 2026):** `t1_d`, `t1_r`, `t1_poll_d`, `t1_poll_r`, `t1_vol_m`, `t1_poll_margin_r`, `t1_poll_win_d`, `t1_poll_win_r`, `t1_trader_markup_r`, `t7_to_t1_shift_r`, `t14_to_t1_shift_r`, `t1_logit_shift_d`, `t1_simple_d`, `t1_pref_d`, `t1_pref_r`, `t1_rating`.

---

## 5. Citation & Disclaimer

```text
Ollarvez, A. (2026). Partisan Pricing Bias in U.S. Political Prediction Markets:
Empirical Evidence Across 455 Elections (2012–2026). Independent Empirical Research
Working Paper. https://github.com/Aollarve/prediction-market-partisan-bias
```

*Independent Research Disclaimer:* All research, code, and papers in this repository were produced independently by the author in a personal capacity and do not represent the views, positions, policies, or endorsements of any employer, parent or affiliated entity, or client. Nothing in this repository constitutes financial, investment, legal, or wagering advice.
