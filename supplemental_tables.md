# Supplemental Statistical Tables: Partisan Pricing Bias in U.S. Political Prediction Markets (2012–2026)

**Author:** Andres Ollarvez  
**Affiliation:** Independent Empirical Research Working Paper — Supplemental Tables Appendix  
**Date:** November 2026  
**Main Working Paper:** [*Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012–2026)*](./partisan_pricing_bias_in_us_political_prediction_markets.md)  
**Replication Data & Code:** [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv) · [`midterm_2026_battlegrounds.csv`](./midterm_2026_battlegrounds.csv) · [`replicate_paper_tables.py`](./replicate_paper_tables.py) · [`run_t7_analysis.py`](./run_t7_analysis.py) · [GitHub Repository](https://github.com/Aollarve/prediction-market-partisan-bias)

---

## Overview

This appendix contains the full, unabbreviated statistical reference tables (**Tables S1–S9**) accompanying [*Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012–2026)*](./partisan_pricing_bias_in_us_political_prediction_markets.md) (**Part I, Tables S1–S6**) together with the locked pre-election 2026 U.S. midterm forecast tables recorded through November 2, 2026 (**Part II, Tables S7–S9**). To keep the tables in the main working paper compact and easy to read, detailed sub-columns—including election date counts (*G*), both date-clustered and race-level exact Student-*t* *p*-values, raw fraction counts (`k/n`), Brier calibration scores, T−14 / T−7 / T−1 2026 market trajectories, and the full 3×3 state-redness-by-incumbency interaction matrix—are reported here alongside the underlying CSV datasets.

Significance levels across all tables: `* p < 0.05`, `** p < 0.01`, `*** p < 0.001`, `NS` = not statistically significant (`p ≥ 0.05`). `pp` denotes percentage points.

**Jump to Table:** [Table S1](#table-s1) · [Table S2](#table-s2) · [Table S3](#table-s3) · [Table S4](#table-s4) · [Table S5](#table-s5) · [Table S6](#table-s6) · [Table S7](#table-s7) · [Table S8](#table-s8) · [Table S9](#table-s9)

---

## Part I: Full Reference Tables for *Partisan Pricing Bias in U.S. Political Prediction Markets* (455 Historical Elections, 2012–April 2026)

<a id="table-s1"></a>
### Table S1: Full Cycle-by-Cycle Market Bias, Trader Win-Odds Markup Over Polls, Favorite Upset Rates, and Brier Scores at T−1 (455 Verified Races)

| Election Group / Era | Races | Dates (G) | Avg Market R Odds | Actual GOP Win % | Net Market Bias | Clustered p (Race p) | Win-Odds Markup vs. Polls | GOP Fav Upset Rate (k/n) | Dem Fav Upset Rate (k/n) | GOP Share of Wrong Calls | Market vs. Poll Brier |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **All Verified (2012–2026)** | 455 | 51 | 53.0% | 47.0% | +6.00 pp | 0.2636 (**0.0007\*\*\***) | **+4.28 pp\*\*\*** | 29.1% (76/261) | 14.9% (29/194) | 72.4% (76/105) | 0.1438 vs. 0.1314 |
| **1. Pre-2016 Control (2012–14)** | 60 | 9 | 46.4% | 45.0% | +1.37 pp | 0.9168 (0.7469) | −0.93 pp (NS) | 11.5% (3/26) | 11.8% (4/34) | 42.9% (3/7) | **0.1050** vs. 0.1107 |
| **2. All Modern (2016–2026)** | 395 | 42 | 54.0% | 47.3% | **+6.70 pp** | 0.2574 (**0.0005\*\*\***) | **+5.07 pp\*\*\*** | 31.1% (73/235) | 15.6% (25/160) | 74.5% (73/98) | 0.1497 vs. 0.1346 |
| **3. Pres Top-of-Ticket (16/20/24)** | 75 | 3 | 53.3% | 62.7% | −9.32 pp | 0.3391 (0.0123\*) | **+3.81 pp\*\*\*** | 2.4% (1/41) | 20.6% (7/34) | 12.5% (1/8) | **0.1062** vs. 0.1098 |
| **4. Pres-Year Down-Ballot (16/20/24)** | 95 | 5 | 54.1% | 60.0% | −5.85 pp | 0.3953 (0.1158) | **+4.24 pp\*\*\*** | 11.8% (6/51) | 27.3% (12/44) | 33.3% (6/18) | **0.1312** vs. 0.1383 |
| **5. Modern Midterms Pool (18 & 22)** | 175 | 3 | 53.8% | 33.7% | **+20.13 pp\*** | **0.0272\* (<0.0001\*\*\*)** | **+6.05 pp\*\*\*** | **52.2% (60/115)** | **6.7% (4/60)** | **93.8% (60/64)** | 0.1818 vs. **0.1476** |
| — **5a. 2018 Midterms Alone** | 84 | 1 | 50.5% | 34.5% | **+15.98 pp\*\*\*** | N/A (**0.0003\*\*\***) | **+6.49 pp\*\*\*** | **49.0% (25/51)** | 9.1% (3/33) | **89.3% (25/28)** | 0.1724 vs. **0.1418** |
| — **5b. 2022 Midterms Alone** | 91 | 2 | 56.9% | 33.0% | **+23.97 pp\*\*** | **0.0059\*\* (<0.0001\*\*\*)** | **+5.64 pp\*\*\*** | **54.7% (35/64)** | **3.7% (1/27)** | **97.2% (35/36)** | 0.1904 vs. **0.1530** |
| **6. Modern Specials / Off-Yr (17–26)** | 50 | 34 | 55.6% | 48.0% | +7.58 pp | 0.2014 (0.1505) | **+5.14 pp\*\*\*** | **21.4% (6/28)** | **9.1% (2/22)** | **75.0% (6/8)** | 0.1377 vs. **0.1189** |
| **7. All Modern Non-Pres (Rows 5+6)** | **225** | **37** | **54.2%** | **36.9%** | **+17.34 pp\*\*\*** | **<0.0001\*\*\* (<0.0001\*\*\*)** | **+5.85 pp\*\*\*** | **46.2% (66/143)** | **7.3% (6/82)** | **91.7% (66/72)** | 0.1720 vs. **0.1412** |
| **8. All Modern Down-Ballot (Rows 4+7)** | **320** | **42** | **54.2%** | **43.8%** | **+10.46 pp** | 0.0518 (**<0.0001\*\*\***) | **+5.37 pp\*\*\*** | **37.1% (72/194)** | **14.3% (18/126)** | **80.0% (72/90)** | 0.1599 vs. **0.1404** |

---

<a id="table-s2"></a>
### Table S2: Full Timeline Breakdown for Pre-2016 vs. Pre-*Dobbs* vs. Post-*Dobbs* Non-Presidential Elections

| Historical Period / Cohort | Races | Dates (G) | Avg Market R Odds | Actual GOP Win % | Win-Odds Markup vs. Polls | Net Market Bias | Clustered p (Race p) | GOP Fav Upset Rate (k/n) | Dem Fav Upset Rate (k/n) | GOP Share of Wrong Calls |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **1. Pre-2016 Control (2012–14)** | 60 | 9 | 46.4% | 45.0% | −0.93 pp (NS) | +1.37 pp | 0.9168 (0.7469) | 11.5% (3/26) | 11.8% (4/34) | 42.9% (3/7) |
| **2. Pre-Dobbs Specials (17–Jun 22)** | 25 | 16 | 54.1% | 56.0% | **+5.29 pp\*\*\*** | −1.88 pp | 0.8557 (0.8197) | 25.0% (4/16) | 22.2% (2/9) | 66.7% (4/6) |
| **3. Pre-Dobbs Non-Pres (17–Jun 22)** | 109 | 17 | 51.3% | 39.4% | **+6.22 pp\*\*\*** | **+11.88 pp\*** | **0.0104\* (0.0022\*\*)** | **43.3% (29/67)** | **11.9% (5/42)** | **85.3% (29/34)** |
| **4. Post-Dobbs Specials (Jul 22–26)** | 25 | 18 | 57.0% | 40.0% | **+4.98 pp\*** | **+17.04 pp\*\*** | **0.0028\*\* (0.0091\*\*)** | 16.7% (2/12) | 0.0% (0/13) | 100.0% (2/2) |
| **5. Post-Dobbs Non-Pres (Jul 22–26)** | 116 | 20 | 57.0% | 34.5% | **+5.49 pp\*\*\*** | **+22.47 pp\*\*\*** | **<0.0001\*\*\* (<0.0001\*\*\*)** | **48.7% (37/76)** | **2.5% (1/40)** | **97.4% (37/38)** |

---

<a id="table-s3"></a>
### Table S3: Separate Effects of State Redness and Seat Incumbency on Actual Wins and Market Bias (225 Non-Presidential Races)

| State Redness or Incumbency Group | Races | Avg Cook PVI | Actual GOP Win Rate (k/n) | 1. Poll Win-Odds Bias | 2. Trader Win-Odds Markup | 3. Total Market Bias | Race-Level p-Value | GOP Fav Upset Rate (k/n) |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **All Non-Presidential** | **225** | R+2.3 | **36.9%** (83/225) | **+11.50 pp\*\*\*** | **+5.85 pp\*\*\*** | **+17.34 pp\*\*\*** | **<0.0001** | 46.2% (66/143) |
| **1. Red States (≥65% 20-Yr GOP)** | **74** | R+8.4 | **64.9%** (48/74) | +3.59 pp (NS) | +1.89 pp\* | **+5.49 pp (NS)** | 0.2359 (NS) | 28.6% (18/63) |
| **2. Purple States (35–65% 20-Yr GOP)** | **72** | R+0.8 | **27.8%** (20/72) | **+15.33 pp\*\*\*** | **+6.85 pp\*\*\*** | **+22.18 pp\*\*\*** | **<0.0001** | 58.1% (25/43) |
| **3. Blue States (≤35% 20-Yr GOP)** | **79** | D+2.1 | **19.0%** (15/79) | **+15.41 pp\*\*\*** | **+8.63 pp\*\*\*** | **+24.04 pp\*\*\*** | **<0.0001** | 62.2% (23/37) |
| **4. GOP-Held Seat (All)** | **124** | R+4.5 | **49.2%** (61/124) | **+11.38 pp\*\*\*** | **+3.93 pp\*\*\*** | **+15.31 pp\*\*\*** | **<0.0001** | 40.0% (40/100) |
| — **4a. Elected GOP Incumbent** | 64 | R+3.2 | **50.0%** (32/64) | **+11.32 pp\*** | **+4.07 pp\*\*\*** | **+15.39 pp\*\*** | **0.0019** | 40.7% (22/54) |
| — **4b. Open / Appt. GOP Seat** | 60 | R+5.9 | **48.3%** (29/60) | **+11.44 pp\*** | **+3.79 pp\*\*\*** | **+15.23 pp\*\*** | **0.0047** | 39.1% (18/46) |
| **5. Dem-Held Seat** | **101** | D+0.5 | **21.8%** (22/101) | **+11.64 pp\*\*** | **+8.19 pp\*\*\*** | **+19.83 pp\*\*\*** | **<0.0001** | **60.5%** (26/43) |

---

<a id="table-s4"></a>
### Table S4: Full 3×3 Interaction of State Redness × Incumbency on Actual GOP Win Rate, Trader Markup, and Total Market Bias (225 Races)

| State Redness Tier | A. Elected GOP Incumbent (64 Races) | B. Open / Appt. GOP Seat (60 Races) | C. Dem-Held Seat (101 Races) | Row Total (225 Races) |
| :-- | :--: | :--: | :--: | :--: |
| **1. Red States (≥65%)** | 65.5% Win / **+8.14 pp Bias** (+2.08 pp Mkp, n=29) | 75.9% Win / **−0.59 pp Bias** (+0.17 pp Mkp, n=29) | 43.8% Win / **+11.69 pp Bias** (+4.66 pp Mkp, n=16) | 64.9% Win / **+5.49 pp Bias** (+1.89 pp Mkp, n=74) |
| **2. Purple States (35–65%)** | 53.3% Win / **+10.47 pp Bias** (+4.93 pp Mkp, n=15) | 25.0% Win / **+33.50 pp Bias** (+6.79 pp Mkp, n=16) | 19.5% Win / **+22.05 pp Bias** (+7.58 pp Mkp, n=41) | 27.8% Win / **+22.18 pp Bias** (+6.85 pp Mkp, n=72) |
| **3. Blue States (≤35%)** | 25.0% Win / **+29.60 pp Bias** (+6.30 pp Mkp, n=20) | 20.0% Win / **+26.33 pp Bias** (+7.59 pp Mkp, n=15) | 15.9% Win / **+20.73 pp Bias** (+10.04 pp Mkp, n=44) | 19.0% Win / **+24.04 pp Bias** (+8.63 pp Mkp, n=79) |
| **Column Total (N = 225)** | 50.0% Win / **+15.39 pp Bias** (+4.07 pp Mkp, n=64) | 48.3% Win / **+15.23 pp Bias** (+3.79 pp Mkp, n=60) | 21.8% Win / **+19.83 pp Bias** (+8.19 pp Mkp, n=101) | 36.9% Win / **+17.34 pp Bias** (+5.85 pp Mkp, N=225) |

---

<a id="table-s5"></a>
### Table S5: Full Platform Breakdown and Voter Turnout (VEP %) Regimes

| Platform or Turnout Subgroup | Verified Races | Avg Market R Odds | Actual GOP Win % | Win-Odds Markup vs. Polls | Net Market Bias | Race-Level p-Value | GOP Fav Upsets (k/n) | Dem Fav Upsets (k/n) |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **1. PredictIt Non-Pres (2017–2024, \$850 Cap)** | 214 | 54.4% | 36.9% | **+5.81 pp\*\*\*** | **+17.47 pp\*\*\*** | **<0.0001** | 47.5% (66/139) | 8.0% (6/75) |
| **2. Polymarket Non-Pres (2021–2026, Crypto)** | 114 | 55.7% | 32.5% | **+5.88 pp\*\*\*** | **+23.21 pp\*\*\*** | **<0.0001** | 50.7% (37/73) | 2.4% (1/41) |
| **3. Kalshi Non-Pres Specials (Oct 2024–Apr 2026)** | 8 | 51.9% | 37.5% | +7.26 pp (NS) | +14.38 pp | 0.1239 (NS) | 0.0% (0/3) | 0.0% (0/5) |
| **4. Kalshi All Down-Ballot (2024 + Specials)** | 53 | 52.8% | 49.1% | **+4.83 pp\*\*\*** | +3.70 pp | 0.4263 (NS) | 11.1% (3/27) | 7.7% (2/26) |
| **5. Kalshi All Verified Contracts (Oct 2024–Apr 2026)** | 78 | 55.0% | 56.4% | **+4.16 pp\*\*\*** | −1.44 pp | 0.6853 (NS) | 6.8% (3/44) | 8.8% (3/34) |
| **6. Specials & Off-Year (14–59% VEP)** | 50 | 55.6% | 48.0% | **+5.14 pp\*\*\*** | +7.58 pp | 0.1505 (NS) | 21.4% (6/28) | 9.1% (2/22) |
| **7. Midterms (42–68% VEP)** | 175 | 53.8% | 33.7% | **+6.05 pp\*\*\*** | **+20.13 pp\*\*\*** | **<0.0001** | 52.2% (60/115) | 6.7% (4/60) |
| **8. Pres-Year Down-Ballot (32–80% VEP)** | 95 | 54.1% | 60.0% | **+4.24 pp\*\*\*** | −5.85 pp | 0.1158 (NS) | 11.8% (6/51) | 27.3% (12/44) |
| **9. Pres Top-of-Ticket (51–80% VEP)** | 75 | 53.3% | 62.7% | **+3.81 pp\*\*\*** | −9.32 pp\* | 0.0123\* | 2.4% (1/41) | 20.6% (7/34) |

---

<a id="table-s6"></a>
### Table S6: Full Breakdown Across the 4 Market Probability Tiers (Toss-Up, Lean, Likely, Safe / Solid) in 225 Non-Presidential Races

| Market Tier & Price Range | Market Pricing Definition | GOP Favored (>50% R): Races, Avg Price, Win %, Upset % | Dem Favored (>50% D): Races, Avg Price, Win %, Upset % | Exact Weighted Net GOP Bias (Markup, p) | Share of Tier Upsets Pro-GOP | Market vs. Poll Brier |
| :-- | :-- | :--: | :--: | :--: | :--: | :--: |
| **1. Toss-Up (45%–55%)** | Dead heat / coin flip; no durable pricing advantage | 28 races (52.8% R): **Won 21.4% (6/28)**, Lost 78.6% (22/28) | 9 races (52.2% D): **Won 77.8% (7/9)**, Lost 22.2% (2/9) | **+29.92 pp\*\*\*** (+10.29 pp Mkp, p = 0.0001) | **91.7% (22/24)** | 0.2608 vs. 0.2087 |
| **2. Lean (55%–65%)** | Clear favorite, within active battleground swing range | 38 races (59.1% R): **Won 26.3% (10/38)**, Lost 73.7% (28/38) | 23 races (59.7% D): **Won 82.6% (19/23)**, Lost 17.4% (4/23) | **+29.05 pp\*\*\*** (+7.65 pp Mkp, p < 0.0001) | **87.5% (28/32)** | 0.2642 vs. 0.2199 |
| **3. Likely (65%–85%)** | Substantial favorite; requires major catalyst to flip | 49 races (73.9% R): **Won 67.3% (33/49)**, Lost 32.7% (16/49) | 28 races (73.3% D): **Won 100.0% (28/28)**, Lost 0.0% (0/28) | **+13.86 pp\*\*** (+5.61 pp Mkp, p = 0.0020) | **100.0% (16/16)** | 0.1622 vs. 0.1373 |
| **4. Safe / Solid (>85%)** | Non-competitive tail; very low upset probability | 28 races (91.2% R): **Won 100.0% (28/28)**, Lost 0.0% (0/28) | 22 races (90.9% D): **Won 100.0% (22/22)**, Lost 0.0% (0/22) | **−0.88 pp (NS)** (+0.71 pp Mkp, p = 0.5148) | N/A (0 upsets) | 0.0089 vs. 0.0014 |
| **Excl. Toss-Ups (≥55%)** | **Clear favorites only (Lean + Likely + Safe)** | **115 races** (73.2% R): Won 61.7% (71/115), **Lost 38.3% (44/115)** | **73 races** (74.3% D): Won 94.5% (69/73), **Lost 5.5% (4/73)** | **+14.87 pp\*\*\*** (+4.97 pp Mkp, p < 0.0001) | **91.7% (44/48)** | 0.1545 vs. 0.1280 |

---

## Part II: Companion 2026 U.S. Midterm Pre-Election Forecast Tables (Locked Through T−1, November 2, 2026)

<a id="table-s7"></a>
### Table S7: Complete 2026 Battleground Market Trajectory (T−14 → T−7 → T−1), Polling Averages, and Trader Markup Compression

| 2026 Battleground Race | Raw (T−14) | Raw (T−7, Oct 27) | Raw (T−1, Nov 2) | T−7 to T−1 GOP Shift | T−1 Poll Avg (D–R) | T−1 Poll Win (R) | GOP Markup (T−7 → T−1) |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **NC Senate (Open, Cooper–Whatley)** | 95% D / 5% R | 96% D / 4% R | **98% D / 2% R** | −2.0 pp R | 51.8%–40.8% | 2.3% R | +0.9 → **−0.3 pp** |
| **ME Senate (Collins\*)** | 66% D / 34% R | 61% D / 39% R | **72.5% D / 27.5% R** | **−11.5 pp R** | 49.9%–46.6% | 27.4% R | +3.9 → **+0.1 pp** |
| **MI Senate (Open)** | 69% D / 31% R | 68% D / 32% R | **78.5% D / 21.5% R** | **−10.5 pp R** | 50.1%–44.8% | 16.8% R | +2.7 → **+4.7 pp** |
| **OH Senate (Husted\*)** | 70% D / 30% R | 67.5% D / 32.5% R | **70.5% D / 29.5% R** | −3.0 pp R | 48.9%–46.1% | 30.5% R | +6.9 → **−1.0 pp** |
| **AK Senate (Sullivan\*)** | 75% D / 25% R | 74% D / 26% R | **72% D / 28% R** | **+2.0 pp R** | 49.2%–47.8% | 40.0% R | −5.2 → **−12.0 pp** |
| **TX Senate (Open)** | 67% D / 33% R | 66% D / 34% R | **75.5% D / 24.5% R** | **−9.5 pp R** | 49.0%–46.5% | 32.5% R | +1.5 → **−8.0 pp** |
| **IA Senate (Open)** | 41% D / 59% R | 42% D / 58% R | **50% D / 50% R** | **−8.0 pp R** | 46.5%–46.8% | 52.2% R | +9.5 → **−2.2 pp** |
| **KS Senate (Marshall\*)** | 38% D / 62% R | 41% D / 59% R | **62% D / 38% R** | **−21.0 pp R** | 49.8%–46.2% | 25.6% R | +16.2 → **+12.4 pp** |
| **NE Senate (Ricketts\*)** | 26% I / 74% R | 29% I / 71% R | **28.5% I / 71.5% R** | +0.5 pp R | 45.8%–48.3% | 67.5% R | +18.8 → **+4.0 pp** |
| **GA Gov (Open)** | 60% D / 40% R | 61% D / 39% R | **69% D / 31% R** | **−8.0 pp R** | 47.3%–48.3% | 57.2% R | −12.5 → **−26.2 pp** |
| **NV Gov (Lombardo\*)** | 66% D / 34% R | 76% D / 24% R | **75.5% D / 24.5% R** | +0.5 pp R | 43.7%–43.7% | 50.0% R | −26.0 → **−25.5 pp** |
| **TX Gov (Abbott\*)** | 36% D / 64% R | 34% D / 66% R | **39% D / 61% R** | **−5.0 pp R** | 47.3%–49.8% | 67.5% R | −0.2 → **−6.5 pp** |
| **VT Gov (P. Scott\*)** | 26% D / 74% R | 23% D / 77% R | **31% D / 69% R** | **−8.0 pp R** | 45.0%–44.8% | 48.5% R | −5.3 → **+20.5 pp** |
| **FL Gov (Open, Jolly–Donalds)** | 28% D / 72% R | 30% D / 70% R | **34.5% D / 65.5% R** | **−4.5 pp R** | 44.3%–48.3% | 76.6% R | −9.3 → **−11.1 pp** |
| **KS Gov (Open, Holscher–Masterson)** | 25% D / 75% R | 23% D / 77% R | **30% D / 70% R** | **−7.0 pp R** | 47.0%–48.8% | 62.8% R | −1.8 → **+7.2 pp** |

---

<a id="table-s8"></a>
### Table S8: Complete 2026 Midterm Chamber Predictions Across T−14, October 27 (T−7), and November 2 (T−1) With 45%–55% Toss-Ups Uncalled

| Chamber (Majority) | Not Up (D/R) | Raw Market (T−14 → T−7 → T−1) | Simple Log-Odds (T−14 → T−7 → T−1) | Preferred (T−14) | Preferred (T−7, Oct 27) | Final Preferred Log-Odds Forecast (T−1, Nov 2) |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| **U.S. Senate (51)** | **34 D / 31 R** | 52–48 → 52–48 → **53 D–46 R** (1 TU: IA) | 54–46 → 54–45 (1 TU) → **54 D–46 R** (0 TU) | 53 D–46 R (1 TU: KS) | 53 D–46 R (1 TU: KS) | **54 D–46 R, 0 Toss-Ups** (IA Lean D 64.2%; KS Likely D 69.4%; NE Likely R 66.2%) |
| **Governors (26)** | **6 D / 8 R** | 28–22 → 28–22 → **28 D–22 R** (0 TU) | 28–21 (1 TU) → 28–20 (2 TU) → **29 D–18 R** (3 TU: VT, FL, KS) | 28 D–22 R (0 TU) | 28 D–22 R (0 TU) | **28 D–22 R, 0 Toss-Ups** (TX 56.7% R; VT 58.5% R; FL 55.4% R; KS 55.2% R) |
| **U.S. House (218)** | All 435 Up | 229–195 (11 TU) → 234–192 (9 TU) → **237 D–194 R** (4 TU) | 251–174 → 254–172 → **250 D–172 R** (13 TU) | 241 D–185 R (9 TU) | 244 D–183 R (8 TU) | **243 D–181 R, 11 Toss-Ups** (+6 called D, −13 called R vs. T−1 raw) |

---

<a id="table-s9"></a>
### Table S9: Complete Race-by-Race 2026 Battleground Win-Probability Predictions Across T−14, October 27 (T−7), and November 2 (T−1)

| 2026 Battleground Race | Inc & Certified 2006–25 R (2025 PVI) | GOP Credit (Red+Inc+Int) | Preferred (T−14) | Raw → Preferred (T−7) | Raw Market (T−1, Nov 2) | Simple Log-Odds (T−1) | Preferred Log-Odds Forecast & Call (T−1, Nov 2) |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **NC Senate (Open)** | Open, 54.5% [6/11] (R+1) | +0.88+0.00+0.00 = **+0.88** | 97.4% D (Safe D) | 96.0% → **97.9% D** (Safe D) | 98.0% D / 2.0% R (Safe D) | 99.0% D (Safe D) | **99.0% D / 1.0% R — Safe / Solid D** |
| **ME Senate (Collins\*)** | Elected R, 50.0% [6/12] (D+4) | +0.67+5.50+0.82 = **+6.99** | 74.8% D (Likely D) | 61.0% → **70.5% D** (Likely D) | 72.5% D / 27.5% R (Likely D) | 84.1% D (Likely D) | **80.1% D / 19.9% R — Likely D** |
| **MI Senate (Open)** | Open, 16.7% [2/12] (EVEN) | +0.00+0.00+0.00 = **+0.00** | 81.9% D (Likely D) | 68.0% → **81.2% D** (Likely D) | 78.5% D / 21.5% R (Likely D) | 88.0% D (Safe D) | **88.1% D / 11.9% R — Safe / Solid D** |
| **OH Senate (Husted\*)** | Appt. R, 66.7% [8/12] (R+5) | +1.43+2.48+0.78 = **+4.69** | 79.6% D (Likely D) | 67.5% → **77.7% D** (Likely D) | 70.5% D / 29.5% R (Likely D) | 82.8% D (Likely D) | **79.8% D / 20.2% R — Likely D** |
| **AK Senate (Sullivan\*)** | Elected R, 81.8% [9/11] (R+6) | +2.11+5.50+2.57 = **+10.18** | 79.4% D (Likely D) | 74.0% → **78.5% D** (Likely D) | 72.0% D / 28.0% R (Likely D) | 83.8% D (Likely D) | **75.7% D / 24.3% R — Likely D** |
| **TX Senate (Open)** | Open, 100.0% [12/12] (R+6) | +2.92+0.00+0.00 = **+2.92** | 78.5% D (Likely D) | 66.0% → **77.8% D** (Likely D) | 75.5% D / 24.5% R (Likely D) | 86.1% D (Safe D) | **82.9% D / 17.1% R — Likely D** |
| **IA Senate (Open)** | Open, 81.8% [9/11] (R+6) | +2.11+0.00+0.00 = **+2.11** | 56.4% D (Lean D) | 42.0% → **57.4% D** (Lean D) | 50.0% D / 50.0% R (Toss-Up) | 66.8% D (Likely D) | **64.2% D / 35.8% R — Lean D** |
| **KS Senate (Marshall\*)** | Elected R, 72.7% [8/11] (R+8) | +1.70+5.50+2.07 = **+9.27** | 46.0% D (Toss-Up) | 41.0% → **49.1% D** (Toss-Up) | 62.0% D / 38.0% R (Lean D) | 76.7% D (Likely D) | **69.4% D / 30.6% R — Likely D** |
| **NE Senate (Ricketts\*)** | Elected R, 92.3% [12/13] (R+10) | +2.58+5.50+3.15 = **+11.23** | 31.1% I (Likely R) | 29.0% → **34.4% I** (Likely R) | 28.5% I / 71.5% R (Likely R) | 44.5% I (Lean R) | **33.8% I / 66.2% R — Likely R** |
| **GA Gov (Open)** | Open, 75.0% [9/12] (R+1) | +1.80+0.00+0.00 = **+1.80** | 69.3% D (Likely D) | 61.0% → **70.2% D** (Likely D) | 69.0% D / 31.0% R (Likely D) | 81.8% D (Likely D) | **72.3% D / 27.7% R — Likely D** |
| **NV Gov (Lombardo\*)** | Elected R, 50.0% [6/12] (R+1) | +0.67+5.50+0.82 = **+6.99** | 68.4% D (Likely D) | 76.0% → **77.9% D** (Likely D) | 75.5% D / 24.5% R (Likely D) | 86.1% D (Safe D) | **77.6% D / 22.4% R — Likely D** |
| **TX Gov (Abbott\*)** | Elected R, 100.0% [12/12] (R+6) | +2.92+5.50+3.58 = **+12.00** | 41.1% D (Lean R) | 34.0% → **39.0% D** (Lean R) | 39.0% D / 61.0% R (Lean R) | 56.3% D (Lean D) | **43.3% D / 56.7% R — Lean R** |
| **VT Gov (P. Scott\*)** | Elected R, 41.2% [7/17] (D+17) | +0.28+5.50+0.34 = **+6.12** | 34.1% D (Likely R) | 23.0% → **30.6% D** (Likely R) | 31.0% D / 69.0% R (Likely R) | 47.5% D (Toss-Up) | **41.5% D / 58.5% R — Lean R** |
| **FL Gov (Open)** | Open, 83.3% [10/12] (R+5) | +2.17+0.00+0.00 = **+2.17** | 38.0% D (Lean R) | 30.0% → **40.3% D** (Lean R) | 34.5% D / 65.5% R (Likely R) | 51.5% D (Toss-Up) | **44.6% D / 55.4% R — Lean R** |
| **KS Gov (Open)** | Open, 72.7% [8/11] (R+8) | +1.70+0.00+0.00 = **+1.70** | 37.9% D (Lean R) | 23.0% → **35.4% D** (Lean R) | 30.0% D / 70.0% R (Likely R) | 46.3% D (Toss-Up) | **44.8% D / 55.2% R — Lean R** |
