# Replication Repository: Do Modern Prediction Markets Have a Right-Wing Tilt? (2012–2026)

This repository contains the race-level dataset, 2026 midterm market snapshots ($T-14$ and $T-7$), and zero-dependency Python replication scripts for the empirical research on partisan bias in political prediction markets across **$455$ verified U.S. elections (2012–April 2026)** and the **2026 U.S. Midterm Forecasts**.

---

## 1. Repository Contents

| File | Description |
| :--- | :--- |
| `prediction_market_partisan_bias_paper.md` | Full text of the empirical paper, including all tables, plain-English equations, and 2026 midterm log-odds forecasts. |
| `verified_election_markets_2012_2026.csv` | Race-by-race dataset of **455 unique, named U.S. general, runoff, recall, and special elections (2012–April 2026)** across 28 verified columns. |
| `midterm_2026_battlegrounds.csv` | Tabular CSV of the 13 core 2026 U.S. Senate and Governor battlegrounds at $T-14$ (Oct 20) and $T-7$ (Oct 27), including polling averages, trader markups, redness/incumbency/fortress credits, and poll-conditioned log-odds forecasts. |
| `midterm_2026_t7_results.json` | Complete JSON archive of the 2026 $T-14$ and $T-7$ snapshots across all 13 battlegrounds and 3 chambers (Senate, Governors, U.S. House). |
| `replicate_paper_tables.py` | **Primary replication script:** reads `verified_election_markets_2012_2026.csv` and `midterm_2026_t7_results.json` directly from disk and reproduces every table, $p$-value, decomposition, and price-controlled wrong-call regression in the paper. |
| `run_t7_analysis.py` | Reproduces the 2026 $T-14$ and $T-7$ log-odds poll-conditioned de-biasing calculations and regenerates `midterm_2026_t7_results.json` and `midterm_2026_battlegrounds.csv`. |
| `build_verified_dataset.py` | Dataset assembly script that compiles the 455 race-level records, computes the normal-CDF poll win probabilities and Brier scores, writes `verified_election_markets_2012_2026.csv`, and prints the full statistical output. |

---

## 2. Quick-Start Replication (Zero External Dependencies)

All scripts run on **Python 3.9+** using only the Python standard library (`csv`, `json`, `math`, `collections`, `statistics`). No `pip install` is required.

```bash
# 1. Verify all historical tables and price-controlled regressions directly from the CSV:
python3 replicate_paper_tables.py

# 2. Verify the 2026 T-14 and T-7 log-odds battleground and chamber forecasts:
python3 run_t7_analysis.py
```

---

## 3. Dataset Structure & Codebook (`verified_election_markets_2012_2026.csv`)

Every row ($N = 455$) is uniquely identified by `(election_date, office, state_or_district)` and belongs to one of five transparent cohorts:
1. **`Pre2016` Control Era (`2012–2014`, $N = 60$ across $9$ dates):** $20$ presidential contracts in 2012 (`Pre2016_Pres`) and $40$ Senate, gubernatorial, and special elections (`Pre2016_NonPres`). Respects Intrade's March 2013 shutdown (`Intrade` present strictly in 2012).
2. **`Pres_Top` (`2016, 2020, 2024`, $N = 75$ across $3$ dates):** National popular/Electoral College contract plus the $24$ most liquid battleground and lean state/district contracts per cycle ($25$ per cycle).
3. **`Pres_Downballot` (`2016, 2020, 2024`, $N = 95$ across $5$ dates):** Competitive Senate, gubernatorial, and U.S. House elections held in presidential cycles ($22$ in 2016 including the LA Senate runoff, $28$ in 2020 including the two Jan 5, 2021 GA Senate runoffs, and $45$ in Nov 2024 across Kalshi, Polymarket, and PredictIt).
4. **`Midterm_2018` & `Midterm_2022` ($N = 175$ across $3$ dates):** $84$ competitive Senate, governor, and House races in 2018 plus $91$ competitive Senate, governor, statewide (AG/SoS), and House races in 2022 (including the Dec 6, 2022 GA Senate runoff).
5. **`Special_PreDobbs` & `Special_PostDobbs` (`2017–April 2026`, $N = 50$ across $35$ dates):** $25$ pre-*Dobbs* special and off-year elections (April 2017–June 14, 2022) and $25$ post-*Dobbs* special and off-year elections (June 28, 2022–April 2026). Across all cohorts, `Kalshi` is recorded strictly on the $78$ contracts resolved after its October 4, 2024 court-approved launch.

### Column Definitions (`28` Columns)

| Column Name | Type | Definition / Formula |
| :--- | :--- | :--- |
| `race_id` | Integer (`1–455`) | Sequential race identifier. |
| `election_date` | Date (`YYYY-MM-DD`) | Certified election date (used as the cluster identifier $G$ for date-clustered standard errors). |
| `cycle_group` | String | Cohort (`Pre2016_Pres`, `Pre2016_NonPres`, `Pres_Top`, `Pres_Downballot`, `Midterm_2018`, `Midterm_2022`, `Special_PreDobbs`, `Special_PostDobbs`). |
| `era` | String | `Pre2016` ($N=60$) or `Modern` ($N=395$). |
| `office` | String | `Pres`, `Senate`, `Senate_Spec`, `Senate_Runoff`, `Gov`, `Gov_Spec`, `Gov_OffYr`, `Statewide_AG`, `Statewide_SoS`, `Statewide_Spec`, `Statewide_OffYr`, `House`, `House_Spec`. |
| `state_or_district` | String | Two-letter state postal code, congressional district (`PA-07`), or special identifier (`WI-SupCt`). |
| `dem_candidate`, `gop_candidate` | String | Major-party (or independent/coalition) nominees. |
| `seat_status` | Categorical | `Elected_R_Inc` (elected GOP incumbent running), `Open_Appt_R` (open or appointed GOP-held seat), or `Dem_Seat` (Democratic-held seat). |
| `cook_pvi`, `cook_pvi_num` | String / Float | Cycle-specific Cook Partisan Voting Index (positive = Republican lean, negative = Democratic lean). |
| `gop_20yr_win_share` | Integer (`0–100`) | Preceding 20-year Republican win percentage in statewide Senate and gubernatorial elections. |
| `redness_tier` | Categorical | `Red_State` ($\ge 65\%$), `Purple_State` ($35\%\text{–}65\%$), or `Blue_State` ($\le 35\%$). |
| `platforms` | Comma-separated | Active prediction market exchanges for the race (`IEM`, `Intrade`, `Betfair`, `PredictIt`, `Polymarket`, `Kalshi`). |
| `turnout_vep_pct` | Float | Turnout as a percentage of the Voting-Eligible Population ($\text{VEP\%}$). |
| `diverse_or_female_dem` | Binary (`0/1`) | Indicator equal to `1` if the Democratic nominee is female or a racial/ethnic minority, or if the jurisdiction is $\ge 35\%$ non-white. |
| `poll_margin_r_minus_d` | Float | Final pre-election consensus polling average margin ($\text{R\%} - \text{D\%}$, in percentage points). |
| `poll_win_prob_r_55sd` | Float (`0–100`) | Poll-implied Republican win probability: $\Phi(\text{poll\_margin\_r\_minus\_d} / 5.5) \times 100$. |
| `mkt_t1_r` | Float (`0–100`) | Pre-election $T-1$ (day before Election Day) normalized Republican win probability ($\%$). |
| `market_tier` | Categorical | `1_TossUp_45_55` ($45\%\text{–}55\%$), `2_Lean_55_65` ($55\%\text{–}65\%$), `3_Likely_65_85` ($65\%\text{–}85\%$), `4_Safe_gt85` ($>85\%$). |
| `gop_win` | Binary (`0/1`) | Certified election outcome (`1` = Republican win, `0` = Democratic/Independent win). |
| `gop_fav`, `fav_upset` | Binary (`0/1`) | `gop_fav = 1` if `mkt_t1_r > 50`; `fav_upset = 1` if the market favorite ($>50\%$) lost. |
| `net_market_bias_pp` | Float | Exact formula: $\text{mkt\_t1\_r} - 100 \times \text{gop\_win}$. |
| `poll_bias_pp` | Float | Exact formula: $\text{poll\_win\_prob\_r\_55sd} - 100 \times \text{gop\_win}$. |
| `trader_markup_pp` | Float | Exact formula: $\text{mkt\_t1\_r} - \text{poll\_win\_prob\_r\_55sd}$. |
| `brier_mkt`, `brier_poll` | Float | Squared probability error $(\text{prob}/100 - \text{gop\_win})^2$ for market and poll win probabilities. |
