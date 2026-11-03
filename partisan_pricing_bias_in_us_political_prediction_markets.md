# Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012–2026)

**Author:** Andres Ollarvez  
**Affiliation:** Independent Empirical Research Working Paper  
**Date:** November 2026  
**Replication Data, Tables & Code:** [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv) · [`supplemental_tables.md`](./supplemental_tables.md) · [`replicate_paper_tables.py`](./replicate_paper_tables.py) · [GitHub Repository](https://github.com/Aollarve/prediction-market-partisan-bias)

---

## Abstract

Prediction markets like Kalshi and Polymarket are widely cited alongside election polls on the premise that profit-seeking traders strip out partisan bias. I test this claim across **455 verified U.S. elections from 2012 to April 2026** ([`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv)). Before 2016 (*N* = 60), betting markets showed no partisan tilt (+1.37 percentage points [pp], *p* = 0.9168). Since 2016, however, traders have priced Republican win probabilities **+3.8 to +6.5 pp** higher than poll-implied win probabilities across every election category. When Donald Trump was on the ballot (2016, 2020, 2024), state polls underestimated Republicans, so this markup paid off—leaving net market error at −9.32 pp in presidential races (*N* = 75) and −5.85 pp in presidential-year down-ballot races (*N* = 95), with lower Brier error than polls in both cohorts. In modern midterms and special elections (*N* = 225 across 37 dates), polls already leaned +11.50 pp too Republican and traders added +5.85 pp of markup on top, producing a **+17.34 pp pro-Republican bias** (*p* < 0.0001).

In **what I call the wrong-call test**, Republican favorites in modern non-presidential races lost **46.2% of the time (66/143)** while Democratic favorites lost **7.3% of the time (6/82)**—a **+34.72 pp excess upset rate** at the exact same contract price (*p* < 0.0001), or **+31.12 pp** (38.3% vs. 5.5%) after excluding 45%–55% Toss-Ups. While traders accurately reflect Republican history in Red States (+5.49 pp bias, *p* = 0.2359), they discount Democratic history in Blue States, marking up Republicans by +8.63 pp over the polls (+24.04 pp total error). Consequently, while prediction markets beat bell-curve polling benchmarks in pre-2016 (Brier 0.1050 vs. 0.1107) and modern presidential-cycle races (0.1062 vs. 0.1098 top-of-ticket; 0.1312 vs. 0.1383 down-ballot), they trail simple poll benchmarks across modern non-presidential elections (0.1720 vs. 0.1412).

---

> [!IMPORTANT]
> **Key Findings at a Glance**
> - **Consistent Post-2015 Trader Markup:** Since 2016, prediction markets have priced Republican win probabilities **+3.81 to +6.49 pp above poll-implied win odds** across every election cohort (*p* < 0.001 in each).
> - **Why Presidential Cycles Masked the Bias:** When Donald Trump was on the ballot (2016, 2020, 2024), polls underestimated Republicans, making that trader markup profitable. In modern midterms and special elections (*N* = 225 across 37 dates), polls leaned +11.50 pp Republican and trader markup (+5.85 pp) compounded the miss to **+17.34 pp** (*p* < 0.0001)—significant both before *Dobbs* (+11.88 pp, *p* = 0.0104) and after *Dobbs* (+22.47 pp, *p* < 0.0001).
> - **The Wrong-Call Test:** Holding the favorite's exact contract price above 50¢ constant across 225 modern non-presidential races, Republican favorites suffered upsets **46.2% of the time (66/143)** vs. **7.3% (6/82)** for Democratic favorites (**+34.72 pp** excess upset rate, *p* < 0.0001), including **73.7% losses (28/38)** among 55%–65% Lean R favorites.
> - **Asymmetric Use of State History & Brier Calibration:** Traders price Red States accurately (+5.49 pp bias, *p* = 0.2359) while marking up Republicans by +8.63 pp over polls in Blue States (+24.04 pp total error), worsening non-presidential Brier accuracy from **0.1412 (polls) to 0.1720 (markets)**.

**Contents:** [1. Introduction](#sec-1) · [2. Dataset & Methodology](#sec-2) · [3. Cycle-by-Cycle Evidence & Wrong-Call Test](#sec-3) · [4. State Redness, Incumbency, Platforms & Tiers](#sec-4) · [5. Brier Calibration & Limitations](#sec-5) · [6. Conclusion](#sec-6) · [Disclosures](#sec-disclosures) · [References & Citation](#sec-references)

---

<a id="sec-1"></a>
## 1. Introduction

### 1.1 Earlier Literature on Market Efficiency
For decades, economists treated political betting markets as the gold standard of election forecasting:
- **Information aggregation and probability pricing (Hayek, 1945; Wolfers & Zitzewitz, 2004; Arrow et al., 2008).** Market prices combine scattered information across thousands of participants (Hayek, 1945), and in a liquid binary market paying \$1.00 for a win, a 60-cent contract price translates to a 60% implied win probability (Wolfers & Zitzewitz, 2004). On that basis, Arrow et al. (2008) urged U.S. regulators in *Science* to legalize prediction markets.
- **Empirical accuracy before 2016 (Rhode & Strumpf, 2004; Berg, Nelson, & Rietz, 2008; Rothschild, 2009).** Rhode and Strumpf (2004) showed that across 15 presidential elections on the Wall Street Curb Exchange (1884–1940), profit-seeking arbitrageurs absorbed Tammany Hall partisan bets: the mid-October betting favorite won 11 times, 3 close contests traded at even odds, and the underdog won only once (1916). Berg, Nelson, and Rietz (2008) found that the Iowa Electronic Markets (IEM) beat 964 national polls 74% of the time across the five presidential elections from 1988 to 2004, and Rothschild (2009) showed that after adjusting for favorite-longshot bias, 2008 Intrade odds beat raw polls with no partisan tilt.

### 1.2 Post-2015 Market Changes and the October 2026 Studies
Every one of those classic studies examined elections **before 2016**, when trading occurred on small academic exchanges capped at \$500 (IEM) or offshore exchanges (Intrade, which closed in March 2013, and Betfair). Since then, political betting shifted first to capped U.S. retail platforms (PredictIt, with an \$850 cap and 10% profit fee) and crypto exchanges (Polymarket, launched in 2020), and then to regulated U.S. event contracts after Kalshi won federal court approval and began listing candidate contracts on **October 4, 2024**.

In **October 2026**, three studies argued that political prediction markets remain unbiased:
- **Zitzewitz (October 2026), NBER Working Paper 35846 (*"Are Prediction Markets Politically Biased?"*).** Analyzing betting returns from 1880 to 2025, Zitzewitz found no significant partisan bias (nor bias by candidate gender, race, or age). Two factors explain why his pooled result differs from modern midterms: in 2016, 2020, and 2024 presidential years, polls underestimated Republicans so a Republican markup was profitable; and his preliminary October 2026 sample **excludes Polymarket**.
- **Crane & Strumpf (October 20, 2026), arXiv:2610.28277 (*"Diversity, Efficiency, and Incentives in Political Prediction Markets"*).** Examining internal 2024 Kalshi records, Crane and Strumpf found that although Kalshi volume came from areas that voted only 28% Republican and single-trade users placed 73% of their volume on Kamala Harris, **60% of overall Kalshi dollar volume backed Republicans**, driven by active multi-trade participants. Kalshi beat poll-based forecasts in the 2024 national presidential race, the 7 battleground states, and 19 Senate races (where Republicans flipped Democratic seats in PA, OH, MT, and WV), whereas on 2016 PredictIt (\$850 cap), positions closely tracked bettors' registered party.
- **Lazarus / Council on Foreign Relations (October 27, 2026) (*"Betting on Democracy"*).** Samuel Henry Lazarus cited a Kalshi calibration study across 6,000 election markets showing that prices track empirical win frequencies overall (for instance, 20-cent underdogs winning roughly 1 in 5 times and 60-cent contracts winning roughly 60% of the time), and highlighted institutional market-making from firms like Susquehanna International Group. However, pooling both parties together can mask a directional gap if 60-cent Democrats win over 80% of the time while 60-cent Republicans win roughly 25% of the time.

This paper tests four questions across 455 resolved U.S. elections from 2012 to April 2026: (1) how market pricing differs between presidential years and non-presidential midterms and specials, both before and after *Dobbs* (June 2022); (2) what a price-controlled wrong-call test shows about favorite upset rates; (3) whether traders are merely projecting historical state and incumbent winning streaks or discounting history in blue states; and (4) where pre-election T−1 market calibration beats or trails polling benchmarks in Brier accuracy.

---

<a id="sec-2"></a>
## 2. Dataset and Methodology (455 Elections, 2012–April 2026)

### 2.1 The 455-Election Replication Dataset
Each row in [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv) represents a certified U.S. general, runoff, recall, or special election (*N* = 455 across *G* = 51 distinct election dates) with a pre-election polling average and a liquid binary winner contract across five cohorts:
1. **Pre-2016 Control Era (2012–2014, 60 races across 9 dates):** 20 presidential contracts in 2012 (IEM, Intrade, Betfair) and 40 Senate, governor, and special elections from 2012 to 2014 (IEM and Betfair only after Intrade closed in March 2013).
2. **Modern Presidential Top-of-Ticket (2016, 2020, 2024, 75 contracts across 3 dates):** The national contract plus 24 battleground and lean state/district contracts per cycle (25 per cycle).
3. **Modern Presidential-Year Down-Ballot (2016, 2020, 2024, 95 races across 5 dates):** Competitive Senate, governor, and U.S. House races held in presidential cycles: 22 in 2016 (including the December Louisiana Senate runoff), 28 in 2020 (including the two January 5, 2021 Georgia Senate runoffs), and 45 in 2024 (18 Senate, 7 governor, and 20 House races).
4. **Modern Midterms (2018 and 2022, 175 races across 3 dates):** 84 competitive Senate (20), governor (22), and House (42) races in 2018, plus 91 Senate (20, including the December 2022 Georgia runoff), governor (26), Attorney General/Secretary of State (6), and House (39) races in 2022.
5. **Modern Special and Off-Year Elections (2017–April 2026, 50 polled races across 34 dates):** Federal Senate and House specials, statewide judicial/ballot specials (Wisconsin Supreme Court 2023 & 2025, Pennsylvania Supreme Court 2023, Ohio Issue 1 2023, California Recall 2021), and off-year statewide races (VA, NJ, KY, MS, LA), split evenly into 25 pre-*Dobbs* (May 2017–June 14, 2022 across 16 dates) and 25 post-*Dobbs* (June 28, 2022–April 2026 across 18 dates) contests. Kalshi is recorded strictly on the 78 contracts resolved after its October 4, 2024 launch.

### 2.2 Contract Normalization and the Strict T−1 Pre-Election Cutoff
Because exchange fees and position limits push raw "Yes" prices for the Republican and Democrat above \$1.00 (often \$1.05–\$1.15 on PredictIt and \$1.01–\$1.02 on Kalshi and Polymarket), I normalize prices so implied win probabilities sum to 100%:

$$\text{Market Win Chance (R)} = \frac{\text{Raw R Price}}{\text{Raw R Price} + \text{Raw D Price}}$$

All market prices in [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv) are evaluated strictly at **T−1** (closing prices the day before Election Day). Stopping at T−1 rather than Election Day morning (T−0) prevents pre-election forecasts from being contaminated by Election Day turnout reports and exit-poll leaks.

### 2.3 Separating Poll Error From Trader Markup
Poll vote share is not win probability: a candidate leading 53% to 47% in the vote has far more than a 53% chance of winning. In empirical audits of late-campaign polls, Shirani-Mehr, Rothschild, Goel, and Gelman (2018) and Silver (2018) found that two-party polling margins have a standard deviation of roughly 5 to 6 percentage points (pp)—where **percentage points (pp)** measure the arithmetic difference between two percentages (for example, a shift from 50% to 56% is +6 pp). Calibrated to those benchmarks, I convert each race's final polling margin in [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv) into a baseline **Poll Win Chance** using a normal cumulative distribution function ($\Phi$) with a uniform 5.5-pp standard deviation on the two-party margin (in a sensitivity check widening House and special elections to a 6.5-pp standard deviation, the modern non-presidential trader markup increases slightly from +5.85 pp to +5.97 pp):

$$\text{Poll Win Chance (R)} = \Phi\!\left(\frac{\text{R Poll \%} - \text{D Poll \%}}{5.5\%}\right)$$

Headline **Total Market Bias** compares the market's T−1 win probability directly against the certified 0-or-1 election outcome and therefore does not depend on any polling assumption. The Poll Win Chance decomposes total market error into two additive components:

$$\text{Total Market Bias} = \text{Poll Win-Odds Bias} + \text{Trader Win-Odds Markup}$$

- **Poll Win-Odds Bias** = $\text{Poll Win Chance} - \text{Actual Win Rate}$
- **Trader Win-Odds Markup** = $\text{Market Win Chance} - \text{Poll Win Chance}$

Across the 225 modern non-presidential races at T−1, Republicans won 36.9% of the time, polls implied a 48.4% Republican win chance, and markets priced a 54.2% Republican win chance (+17.34 pp Total Bias = +11.50 pp Poll Bias + +5.85 pp Trader Markup; unrounded 11.497 + 5.847 = 17.344). Because races held on the same date share correlated polling errors, I report both **date-clustered** and **race-level** *t*-test *p*-values computed via exact Student-*t* integration (with full date counts and sub-columns in [`supplemental_tables.md`](./supplemental_tables.md)).

---

<a id="sec-3"></a>
## 3. Cycle-by-Cycle Evidence and the Wrong-Call Test

### 3.1 Comparing Pre-2016, Presidential Years, Down-Ballot Races, Midterms, and Specials
Alongside measuring average win-probability bias, I run what I call the **wrong-call test**: when the market names a candidate the favorite (>50¢) and that favorite loses, which party did the market overrate?

Favorites are supposed to lose sometimes—a 60-cent favorite should lose about 40% of the time. More importantly, **comparing the share of Republican wrong calls against a naive 50/50 coin flip would commit a base-rate fallacy** whenever Republicans are favored in more than half of the races on the board. In the 225 modern non-presidential races, Republicans were priced as favorites in 63.6% (143/225) of contests; even in a completely unbiased market, roughly 64% of all wrong calls would be Republicans simply because there were more Republican favorites. To avoid base-rate distortion, I compare **each party's own favorite upset rate** (GOP Upsets / GOP Favorites vs. Dem Upsets / Dem Favorites) and run a **price-controlled regression** that holds the favorite's exact price above 50¢ constant.

#### Table 1: Summary of Market Bias, Trader Markup Over Polls, and Favorite Upset Rates at T−1 (455 Races)
*(Full 11-column breakdown with date counts G, average market odds, actual win rates, clustered and race-level p-values, and exact k/n fractions in [Supplemental Table S1](./supplemental_tables.md#table-s1).)*

| Election Cohort | Races | Net Market Bias | Trader Markup | GOP Fav Upset % | Dem Fav Upset % |
| :-- | :--: | :--: | :--: | :--: | :--: |
| **All Verified Elections (2012–26)** | 455 | +6.00 pp\*\*\* | **+4.28 pp\*\*\*** | 29.1% | 14.9% |
| **1. Pre-2016 Control (2012–14)** | 60 | +1.37 pp (NS) | −0.93 pp (NS) | 11.5% | 11.8% |
| **2. All Modern (2016–2026)** | 395 | **+6.70 pp\*\*\*** | **+5.07 pp\*\*\*** | 31.1% | 15.6% |
| **3. Pres Top-of-Ticket (16/20/24)** | 75 | −9.32 pp\* | **+3.81 pp\*\*\*** | 2.4% | 20.6% |
| **4. Pres-Year Down-Ballot (16/20/24)** | 95 | −5.85 pp (NS) | **+4.24 pp\*\*\*** | 11.8% | 27.3% |
| **5. Modern Midterms Pool (18 & 22)** | 175 | **+20.13 pp\*\*\*** | **+6.05 pp\*\*\*** | **52.2%** | **6.7%** |
| — **5a. 2018 Midterms Alone** | 84 | **+15.98 pp\*\*\*** | **+6.49 pp\*\*\*** | **49.0%** | 9.1% |
| — **5b. 2022 Midterms Alone** | 91 | **+23.97 pp\*\*\*** | **+5.64 pp\*\*\*** | **54.7%** | **3.7%** |
| **6. Modern Specials / Off-Yr (17–26)** | 50 | +7.58 pp (NS) | **+5.14 pp\*\*\*** | **21.4%** | **9.1%** |
| **7. All Modern Non-Pres (Rows 5+6)** | **225** | **+17.34 pp\*\*\*** | **+5.85 pp\*\*\*** | **46.2%** | **7.3%** |
| **8. All Modern Down-Ballot (Rows 4+7)** | **320** | **+10.46 pp\*\*\*** | **+5.37 pp\*\*\*** | **37.1%** | **14.3%** |

- **Why presidential cycles reconcile these findings with Zitzewitz (2026) and Crane & Strumpf (2026).** Across Rows 3 through 7, traders priced Republican win probabilities **+3.81 pp to +6.49 pp higher than poll-implied win probabilities** in every modern category (*p* < 0.001 in each). In 2016, 2020, and 2024, state polls underestimated Donald Trump and down-ballot Republicans (who held PA, WI, and NC Senate seats in 2016; held ME and NC Senate in 2020; and flipped PA, OH, and MT Senate in 2024). Because Republicans beat their polls when Trump was on the ballot, that trader markup made markets more accurate than polls—leaving net market error at −5.85 pp in presidential-year down-ballot races (Row 4) and +6.70 pp across all 395 modern races (Row 2; clustered *p* = 0.2574, race-level *p* = 0.0005).
- **Outside presidential years, the same Republican markup backfires (+17.34 pp, *p* < 0.0001).** In midterms and special elections (Row 7, 225 races across 37 dates), polls did not underestimate Republicans. Poll-implied win probabilities already leaned +11.50 pp too Republican, and traders added another +5.85 pp of markup on top, producing a **+17.34 pp** pro-Republican miss (clustered *p* < 0.0001, race-level *p* < 0.0001; +10.46 pp across all 320 modern down-ballot races in Row 8, clustered *p* = 0.0518, race-level *p* < 0.0001).
- **Both 2018 (+15.98 pp) and 2022 (+23.97 pp) show large pro-Republican errors.** In **2018** (Row 5a, 84 races), even though Republicans won Florida, Indiana, and Missouri Senate, traders overpriced Republicans across suburban House districts and governor races (WI, KS, NV), resulting in 25 GOP favorite upsets versus 3 Democratic upsets. In **2022** (Row 5b, 91 races), traders priced in a "Red Wave" that never materialized across battleground Senate (PA, AZ, NV, GA, NH), governor (AZ, WI, KS), and House contracts (clustered *p* = 0.0059; 35 GOP favorite losses vs. 1 Democratic loss).
- **What the wrong-call test proves: a +34.72 pp double standard between parties.** Across the 225 modern non-presidential races (Row 7), Democratic favorites lost only **7.3% of the time (6/82)**, whereas Republican favorites **lost 46.2% of the time (66/143)**—more than **six times** as often (91.7% of all wrong calls [66/72]). Holding the favorite's exact price above 50¢ constant in an ordinary-least-squares regression, being a Republican favorite increases the probability of an upset by **+34.72 pp** (SE = 5.16 pp, *t* = 6.73, *p* < 0.0001). Traders require a clear lead before making a Democrat the favorite, while routinely pricing Republicans as favorites in coin-flip races.

### 3.2 Pre-*Dobbs* vs. Post-*Dobbs* Non-Presidential Elections
A reasonable skeptic could argue that the Supreme Court's June 2022 *Dobbs* decision (overturning *Roe v. Wade*) and the 2025–2026 backlash against Donald Trump's second term produced unexpected Democratic wins that merely make the statistics look like a pro-Republican bias. To test whether the bias is just an artifact of those post-June 2022 shocks, Table 2 splits the 225 modern non-presidential races into **Pre-*Dobbs*** (May 2017 to June 14, 2022) and **Post-*Dobbs*** (June 28, 2022 to April 2026).

#### Table 2: Pre-2016 vs. Pre-*Dobbs* vs. Post-*Dobbs* Non-Presidential Elections
*(Full breakdown with date counts G, clustered p-values, and raw fractions in [Supplemental Table S2](./supplemental_tables.md#table-s2).)*

| Historical Period / Cohort | Races | Trader Markup | Net Market Bias | GOP Fav Upset % | Dem Fav Upset % |
| :-- | :--: | :--: | :--: | :--: | :--: |
| **1. Pre-2016 Control (2012–14)** | 60 | −0.93 pp (NS) | +1.37 pp (NS) | 11.5% | 11.8% |
| **2. Pre-Dobbs Specials (17–Jun 22)** | 25 | **+5.29 pp\*\*\*** | −1.88 pp (NS) | 25.0% | 22.2% |
| **3. Pre-Dobbs Non-Pres (17–Jun 22)** | 109 | **+6.22 pp\*\*\*** | **+11.88 pp\*\*** | **43.3%** | **11.9%** |
| **4. Post-Dobbs Specials (Jul 22–26)** | 25 | **+4.98 pp\*** | **+17.04 pp\*\*** | 16.7% | 0.0% |
| **5. Post-Dobbs Non-Pres (Jul 22–26)** | 116 | **+5.49 pp\*\*\*** | **+22.47 pp\*\*\*** | **48.7%** | **2.5%** |

- **The pro-Republican bias was already statistically significant before *Dobbs* and before Trump's second term (+11.88 pp across 109 pre-*Dobbs* non-presidential races across 17 dates; clustered *p* = 0.0104, race-level *p* = 0.0022).** Between 2017 and June 2022, traders priced Republicans +5.29 pp to +6.22 pp above poll-implied win odds (*p* < 0.001), and Republican favorites lost nearly four times as often as Democratic favorites (43.3% [29/67] vs. 11.9% [5/42], or 85.3% of all wrong calls). Even in the 25 pre-*Dobbs* special and off-year elections (including Glenn Youngkin's and Winsome Earle-Sears's November 2021 Virginia wins), traders still marked up Republican win odds by **+5.29 pp** over the polls (*p* = 0.0006). The non-presidential bias therefore cannot be dismissed as a fluke of *Dobbs* or post-2024 backlash.
- ***Dobbs* and the 2025–2026 second-term backlash compounded that existing markup (+22.47 pp post-*Dobbs*, *p* < 0.0001).** After June 2022 (Rows 4 and 5), traders kept applying a +5.49 pp Republican markup over the polls even as Democrats consistently beat their polls across both the 2022 midterms and the 2023–2026 special and off-year elections. Across 25 post-*Dobbs* specials and off-year races on 18 dates (Row 4), net pro-Republican bias rose to **+17.04 pp** (clustered *p* = 0.0028, race-level *p* = 0.0091), and across all 116 post-*Dobbs* non-presidential races (Row 5), Democratic favorites lost only 1 of 40 races (2.5%) while Republican favorites lost 37 of 76 (48.7%).

---

<a id="sec-4"></a>
## 4. State Redness, Incumbency, Platforms, and Probability Tiers

Before calling this a right-wing bias, I test a simpler structural explanation: maybe traders are just predicting that **what has always happened will keep happening**—assuming that Republican incumbents who keep winning re-election, or Republicans running in red states that have voted Republican for decades, will simply keep winning. In a state like Kansas or Texas, pricing a Republican above a single noisy poll is standard Bayesian reasoning rather than partisan wishful thinking.

### 4.1 Measuring State Redness and Seat Incumbency (225 Non-Presidential Races)
For every contest in [`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv), I track two structural fundamentals:
1. **State Redness (20-Year Statewide GOP Win Share & Cook PVI):** How often Republicans won statewide Senate and governor elections over the preceding 20 years, paired with the state or district's Cook Partisan Voting Index (PVI): **Red States** (≥65% GOP win history, average PVI = R+8.4, 74 races), **Purple States** (35% to 65% GOP history, average PVI = R+0.8, 72 races), and **Blue States** (≤35% GOP history, average PVI = D+2.1, 79 races).
2. **Seat Incumbency (Who Holds the Seat):** Whether the seat is defended by an **elected Republican incumbent on the ballot** (64 races), is an **open or appointed Republican-held seat** (60 races), or is a **Democratic-held seat** (101 races).

#### Table 3: State Redness and Seat Incumbency Effects on Actual Wins and Market Bias (225 Races)
*(Full sub-columns and the complete 3×3 State Redness × Incumbency interaction matrix are reported in [Supplemental Tables S3](./supplemental_tables.md#table-s3) and [S4](./supplemental_tables.md#table-s4).)*

| Structural Group | Races | Actual GOP Win % | Poll Bias | Trader Markup | Total Market Bias |
| :-- | :--: | :--: | :--: | :--: | :--: |
| **All Non-Presidential** | **225** | **36.9%** | **+11.50 pp\*\*\*** | **+5.85 pp\*\*\*** | **+17.34 pp\*\*\*** |
| **1. Red States (≥65% GOP)** | 74 | **64.9%** | +3.59 pp (NS) | +1.89 pp\* | **+5.49 pp (NS)** |
| **2. Purple States (35–65%)** | 72 | **27.8%** | **+15.33 pp\*\*\*** | **+6.85 pp\*\*\*** | **+22.18 pp\*\*\*** |
| **3. Blue States (≤35% GOP)** | 79 | **19.0%** | **+15.41 pp\*\*\*** | **+8.63 pp\*\*\*** | **+24.04 pp\*\*\*** |
| **4a. Elected GOP Incumbent** | 64 | **50.0%** | **+11.32 pp\*** | **+4.07 pp\*\*\*** | **+15.39 pp\*\*** |
| **4b. Open / Appt. GOP Seat** | 60 | **48.3%** | **+11.44 pp\*** | **+3.79 pp\*\*\*** | **+15.23 pp\*\*** |
| **5. Dem-Held Seat** | 101 | **21.8%** | **+11.64 pp\*\*** | **+8.19 pp\*\*\*** | **+19.83 pp\*\*\*** |

### 4.2 What Crossing State Redness and Incumbency Reveals
Crossing the three state-redness tiers with the three seat-incumbency categories ([Supplemental Table S4](./supplemental_tables.md#table-s4)) isolates where historical projection works and where it breaks down:
- **In Red States (≥65% GOP win history), traders' belief that "what has always happened will keep happening" holds up.** Across 74 non-presidential races in Red States (Row 1), Republicans won **64.9% (48/74)** of the time (65.5% with an elected GOP incumbent and 75.9% in open/appointed GOP seats), and net market bias was an insignificant **+5.49 pp** (*p* = 0.2359, with trader markup at +1.89 pp).
- **Both state redness (*R*² = 0.170) and seat incumbency (*R*² = 0.080) strongly predict actual winners.** Moving from a Democratic-held seat (21.8% GOP win rate) to a Republican-held seat (49.2% across all 124 GOP-held seats) raises Republican wins by **+27.4 pp**, and moving from a Blue State (19.0%) or Purple State (27.8%) to a Red State (64.9%) raises Republican wins by **+37 to +46 pp**. Combining an elected Republican incumbent with a Red or Purple state creates a genuine structural "fortress."
- **In Purple States, open Republican seats trap traders (+33.50 pp bias).** When an elected Republican incumbent runs in a Purple State, they win 53.3% of the time (+10.47 pp bias). When a Purple-State Republican seat is **open** (16 races, such as Pennsylvania Senate or Arizona Governor in 2022), the Republican win rate drops to **25.0% (4/16)**, yet traders still mark up the Republican by **+6.79 pp** over the polls—producing a **+33.50 pp** error ([Supplemental Table S4](./supplemental_tables.md#table-s4)).
- **Traders discount history when it favors Democrats in Blue States.** If traders were simply betting that "what has always happened will keep happening," then in **Blue States** (≤35% statewide GOP history, Row 3), where Democrats won **81.0% (64/79)** of non-presidential contests, traders would price Democratic favorites aggressively. Instead, across 79 Blue-State races, traders marked up Republican win probabilities by **+8.63 pp above the polls**—and by **+10.04 pp** when Republicans challenged Democratic-held seats (44 races)—resulting in a **+24.04 pp** pro-Republican miss (*p* < 0.0001).

### 4.3 Candidate and State Demographics
Controlling for state redness and seat incumbency across the 225 non-presidential races, the indicator `diverse_or_female_dem` (equal to 1 when the Democratic nominee is female or a racial/ethnic minority or the jurisdiction is ≥35% non-white; *N* = 131 vs. *N* = 94) has no statistically significant effect on net market bias (+7.63 pp, SE = 5.04 pp, *t* = 1.52, *p* = 0.1312). This matches Zitzewitz (2026), who likewise found no systematic market pricing bias by candidate gender or race; state redness, incumbency, and the election cycle drive the mispricing.

### 4.4 Platform Rules, Voter Turnout, and the 4-Tier Market Classification
Tables 4 and 5 summarize the dataset across trading platforms, voter turnout (VEP %), and the four standard market probability tiers: **Toss-Up** (45%–55% / 45¢–55¢), **Lean** (55%–65% / 55¢–65¢), **Likely** (65%–85% / 65¢–85¢), and **Safe / Solid** (>85% / >85¢).

#### Table 4: Platform Breakdown and Voter Turnout (VEP %) Regimes
*(Full breakdown with average market odds, actual win rates, and exact k/n fractions in [Supplemental Table S5](./supplemental_tables.md#table-s5).)*

| Platform or Turnout Subgroup | Races | Trader Markup | Net Market Bias | GOP vs. Dem Fav Upset % |
| :-- | :--: | :--: | :--: | :--: |
| **1. PredictIt Non-Pres (2017–24, \$850 Cap)** | 214 | **+5.81 pp\*\*\*** | **+17.47 pp\*\*\*** | 47.5% vs. 8.0% |
| **2. Polymarket Non-Pres (2021–26, Crypto)** | 114 | **+5.88 pp\*\*\*** | **+23.21 pp\*\*\*** | 50.7% vs. 2.4% |
| **3. Kalshi Non-Pres Specials (2024–26)** | 8 | +7.26 pp (NS) | +14.38 pp (NS) | 0.0% vs. 0.0% |
| **4. Kalshi All Down-Ballot (2024–26)** | 53 | **+4.83 pp\*\*\*** | +3.70 pp (NS) | 11.1% vs. 7.7% |
| **5. Kalshi All Verified (Oct 2024–Apr 2026)** | 78 | **+4.16 pp\*\*\*** | −1.44 pp (NS) | 6.8% vs. 8.8% |
| **6. Specials & Off-Year (14–59% VEP)** | 50 | **+5.14 pp\*\*\*** | +7.58 pp (NS) | 21.4% vs. 9.1% |
| **7. Midterms (42–68% VEP)** | 175 | **+6.05 pp\*\*\*** | **+20.13 pp\*\*\*** | 52.2% vs. 6.7% |
| **8. Pres-Year Down-Ballot (32–80% VEP)** | 95 | **+4.24 pp\*\*\*** | −5.85 pp (NS) | 11.8% vs. 27.3% |
| **9. Pres Top-of-Ticket (51–80% VEP)** | 75 | **+3.81 pp\*\*\*** | −9.32 pp\* | 2.4% vs. 20.6% |

#### Table 5: Breakdown Across the 4 Market Probability Tiers in 225 Non-Presidential Races
*(Full tier definitions, average contract prices, win rates, Brier scores, and exact k/n fractions in [Supplemental Table S6](./supplemental_tables.md#table-s6).)*

| Market Probability Tier | Races (R / D Fav) | GOP Fav Upset % | Dem Fav Upset % | Net Tier Bias (Markup) |
| :-- | :--: | :--: | :--: | :--: |
| **1. Toss-Up (45%–55%)** | 37 (28 R / 9 D) | **78.6%** (22/28) | **22.2%** (2/9) | **+29.92 pp\*\*\*** (+10.29 pp) |
| **2. Lean (55%–65%)** | 61 (38 R / 23 D) | **73.7%** (28/38) | **17.4%** (4/23) | **+29.05 pp\*\*\*** (+7.65 pp) |
| **3. Likely (65%–85%)** | 77 (49 R / 28 D) | **32.7%** (16/49) | **0.0%** (0/28) | **+13.86 pp\*\*** (+5.61 pp) |
| **4. Safe / Solid (>85%)** | 50 (28 R / 22 D) | 0.0% (0/28) | 0.0% (0/22) | **−0.88 pp (NS)** (+0.71 pp) |
| **Excl. Toss-Ups (≥55%)** | **188 (115 R / 73 D)** | **38.3% (44/115)** | **5.5% (4/73)** | **+14.87 pp\*\*\*** (+4.97 pp) |

- **Kalshi's verified record (*n* = 78 since October 4, 2024).** Because Kalshi began listing candidate contracts in October 2024, its verified pre-midterm record consists of 25 November 2024 presidential contracts, 45 November 2024 down-ballot contracts, and 8 special and off-year elections in 2025–2026. Across all 78 Kalshi contracts (Row 5 of Table 4), traders priced Republicans +4.16 pp above poll win probabilities and matched or beat the polls in November 2024 (−1.44 pp net error overall; +3.70 pp across the 53 down-ballot contracts in Row 4, where Republican favorites lost CA-13, CA-27, and CA-45 while Democratic favorites lost Pennsylvania Senate and NE-02). In the 8 post-2024 special and off-year elections (Row 3), Republicans were priced +7.26 pp above poll-implied odds (+14.38 pp net bias, *p* = 0.1239).
- **Turnout regimes (VEP %).** Splitting the 225 non-presidential races at 45% VEP turnout shows significant pro-Republican bias in both low-turnout <45% VEP contests (*N* = 47, +10.00 pp bias, *p* = 0.0472) and standard-turnout ≥45% VEP midterm/off-year contests (*N* = 178, +19.28 pp bias, *p* < 0.0001). The decisive divide is not low versus medium turnout, but whether Donald Trump is at the top of the ballot (51%–80% VEP in November presidential general elections, or 32%–80% including the December 2016 Louisiana runoff).
- **Why the bias peaks in 45%–55% Toss-Ups and 55%–65% Lean contracts.** In 45%–55% Toss-Ups (Row 1 of Table 5, 37 races), Republicans priced at 50%–55% won 6 of 28 (21.4%), while Democrats won 7 of 9 (77.8%). In **Row 2 (Lean 55%–65%, 61 races)**, when markets priced a Republican as a Lean R favorite (59.1% R average price across 38 races, such as Mehmet Oz at 57¢ in PA 2022 or Tim Michels at 58¢ in WI 2022), **those Lean R favorites lost 73.7% of the time (28/38)**, while Lean D favorites (59.7% D) won **82.6% (19/23)**—a **+29.05 pp** tier bias (*p* < 0.0001).
- **Excluding 45%–55% Toss-Ups still leaves a +31.12 pp price-controlled upset gap (*p* < 0.0001).** Among the 188 clear favorites priced ≥55¢ (bottom row of Table 5), **Republican clear favorites lost 38.3% of the time (44/115) while Democratic clear favorites lost 5.5% of the time (4/73)** (SE = 5.37 pp, *t* = 5.80, *p* < 0.0001). Above 85¢ (Safe / Solid, Row 4), bias disappears (−0.88 pp), with both parties winning 100% of the time (28/28 R, 22/22 D).

---

<a id="sec-5"></a>
## 5. Brier Probability Calibration vs. Polling Benchmarks and Study Limitations

### 5.1 When Do Prediction Markets Beat Polls in Brier Accuracy?
To evaluate overall probability accuracy without directional cancellation (where a +20 pp error in one race cancels a −20 pp error in another), Table 6 compares the mean **Brier score** $(\text{Prob} - \text{Outcome})^2$ of T−1 normalized market probabilities against the bell-curve polling benchmark (`poll_win_prob_r_55sd`) across all major election regimes (where 0.0000 is perfect foresight and 0.2500 is a 50/50 coin flip).

#### Table 6: T−1 Market vs. Polling Brier Calibration Across Election Regimes (455 Races)

| Election Regime | Races (Dates) | Market Brier | Poll Brier | Brier Diff (Mkt − Poll) | More Accurate Benchmark |
| :-- | :--: | :--: | :--: | :--: | :--: |
| **1. Pre-2016 Control (2012–14)** | 60 (9) | **0.1050** | 0.1107 | −0.0057 | **Prediction Markets** |
| **2. Pres Top-of-Ticket (16/20/24)** | 75 (3) | **0.1062** | 0.1098 | −0.0036 | **Prediction Markets** |
| **3. Pres-Year Down-Ballot (16/20/24)** | 95 (5) | **0.1312** | 0.1383 | −0.0071 | **Prediction Markets** |
| **4. Modern Midterms (2018 & 2022)** | 175 (3) | 0.1818 | **0.1476** | **+0.0342** | **Polling Benchmark** |
| **5. Modern Specials / Off-Yr (17–26)** | 50 (34) | 0.1377 | **0.1189** | **+0.0188** | **Polling Benchmark** |
| **6. All Modern Non-Pres (Rows 4+5)** | **225 (37)** | 0.1720 | **0.1412** | **+0.0308** | **Polling Benchmark** |
| **All Verified Elections (2012–2026)** | **455 (51)** | 0.1438 | **0.1314** | +0.0124 | **Polling Benchmark** |

- **Markets beat polls before 2016 and whenever Trump was on the ballot.** In the pre-2016 control cohort (0.1050 vs. 0.1107), modern presidential top-of-ticket contracts (0.1062 vs. 0.1098), and presidential-year down-ballot contests (0.1312 vs. 0.1383), T−1 market prices achieved lower Brier error than poll-implied probabilities.
- **In modern non-presidential races, the trader markup degrades Brier calibration across every competitive tier.** Across the 225 modern non-presidential races, adding +5.85 pp of pro-Republican trader markup onto polls that already leaned +11.50 pp Republican worsened the Brier score from **0.1412 (polls) to 0.1720 (markets)** (+0.0308 penalty). In both 45%–55% Toss-Ups (0.2608 market Brier vs. 0.2087 poll Brier) and 55%–65% Lean races (0.2642 vs. 0.2199; [Supplemental Table S6](./supplemental_tables.md#table-s6)), raw non-presidential market prices performed worse than a blind 50/50 coin flip (0.2500).

### 5.2 Study Limitations
1. **Two modern midterm cycles (2018 and 2022).** While the 50 special and off-year elections span 34 separate election dates, the 175 modern midterm races come from two national midterm cycles, and the pro-Republican error was larger in 2022 (+23.97 pp) than in 2018 (+15.98 pp).
2. **Capped retail order books vs. institutional liquidity.** Most pre-2024 non-presidential contracts traded on PredictIt (\$850 cap, 10% profit fee) or early Polymarket, where retail limits prevented institutional arbitrageurs from absorbing partisan order flow (Crane & Strumpf, 2026). Whether uncapped regulated exchanges (Kalshi) and institutional market makers (Lazarus / Council on Foreign Relations, 2026) eliminate or compress this non-presidential markup in future cycles remains an open empirical question.
3. **Selection into competitive races and polling-benchmark assumptions.** Prediction markets only attract deep liquidity in contests where an upset is plausible, and decomposing total market bias into poll bias versus trader markup relies on a bell-curve polling margin standard deviation (5.5 pp uniform baseline; +5.97 pp markup under a 6.5-pp House/specials sensitivity check) that splits undecided voters evenly. Headline Total Market Bias (+17.34 pp) and the wrong-call test (+34.72 pp), however, compare T−1 market prices directly against certified election outcomes and require no polling assumptions.

---

<a id="sec-6"></a>
## 6. Conclusion

Across 455 verified U.S. election markets from 2012 to April 2026 ([`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv)), political betting markets since 2016 have priced Republican win probabilities +3.81 to +6.49 pp higher than poll-implied win probabilities in every election category. When Donald Trump was on the ballot in 2016, 2020, and 2024, state polls underestimated Republicans, so that trader markup beat the polls both at the top of the ticket (−9.32 pp net error; 0.1062 vs. 0.1098 Brier) and down-ballot (−5.85 pp; 0.1312 vs. 0.1383 Brier)—reconciling this dataset with Zitzewitz (2026) and Crane & Strumpf (2026). Outside of presidential elections (225 midterm, special, and off-year races across 37 dates), poll-implied win probabilities already leaned +11.50 pp too Republican and traders added another +5.85 pp on top, creating a **+17.34 pp** pro-Republican miss (clustered *p* < 0.0001) and a +0.0308 Brier penalty relative to polls (0.1720 vs. 0.1412) that was already significant before *Dobbs* (+11.88 pp, clustered *p* = 0.0104) and widened further afterward (+22.47 pp, clustered *p* < 0.0001).

What I call the **wrong-call test** captures this asymmetry directly: holding the favorite's exact price above 50¢ constant, Republican favorites suffered upsets at a **+34.72 pp higher rate** than Democratic favorites (46.2% vs. 7.3%, *p* < 0.0001), and 55%–65% Lean R favorites lost 73.7% of the time (28/38). Rather than uniformly projecting historical winning streaks, traders accurately price Red States (+5.49 pp bias, *p* = 0.2359) while discounting Democratic history in Blue States (+8.63 pp trader markup, +24.04 pp total bias).

---

<a id="sec-disclosures"></a>
## Disclosures

### Independent Research and Employer Disclaimer
I conducted this research and wrote this paper independently in my personal capacity. None of the analysis, data interpretations, or viewpoints expressed in this paper represent the views, positions, policies, or endorsements of my employer, its parent or affiliated entities, or any of its clients. Nothing in this paper constitutes financial, investment, legal, or wagering advice.

### Declaration of Generative AI and AI-Assisted Technologies in the Writing and Research Process
During the preparation of this work, I used generative AI coding and research assistants to help compile and verify the 455-election replication dataset ([`verified_election_markets_2012_2026.csv`](./verified_election_markets_2012_2026.csv)), run Python statistical replication scripts ([`replicate_paper_tables.py`](./replicate_paper_tables.py)), and draft and edit the text and tables. All research questions (including the cycle-by-cycle comparisons, the price-controlled wrong-call test, the pre-*Dobbs* falsification test, and the state-redness and incumbency controls), dataset rules, and conclusions were conceived, directed, and checked by me, and I take full responsibility for the accuracy of the work.

---

<a id="sec-references"></a>
## References

- **Arrow, K. J., Forsythe, R., Gorham, M., Hahn, R., Hanson, R., Ledyard, J. O., ... & Zitzewitz, E. (2008).** The promise of prediction markets. *Science*, 320(5878), 877–878.
- **Berg, J. E., Nelson, F. D., & Rietz, T. A. (2008).** Prediction market accuracy in the long run. *International Journal of Forecasting*, 24(2), 285–300.
- **Crane, H., & Strumpf, K. S. (2026, October 20).** *Diversity, efficiency, and incentives in political prediction markets*. Working Paper, arXiv:2610.28277. https://arxiv.org/abs/2610.28277
- **Hayek, F. A. (1945).** The use of knowledge in society. *The American Economic Review*, 35(4), 519–530.
- **Lazarus, S. H. / Council on Foreign Relations [CFR]. (2026, October 27).** *Betting on democracy: The promise and perils of election markets*. Council Special Report, Council on Foreign Relations. https://www.cfr.org/reports/betting-on-democracy
- **Rhode, P. W., & Strumpf, K. S. (2004).** Historical presidential betting markets. *Journal of Economic Perspectives*, 18(2), 127–142.
- **Rothschild, D. (2009).** Forecasting elections: Comparing prediction markets, polls, and their biases. *Public Opinion Quarterly*, 73(5), 895–916.
- **Shirani-Mehr, H., Rothschild, D., Goel, S., & Gelman, A. (2018).** Disentangling bias and variance in election polls. *Journal of the American Statistical Association*, 113(522), 607–614. https://doi.org/10.1080/01621459.2018.1448823
- **Silver, N. (2018, May 30).** *The polls are all right*. FiveThirtyEight. https://fivethirtyeight.com/features/the-polls-are-all-right/
- **Wolfers, J., & Zitzewitz, E. (2004).** Prediction markets. *Journal of Economic Perspectives*, 18(2), 107–126.
- **Zitzewitz, E. (2026, October).** *Are prediction markets politically biased?* National Bureau of Economic Research (NBER) Working Paper No. 35846. https://doi.org/10.3386/w35846

### Suggested Citation
> Ollarvez, A. (2026). *Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012–2026)*. Independent Empirical Research Working Paper. Available at: https://github.com/Aollarve/prediction-market-partisan-bias
