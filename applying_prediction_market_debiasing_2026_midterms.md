# Applying Prediction Market De-Biasing to the 2026 U.S. Midterms: Poll-Conditioned Log-Odds Forecasts Through T−1 for the Senate, Governors, and House

**Author:** Andres Ollarvez  
**Affiliation:** Independent Empirical Forecast Working Paper  
**Updated:** November 2, 2026 (T−1 Final Pre-Election Snapshot; Baseline Model Locked Prior to October 27 and Tracked Across T−14, October 27 T−7, and November 2 T−1 Ahead of the November 3, 2026 U.S. Midterm Elections)  
**Baseline Historical Study:** [*Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012–2026)*](./partisan_pricing_bias_in_us_political_prediction_markets.md)  
**Replication Data, Full Tables & Code:** [`midterm_2026_battlegrounds.csv`](./midterm_2026_battlegrounds.csv) · [`supplemental_tables.md`](./supplemental_tables.md) · [`midterm_2026_t7_results.json`](./midterm_2026_t7_results.json) · [`run_t7_analysis.py`](./run_t7_analysis.py) · [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv) · [GitHub Repository](https://github.com/Aollarve/prediction-market-partisan-bias)

---

## Abstract

Ahead of the November 3, 2026 U.S. midterm elections, political event contracts on Kalshi and Polymarket have drawn over \$1.4 billion in trading volume. In my historical baseline study of 455 U.S. elections from 2012 to April 2026 ([*Partisan Pricing Bias in U.S. Political Prediction Markets*](./partisan_pricing_bias_in_us_political_prediction_markets.md)), I showed that modern non-presidential prediction markets (*N* = 225 across 37 dates) overstated Republican win probabilities at T−1 by **+17.34 percentage points [pp]** (*p* < 0.0001), combining +11.50 pp of poll win-odds bias with +5.85 pp of trader markup. Tracking all 15 competitive 2026 statewide battlegrounds across T−14 (October 20), T−7 (October 27, \$153.6 million volume), and T−1 (November 2, \$255.5 million volume) reveals a striking two-phase pattern: after drifting +0.71 pp more Republican from T−14 to T−7 and pricing Senate Republicans +6.13 pp above poll win odds, institutional markets reversed course in the final week, shifting **−7.82 pp toward Democrats** (volume-weighted) and compressing the mean Senate trader markup to **−0.26 pp** by T−1.

To adjust 2026 market prices without pushing probabilities past 100%, erasing genuine Red-State and incumbent advantages, or double-counting races where traders already price Democrats ahead of the polls, I apply a frozen **poll-conditioned log-odds de-biasing model** with separated State Redness, Incumbency, and Fortress credits ([`run_t7_analysis.py`](./run_t7_analysis.py)). Notably, raw T−1 Senate market prices (**53 D–46 R**, 1 Toss-Up) converged onto the exact seat count projected a week earlier by my T−7 de-biased model (**53 D–46 R**, 1 Toss-Up). Leaving 45%–55% Toss-Ups uncalled (No Call), the final November 2 (T−1) model projects Democrats winning the **U.S. Senate 54 D–46 R** with **0 Toss-Ups** (open-seat Iowa at 64.2% D Lean D; Kansas at 69.4% D Likely D; Nebraska held by Ricketts at 66.2% R Likely R), **Governors 28 D–22 R** with **0 Toss-Ups** (+4 net Democratic governorships), and the **U.S. House 243 D–181 R** with **11 Toss-Ups** (+6 called Democratic seats and −13 called Republican seats relative to raw T−1 market odds).

---

> [!IMPORTANT]
> **Final T−1 Pre-Election Forecasts at a Glance (Locked November 2, 2026; 45%–55% Toss-Ups Uncalled)**
> - **Two-Phase 2026 Market Dynamics:** Across 15 statewide battlegrounds (\$255.5M volume), Republican odds drifted **+0.71 pp higher** from T−14 to T−7 (+6.13 pp Senate trader markup over polls) before reversing **−7.82 pp toward Democrats** between T−7 and T−1, compressing the mean Senate markup to **−0.26 pp**.
> - **U.S. Senate — 54 D–46 R (0 Toss-Ups):** Raw T−1 markets (53 D–46 R, 1 Toss-Up) converged onto my locked T−7 de-biased seat count; at T−1, poll-conditioned log-odds de-biasing places open-seat **Iowa at 64.2% D (Lean D)** and **Kansas at 69.4% D (Likely D)** while keeping **Nebraska at 66.2% R (Likely R)**.
> - **Governors — 28 D–22 R (0 Toss-Ups):** Separated fortress, redness, and poll-conditioning credits keep incumbents **Greg Abbott (TX, 56.7% R Lean R)** and **Phil Scott (VT, 58.5% R Lean R)** plus open-seat Republicans **Byron Donalds (FL, 55.4% R Lean R)** and **Ty Masterson (KS, 55.2% R Lean R)** favored while projecting Democratic flips in **Nevada (77.6% D)** and **Georgia (72.3% D)** (+4 net Democratic governorships from 26 R–24 D).
> - **U.S. House — 243 D–181 R (11 Toss-Ups):** Adds +6 called Democratic seats and moves 11 vulnerable 56%–68% R seats into uncalled Toss-Ups relative to raw T−1 Kalshi district odds (237 D–194 R, 4 Toss-Ups).

**Contents:** [1. Introduction](#sec-1) · [2. 2026 Market Data (T−14 to T−1)](#sec-2) · [3. Poll-Conditioned Log-Odds Methodology](#sec-3) · [4. 2026 Chamber & Battleground Predictions](#sec-4) · [5. Limitations & Falsification Tests](#sec-5) · [6. Conclusion](#sec-6) · [Disclosures](#sec-disclosures) · [References & Citation](#sec-references)

---

<a id="sec-1"></a>
## 1. Introduction: Why 2026 Midterm Odds Require Conditional De-Biasing

### 1.1 Empirical Baseline From the 455-Election Historical Study
November 3, 2026 is the first national U.S. midterm election with legal, uncapped federal event contracts on Kalshi alongside high-liquidity crypto and CFTC-regulated order books on Polymarket (Lazarus / Council on Foreign Relations, 2026; Crane & Strumpf, 2026). While recent working papers find little partisan bias when pooling presidential and historical markets (Zitzewitz, 2026; Crane & Strumpf, 2026), my baseline study of 455 verified U.S. elections from 2012 to April 2026 ([*Partisan Pricing Bias in U.S. Political Prediction Markets*](./partisan_pricing_bias_in_us_political_prediction_markets.md)) isolates three structural patterns in modern **non-presidential** elections (225 midterm, special, and off-year races across 37 dates) that govern how 2026 midterm prices should be interpreted:
1. **Substantial pro-Republican non-presidential bias (+17.34 pp).** Where **percentage points (pp)** measure the arithmetic difference between two percentages (for example, a shift from 50% to 56% is +6 pp), modern non-presidential markets priced Republican win odds at 54.2% when Republicans won 36.9% of the time—a **+17.34 pp** error (date-clustered *p* < 0.0001) composed of +11.50 pp in poll win-odds bias plus +5.85 pp in trader markup. This bias held both pre-*Dobbs* (+11.88 pp, clustered *p* = 0.0104) and post-*Dobbs* (+22.47 pp, clustered *p* < 0.0001).
2. **What I call the wrong-call test and the 55%–65% Lean R trap.** Holding contract prices above 50¢ constant, Republican favorites lost **46.2% of the time (66/143)** compared to **7.3% (6/82)** for Democratic favorites (+34.72 pp excess upset rate, *p* < 0.0001). In the 55%–65% Lean tier, Lean R favorites lost **73.7% of the time (28/38)**, while 45%–55% Toss-Ups behaved as noisy coin flips that should remain uncalled.
3. **Red-State and incumbent fortresses versus open-seat traps.** In Red States (≥65% 20-year statewide GOP win share), market bias was statistically indistinguishable from zero (+5.49 pp, *p* = 0.2359), and elected Republican incumbents in Red and Purple states won 65.5% and 53.3% of their races. By contrast, open/appointed Republican seats in Purple States (+33.50 pp bias) and contests in Blue States (≤35% GOP history, +24.04 pp bias) accounted for the bulk of market misses.

### 1.2 Why a Naive Flat Shift Fails in 2026
Applying a flat +17 pp linear adjustment to every 2026 Democrat would commit three forecasting errors:
- **Boundary violations:** In high-probability contracts like North Carolina Senate (96% D at T−7 and 98% D at T−1), adding +17 pp produces an impossible >100% D win probability.
- **Erasing structural fortresses:** Treating a 5-term Republican governor like Phil Scott in Vermont, 3-term incumbent Greg Abbott in Texas, or elected Red-State incumbent Pete Ricketts in Nebraska identically to an open Senate seat ignores the real electoral advantage of incumbency and state partisanship.
- **Double-counting institutional adjustments:** Where 2026 institutional traders have already priced a Democrat above the polls based on early-vote data or late survey waves (such as Nevada Governor, Georgia Governor, or Texas Senate at T−1), adding a full historical trader-markup correction would adjust for the same information twice.

---

<a id="sec-2"></a>
## 2. The 2026 Midterm Market Data (T−14, October 27 T−7, and November 2 T−1)

### 2.1 Contract Normalization and Polling Win-Probability Benchmark
To remove exchange vig and fee spreads on Kalshi and Polymarket, raw binary contract prices are normalized to sum to 100%:

$$\text{Market Win Chance (R)} = \frac{\text{Raw R Price}}{\text{Raw R Price} + \text{Raw D Price}}$$

Following Shirani-Mehr, Rothschild, Goel, and Gelman (2018) and Silver (2018), I convert each battleground's pre-election two-party polling average into a bell-curve **Poll Win Odds** benchmark using a normal cumulative distribution function ($\Phi$) with a 5.5-pp margin standard deviation, and define the **Trader Markup**:

$$\text{Poll Win Odds (R)} = \Phi\!\left(\frac{\text{R Poll \%} - \text{D Poll \%}}{5.5\%}\right)$$

$$\text{Trader Markup (R)} = \text{Raw Market R} - \text{Poll Win Odds (R)}$$

### 2.2 From T−7 GOP Drift to the T−1 Institutional Reversal
I locked the model specification prior to **Tuesday, October 27, 2026** (T−7) and recorded the T−14, October 27 (T−7), and final **Monday, November 2, 2026** (T−1) pre-election snapshots in [`midterm_2026_battlegrounds.csv`](./midterm_2026_battlegrounds.csv) and [`midterm_2026_t7_results.json`](./midterm_2026_t7_results.json). Table 1 summarizes all **15 competitive statewide battlegrounds**—all 9 competitive Senate battlegrounds (8 Republican-held seats plus open Democratic-held Michigan) and all 6 competitive Governor races (5 Republican-held seats plus open Democratic-held Kansas), totaling \$255.5 million in direct race volume by T−1.

#### Table 1: 2026 Battleground Market Trajectory (T−7 to T−1), Poll Win Odds, and Trader Markup
*(Full breakdown including T−14 prices, two-party polling averages, and T−7 markups in [Supplemental Table S7](./supplemental_tables.md#table-s7) and [`midterm_2026_battlegrounds.csv`](./midterm_2026_battlegrounds.csv).)*

| 2026 Battleground Race | Raw (T−7, Oct 27) | Raw (T−1, Nov 2) | T−7 to T−1 Shift | T−1 Poll Win (R) | T−1 GOP Markup |
| :-- | :--: | :--: | :--: | :--: | :--: |
| **NC Senate (Open)** | 96% D / 4% R | **98% D / 2% R** | −2.0 pp R | 2.3% R | **−0.3 pp** |
| **ME Senate (Collins\*)** | 61% D / 39% R | **72.5% D / 27.5% R** | **−11.5 pp R** | 27.4% R | **+0.1 pp** |
| **MI Senate (Open)** | 68% D / 32% R | **78.5% D / 21.5% R** | **−10.5 pp R** | 16.8% R | **+4.7 pp** |
| **OH Senate (Husted\*)** | 67.5% D / 32.5% R | **70.5% D / 29.5% R** | −3.0 pp R | 30.5% R | **−1.0 pp** |
| **AK Senate (Sullivan\*)** | 74% D / 26% R | **72% D / 28% R** | **+2.0 pp R** | 40.0% R | **−12.0 pp** |
| **TX Senate (Open)** | 66% D / 34% R | **75.5% D / 24.5% R** | **−9.5 pp R** | 32.5% R | **−8.0 pp** |
| **IA Senate (Open)** | 42% D / 58% R | **50% D / 50% R** | **−8.0 pp R** | 52.2% R | **−2.2 pp** |
| **KS Senate (Marshall\*)** | 41% D / 59% R | **62% D / 38% R** | **−21.0 pp R** | 25.6% R | **+12.4 pp** |
| **NE Senate (Ricketts\*)** | 29% I / 71% R | **28.5% I / 71.5% R** | +0.5 pp R | 67.5% R | **+4.0 pp** |
| **GA Gov (Open)** | 61% D / 39% R | **69% D / 31% R** | **−8.0 pp R** | 57.2% R | **−26.2 pp** |
| **NV Gov (Lombardo\*)** | 76% D / 24% R | **75.5% D / 24.5% R** | +0.5 pp R | 50.0% R | **−25.5 pp** |
| **TX Gov (Abbott\*)** | 34% D / 66% R | **39% D / 61% R** | **−5.0 pp R** | 67.5% R | **−6.5 pp** |
| **VT Gov (P. Scott\*)** | 23% D / 77% R | **31% D / 69% R** | **−8.0 pp R** | 48.5% R | **+20.5 pp** |
| **FL Gov (Open)** | 30% D / 70% R | **34.5% D / 65.5% R** | **−4.5 pp R** | 76.6% R | **−11.1 pp** |
| **KS Gov (Open)** | 23% D / 77% R | **30% D / 70% R** | **−7.0 pp R** | 62.8% R | **+7.2 pp** |

- **Phase 1 (T−14 → T−7): Early Republican drift and +6.13 pp Senate markup.** Between T−14 and October 27 (T−7), Republican win odds moved higher in 8 of the 14 competitive battlegrounds outside safe North Carolina, rising by **+0.71 pp** volume-weighted across all 15 battlegrounds (+0.95 pp excluding North Carolina). At T−7, traders priced Senate Republicans **+6.13 pp above** poll win odds—led by Iowa (+9.5 pp), Kansas (+16.2 pp), and Nebraska (+18.8 pp)—while pricing Governor Republicans **−9.18 pp below** poll win odds across the 6 gubernatorial battlegrounds.
- **Phase 2 (T−7 → T−1): Institutional reversal and Senate markup compression.** Between October 27 and November 2, uncapped 2026 order books broke sharply toward Democrats in 12 of the 15 battlegrounds, producing a **−7.82 pp volume-weighted Republican shift** (−7.28 pp net from T−14 → T−1). Kalshi's **U.S. Senate Control** contract jumped from 63% D at T−7 to **74% D / 26% R** at T−1 (75% D sweep on the \$96.6 million Balance of Power market), and **U.S. House Control** rose from 90.9% D to **94% D / 6% R** alongside a D+8.5 RealClearPolling Generic Ballot at snapshot (ticking to D+8.8 late November 2).
- **Where markups vanished—and where they remain at T−1.** Following final NYT/Siena, Washington Post, CNN, and YouGov polls showing Democratic gains across surveyed Senate battlegrounds, the mean Senate trader markup compressed from **+6.13 pp at T−7 to −0.26 pp at T−1** (ME +0.1 pp, OH −1.0 pp, IA −2.2 pp, TX −8.0 pp). Substantial Republican markups remain only in **Kansas Senate** (**+12.4 pp R**, where Democrat Adam Hamilton leads 49.8%–46.2% in polls [25.6% R poll win odds] while markets price Sen. Roger Marshall at 38% R), **Kansas Governor** (**+7.2 pp R** in the open Democratic-held race where Republican Ty Masterson leads Cindy Holscher 48.8%–47.0% [62.8% R poll win odds] while markets price Masterson at 70% R), **Michigan Senate** (**+4.7 pp R** after primary runner-up Rep. Haley Stevens endorsed Republican Mike Rogers over Abdul El-Sayed on November 1), **Nebraska Senate** (**+4.0 pp R**, independent Dan Osborn vs. Sen. Pete Ricketts), and **Vermont Governor** (**+20.5 pp R**, after a November 1 UNH survey put Democrat Amanda Janoo ahead of Gov. Phil Scott, whom pre-election polls have consistently understated since 2016). Conversely, **Alaska Senate** (Mary Peltola vs. Sen. Dan Sullivan) was the sole competitive Senate race to move toward Republicans (+2.0 pp R to 72% D / 28% R) following October 28–30 reporting on no-party candidate Daniel J. Sullivan Jr. and narrowing polls (49.2%–47.8%).

---

<a id="sec-3"></a>
## 3. Poll-Conditioned Log-Odds De-Biasing Methodology

### 3.1 Chamber Holdover Baselines and Certified 2006–2025 State Win Shares
Every seat projection in [`run_t7_analysis.py`](./run_t7_analysis.py) starts from exact pre-election chamber arithmetic:
- **U.S. Senate (53 R–47 D entering November 2026; 51 for majority, or 50 R with the Vice President's tie-breaker):** With 35 seats up in 2026 (13 D, 22 R), seats **Not Up** are **34 D / 31 R** (including the 2 Independents caucusing with Democrats). Outside the 9 Senate battlegrounds in Table 3, Democrats hold 12 safe/likely seats (34 + 12 = **46 D** baseline) and Republicans hold 14 safe/likely/lean seats (31 + 14 = **45 R** baseline).
- **Governors (26 R–24 D entering November 2026 after Virginia flipped R→D in November 2025):** With 36 governorships up (18 D, 18 R), seats **Not Up** are **6 D / 8 R**. Outside the 6 tracked Governor battlegrounds (5 Republican-held plus open Democratic-held Kansas), Democrats lead all 17 remaining Democratic-held seats plus 3 open Republican-held seats (AK, IA, OH; 6 + 17 + 3 = **26 D** baseline) and Republicans hold 10 safe seats (8 + 10 = **18 R** baseline).
- **U.S. House (all 435 seats up; 218 for majority):** Evaluated across competitive district contracts by mapping district partisanship onto the 35%–100% redness scale alongside Republican incumbency credits ([`run_t7_analysis.py`](./run_t7_analysis.py)).
- **Certified 2006–2025 Statewide GOP Win Shares:** For each state, GOP 20-Yr Win% measures the exact fraction of certified general and special Senate and Governor elections won by Republicans from 2006 through 2025 (reported alongside official 2025 Cook PVIs in [Supplemental Table S9](./supplemental_tables.md#table-s9)).

### 3.2 Separated State Redness, Incumbency, and Fortress Credit
To preserve legitimate historical and incumbent advantages found in the 2012–2026 baseline study, each race receives a structural **GOP Credit** (in percentage-point equivalents above the 35% Blue-State threshold, where $\text{Incumbent} = 1.00$ for an elected Republican incumbent, $0.45$ for an appointed Republican incumbent [Jon Husted in Ohio], and $0.00$ for an open seat):

$$\text{GOP Credit (pp)} = 0.045 \max(0,\; \text{GOP 20-Yr\%} - 35\%) + 5.50 \times \text{Incumbent} + 0.055 \max(0,\; \text{GOP 20-Yr\%} - 35\%) \times \text{Incumbent}$$

The three additive terms capture **State Redness Alone**, **Incumbency Alone**, and the **Combined Fortress Interaction**, respectively.

### 3.3 Frozen Poll-Conditioned Log-Odds Specification and 4-Tier Classification
To avoid ex-post parameter tuning, I apply the exact specification frozen at T−7 to the live T−1 market and polling inputs, comparing two bounded **log-odds (logit)** adjustments against raw market prices:
1. **Simple Log-Odds Benchmark:** Applies a uniform +0.70 logit shift toward the Democrat (equivalent to roughly +17 pp near a 50/50 market price) to every contract.
2. **Preferred Poll-Conditioned Log-Odds Model:** Subtracts the race's structural GOP Credit from the historical non-presidential baseline (**17.34 pp**, matching the 455-election baseline study's exact modern non-presidential net market bias), converts the net adjustment into logit units, and scales the shift down whenever traders already price the Republican below Poll Win Odds ($\text{Markup} < 0$, with weight $w = 1.0$ if $\text{Markup} \ge 0$ and $w = \max(0.25,\; 1 + \text{Markup}/35)$ if $\text{Markup} < 0$):

$$\Delta_{\text{logit}} = \left(\frac{\max(0,\; 17.34 - \text{GOP Credit})}{24.5}\right) \times w$$

$$\text{Preferred D Win Odds} = \frac{1}{1 + \exp\!\Big(-\big[\ln(\text{Raw D} / \text{Raw R}) + \Delta_{\text{logit}}\big]\Big)}$$

Even when the T−1 trader markup approaches zero (as in Maine, Ohio, or Iowa), a positive net shift remains for non-fortress seats because historical non-presidential market bias (+17.34 pp) reflected **+11.50 pp of systematic midterm poll error** in addition to +5.85 pp of trader markup. All races are classified into four standard market probability tiers, with **45%–55% Toss-Ups left strictly uncalled (No Call)** in chamber seat totals:
- **Toss-Up (45%–55%):** Dead heat / coin flip; left uncalled (No Call).
- **Lean (55%–65%):** Clear favorite within active battleground swing range.
- **Likely (65%–85%):** Substantial favorite requiring a major catalyst to flip.
- **Safe / Solid (>85%):** Non-competitive tail with very low upset probability.

---

<a id="sec-4"></a>
## 4. 2026 Midterm Chamber and Battleground Predictions Through T−1

#### Table 2: 2026 Midterm Chamber Seat Projections at T−1 (With 45%–55% Toss-Ups Uncalled)
*(Full T−14 and T−7 seat trajectories across all three models are reported in [Supplemental Table S8](./supplemental_tables.md#table-s8).)*

| Chamber (Majority) | Not Up | Raw Market (T−1) | Simple Log-Odds (T−1) | Preferred Forecast (T−1, Nov 2) |
| :-- | :--: | :--: | :--: | :--: |
| **U.S. Senate (51)** | 34 D / 31 R | **53 D–46 R** (1 TU: IA) | **54 D–46 R** (0 TU) | **54 D–46 R, 0 Toss-Ups** (IA Lean D 64.2%; KS Likely D 69.4%; NE Likely R 66.2%) |
| **Governors (26)** | 6 D / 8 R | **28 D–22 R** (0 TU) | **29 D–18 R** (3 TU: VT, FL, KS) | **28 D–22 R, 0 Toss-Ups** (TX 56.7% R; VT 58.5% R; FL 55.4% R; KS 55.2% R) |
| **U.S. House (218)** | All 435 Up | **237 D–194 R** (4 TU) | **250 D–172 R** (13 TU) | **243 D–181 R, 11 Toss-Ups** (+6 called D, −13 called R vs. raw) |

#### Table 3: Race-by-Race 2026 Battleground Forecasts at T−7 and T−1
*(Full 8-column table including certified 2006–2025 state win ratios, 2025 Cook PVI, T−14 forecasts, and Simple Log-Odds outputs in [Supplemental Table S9](./supplemental_tables.md#table-s9).)*

| 2026 Battleground Race | GOP Credit | Preferred (T−7) | Raw Market (T−1) | Preferred Forecast & Call (T−1, Nov 2) |
| :-- | :--: | :--: | :--: | :--: |
| **NC Senate (Open)** | +0.88 pp | 97.9% D (Safe D) | 98.0% D / 2.0% R | **99.0% D / 1.0% R — Safe / Solid D** |
| **ME Senate (Collins\*)** | +6.99 pp | 70.5% D (Likely D) | 72.5% D / 27.5% R | **80.1% D / 19.9% R — Likely D** |
| **MI Senate (Open)** | +0.00 pp | 81.2% D (Likely D) | 78.5% D / 21.5% R | **88.1% D / 11.9% R — Safe / Solid D** |
| **OH Senate (Husted\*)** | +4.69 pp | 77.7% D (Likely D) | 70.5% D / 29.5% R | **79.8% D / 20.2% R — Likely D** |
| **AK Senate (Sullivan\*)** | +10.18 pp | 78.5% D (Likely D) | 72.0% D / 28.0% R | **75.7% D / 24.3% R — Likely D** |
| **TX Senate (Open)** | +2.92 pp | 77.8% D (Likely D) | 75.5% D / 24.5% R | **82.9% D / 17.1% R — Likely D** |
| **IA Senate (Open)** | +2.11 pp | 57.4% D (Lean D) | 50.0% D / 50.0% R | **64.2% D / 35.8% R — Lean D** |
| **KS Senate (Marshall\*)** | +9.27 pp | 49.1% D (Toss-Up) | 62.0% D / 38.0% R | **69.4% D / 30.6% R — Likely D** |
| **NE Senate (Ricketts\*)** | +11.23 pp | 34.4% I (Likely R) | 28.5% I / 71.5% R | **33.8% I / 66.2% R — Likely R** |
| **GA Gov (Open)** | +1.80 pp | 70.2% D (Likely D) | 69.0% D / 31.0% R | **72.3% D / 27.7% R — Likely D** |
| **NV Gov (Lombardo\*)** | +6.99 pp | 77.9% D (Likely D) | 75.5% D / 24.5% R | **77.6% D / 22.4% R — Likely D** |
| **TX Gov (Abbott\*)** | +12.00 pp | 39.0% D (Lean R) | 39.0% D / 61.0% R | **43.3% D / 56.7% R — Lean R** |
| **VT Gov (P. Scott\*)** | +6.12 pp | 30.6% D (Likely R) | 31.0% D / 69.0% R | **41.5% D / 58.5% R — Lean R** |
| **FL Gov (Open)** | +2.17 pp | 40.3% D (Lean R) | 34.5% D / 65.5% R | **44.6% D / 55.4% R — Lean R** |
| **KS Gov (Open)** | +1.70 pp | 35.4% D (Lean R) | 30.0% D / 70.0% R | **44.8% D / 55.2% R — Lean R** |

- **U.S. Senate (54 D–46 R with 0 Toss-Ups at T−1, following raw-market convergence to my T−7 seat count).** At T−14 and T−7, raw markets called 52 D–48 R (IA at 58% R, KS at 59% R), whereas my T−14 and T−7 preferred model flagged open-seat Iowa as a Lean R trap (57.4% D at T−7) and projected **53 D–46 R (1 Toss-Up)**. By T−1, raw Kalshi and Polymarket prices surged to **53 D–46 R (1 Toss-Up)**—flipping **Kansas** 21 pp to 62.0% D and moving **Iowa** (Josh Turek vs. Ashley Hinson) to an exact 50.0% D / 50.0% R Toss-Up. Applying the frozen poll-conditioned log-odds model at T−1 moves **open-seat Iowa** (+2.11 pp redness credit, no incumbent) from 50.0% D raw to **64.2% D (Lean D)** and **Kansas** (+12.4 pp remaining GOP markup minus +9.27 pp Marshall fortress credit) from 62.0% D raw to **69.4% D (Likely D)**, yielding **54 D–46 R (0 Toss-Ups)**. Meanwhile, structural fortress credits keep **Nebraska** (+11.23 pp credit → **66.2% R Likely R**) and untabulated **South Carolina** (appointed Republican Sen. Darline Graham vs. Annie Andrews, +7.01 pp credit moving 68% R raw on Kalshi to **58.2% R Lean R**) in the Republican column.
- **Governors (28 D–22 R with 0 Toss-Ups across all three horizons, a net +4 Democratic gain from 26 R–24 D).** The 6-race gubernatorial battleground slate shows why structural credits and poll-conditioning are essential. After late polls tightened in Texas (NYT/Siena and AtlasIntel putting Gina Hinojosa 1 point ahead of Greg Abbott, while the 9-poll RealClearPolling average remained Abbott+2.5), Vermont (UNH putting Amanda Janoo ahead of Phil Scott), Florida (Byron Donalds leading David Jolly 48.3%–44.3%), and open Democratic-held Kansas (Ty Masterson leading Cindy Holscher 48.8%–47.0%), an unadjusted **Simple Log-Odds** shift at T−1 flips **Texas Governor** to Lean D (56.3% D) and pushes **Vermont (47.5% D)**, **Florida (51.5% D)**, and **Kansas (46.3% D)** into three uncalled Toss-Ups (**29 D–18 R, 3 Toss-Ups**). By contrast, my preferred model preserves Lean R calls across all four contests—**Abbott (56.7% R)** via his +12.00 pp fortress credit, **Scott (58.5% R)** via his +6.12 pp incumbency credit, **Donalds in Florida (55.4% R)** via Florida's +2.17 pp redness credit and −11.1 pp negative markup weight, and **Masterson in Kansas (55.2% R)** at the edge of the Lean R boundary—while projecting Democratic flips in **Nevada (77.6% D)** and **Georgia (72.3% D)** alongside non-battleground open-seat flips in Alaska, Iowa, and Ohio.
- **U.S. House (243 D–181 R with 11 Toss-Ups at T−1).** On Kalshi's final November 2 district map (435 seats), raw prices under my strict 45%–55% Toss-Up rule call **237 D–194 R** with **4 Toss-Ups** (PA-01 54% D, WI-01 50% D, SC-01 49% D, TX-23 46% D). District-level log-odds de-biasing promotes those 4 raw Toss-Ups plus open ME-02 (44% D → 61.0% D) and newly redrawn AL-02 (44% D → 61.2% D) into Lean D (**243 D**), while moving 11 vulnerable 56%–68% R Republican seats (CO-05, NC-03, AZ-02, FL-27, MN-01, NC-13, CO-03, MO-02, NV-02, FL-09, NY-21) into uncalled 45%–55% Toss-Ups (**181 R, 11 Toss-Ups**).

---

<a id="sec-5"></a>
## 5. Limitations and How November 3 Can Falsify This Model

1. **Calibration on two modern midterm cycles (2018 and 2022).** Although the 225-race non-presidential baseline spans 37 election dates, 175 of those contests come from 2018 (+15.98 pp bias) and 2022 (+23.97 pp bias). Even after Senate trader markups compressed to −0.26 pp at T−1, my model still applies a positive Democratic log-odds adjustment in non-fortress states because historical non-presidential polls underestimated Democrats by +11.50 pp in win-probability terms. If 2026 pollsters have eliminated—or reversed—that midterm polling error, raw T−1 prices will outperform my adjusted probabilities.
2. **Institutional arbitrage in the final week of 2026.** Pre-2024 non-presidential markets traded primarily on PredictIt (\$850 cap, 10% fee) and early Polymarket. The −7.82 pp Democratic surge and elimination of the aggregate Senate trader markup between T−7 and T−1 demonstrate that deep institutional capital on Kalshi and Polymarket actively arbitraged late polling releases in ways capped retail markets in 2018 and 2022 never did.
3. **Polling-margin variance assumptions.** Conditioning the log-odds shift on the market-vs-poll gap relies on a 5.5-pp statewide polling margin standard deviation that splits undecided voters evenly and uses two-way polling in ranked-choice Alaska.
4. **Explicit November 3 falsification test across both T−7 and T−1.** Locking both the October 27 (T−7) and November 2 (T−1) snapshots prior to Election Day creates two clean out-of-sample tests once certified November 3 results are tabulated:
   - **Test 1 (Did institutional markets self-correct by T−1?):** Comparing raw T−7 vs. raw T−1 Brier scores tests whether late institutional capital improved forecast accuracy over the final week.
   - **Test 2 (Does de-biasing still beat raw T−1 institutional prices?):** If raw November 2 Kalshi/Polymarket prices achieve a lower **Brier score** across the 15 battlegrounds than the Preferred Poll-Conditioned Log-Odds forecasts—for instance, if Republicans win Iowa Senate (50.0% R raw vs. 35.8% R adjusted) and Kansas Senate (38.0% R raw vs. 30.6% R adjusted)—2026 will falsify the persistence of non-presidential market bias on modern institutional exchanges.

---

<a id="sec-6"></a>
## 6. Conclusion

Tracking the 2026 U.S. midterm prediction markets from T−14 through T−7 (October 27) and T−1 (November 2) uncovers a pivotal contrast with earlier midterm cycles. Through T−7, 2026 Senate markets resembled 2018 and 2022, drifting +0.71 pp more Republican and pricing Senate Republicans +6.13 pp above poll-implied win probabilities. Over the final six days before Election Day, however, uncapped institutional order books on Kalshi and Polymarket reversed that trajectory—shifting −7.82 pp toward Democrats across the 15 battlegrounds (\$255.5 million volume), compressing the mean Senate trader markup to −0.26 pp, and bringing raw Senate seat calls (53 D–46 R, 1 Toss-Up) into alignment with my locked T−7 de-biased seat count.

Applying the frozen poll-conditioned log-odds model with separated State Redness, Incumbency, and Fortress credits to final November 2 (T−1) prices and polls—while leaving 45%–55% Toss-Ups uncalled—projects Democrats winning the **U.S. Senate 54 D–46 R with 0 Toss-Ups** (Iowa Lean D at 64.2% D; Kansas Likely D at 69.4% D; Nebraska Likely R at 66.2% R), **Governors 28 D–22 R with 0 Toss-Ups** (preserving Lean R calls for incumbents Greg Abbott [56.7% R] and Phil Scott [58.5% R] and open-seat Republicans Byron Donalds [55.4% R] and Ty Masterson [55.2% R]), and the **U.S. House 243 D–181 R with 11 Toss-Ups**. With both T−7 and T−1 forecasts locked ahead of November 3, certified election outcomes will provide a transparent Brier-score test of raw institutional market pricing versus poll-conditioned de-biasing.

---

<a id="sec-disclosures"></a>
## Disclosures

### Independent Research and Employer Disclaimer
I conducted this research and wrote this paper independently in my personal capacity. None of the analysis, data interpretations, election forecasts, or viewpoints expressed in this paper represent the views, positions, policies, or endorsements of my employer, its parent or affiliated entities, or any of its clients. Nothing in this paper constitutes financial, investment, legal, or wagering advice.

### Declaration of Generative AI and AI-Assisted Technologies in the Writing and Research Process
During the preparation of this work, I used generative AI coding and research assistants to help compile the 2026 market and polling snapshots ([`midterm_2026_battlegrounds.csv`](./midterm_2026_battlegrounds.csv) and [`midterm_2026_t7_results.json`](./midterm_2026_t7_results.json)), run Python log-odds de-biasing scripts ([`run_t7_analysis.py`](./run_t7_analysis.py)), verify chamber holdover baselines and certified 2006–2025 state election histories, and draft and edit the text and tables. All modeling choices (including the separated redness-incumbency-fortress credits, poll-conditioned log-odds specification, and uncalled 45%–55% Toss-Up rule), dataset rules, and forecasts were conceived, directed, and checked by me, and I take full responsibility for the accuracy of the work.

---

<a id="sec-references"></a>
## References

- **Crane, H., & Strumpf, K. S. (2026, October 20).** *Diversity, efficiency, and incentives in political prediction markets*. Working Paper, arXiv:2610.28277. https://arxiv.org/abs/2610.28277
- **Lazarus, S. H. / Council on Foreign Relations [CFR]. (2026, October 27).** *Betting on democracy: The promise and perils of election markets*. Council Special Report, Council on Foreign Relations. https://www.cfr.org/reports/betting-on-democracy
- **Shirani-Mehr, H., Rothschild, D., Goel, S., & Gelman, A. (2018).** Disentangling bias and variance in election polls. *Journal of the American Statistical Association*, 113(522), 607–614. https://doi.org/10.1080/01621459.2018.1448823
- **Silver, N. (2018, May 30).** *The polls are all right*. FiveThirtyEight. https://fivethirtyeight.com/features/the-polls-are-all-right/
- **Wolfers, J., & Zitzewitz, E. (2004).** Prediction markets. *Journal of Economic Perspectives*, 18(2), 107–126.
- **Zitzewitz, E. (2026, October).** *Are prediction markets politically biased?* National Bureau of Economic Research (NBER) Working Paper No. 35846. https://doi.org/10.3386/w35846

### Suggested Citation
> Ollarvez, A. (2026). *Applying Prediction Market De-Biasing to the 2026 U.S. Midterms: Poll-Conditioned Log-Odds Forecasts Through T−1 for the Senate, Governors, and House*. Independent Empirical Forecast Working Paper. Available at: https://github.com/Aollarve/prediction-market-partisan-bias
