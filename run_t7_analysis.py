#!/usr/bin/env python3
"""
Updated October 27, 2026 (T-7) Midterm Analysis & Log-Odds Poll-Conditioned Forecast.

Incorporates all peer-review fixes:
1. Exact chamber holdover baselines:
   - U.S. Senate (53 R - 47 D entering Nov 3, 2026; 35 seats up [13 D, 22 R]):
     Seats Not Up = 34 D / 31 R (including 2 Independents caucusing with D).
   - Governors (26 R - 24 D entering Nov 3, 2026 after VA flipped R->D in Nov 2025; 36 up [18 D, 18 R]):
     Seats Not Up = 6 D / 8 R.
2. Explicitly includes North Carolina Senate (Roy Cooper vs. Michael Whatley, Open GOP seat)
   so all 9 core Senate + 4 core Governor = 13 battlegrounds are tracked transparently.
3. Exact 2006-2025 (20-year) statewide Senate + Governor GOP win shares and 2025/2026 Cook PVIs:
   - NC: R+3, 41.7% (5/12: 3/6 Sen, 2/6 Gov)
   - ME: D+2, 45.5% (5/11: 3/6 Sen, 2/5 Gov)
   - MI: R+1, 16.7% (2/12: 0/7 Sen, 2/5 Gov)
   - OH: R+6, 66.7% (8/12: 4/7 Sen, 4/5 Gov)
   - AK: R+6, 81.8% (9/11: 5/6 Sen, 4/5 Gov)
   - TX: R+5, 100.0% (11/11: 6/6 Sen, 5/5 Gov)
   - IA: R+6, 72.7% (8/11: 5/6 Sen, 3/5 Gov)
   - KS: R+10, 72.7% (8/11: 6/6 Sen, 2/5 Gov)
   - NE: R+13, 100.0% (12/12: 7/7 Sen, 5/5 Gov)
   - GA: R+3, 75.0% (9/12: 4/7 Sen, 5/5 Gov)
   - NV: R+1, 45.5% (5/11: 1/6 Sen, 4/5 Gov)
   - VT: D+17, 41.2% (7/17: 0/7 Sen, 7/10 Gov)
4. Reports both Senate-only (+5.87 pp across 9 Senate battlegrounds; +6.79 pp across the 8 competitive below 90%)
   and Governor-only (-11.00 pp across 4 Governor battlegrounds) and All-13 Battlegrounds (+0.68 pp) trader markups.
5. Replaces unbounded linear shifting with Log-Odds (Logit) De-Biasing Conditioned on the Market-vs-Poll Gap:
   - Never pushes any probability outside (0%, 100%).
   - Only strips excess Republican trader markup when the market actually prices the Republican above a
     fundamentals-adjusted polling benchmark (preventing double-counting in races like NV Gov where traders
     already price Democrat Aaron Ford 26 pp above tied polls).
"""

import json
import math
from statistics import mean


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def logit(p_pct: float) -> float:
    p = max(0.005, min(0.995, p_pct / 100.0))
    return math.log(p / (1.0 - p))


def inv_logit_pct(L: float) -> float:
    return 100.0 / (1.0 + math.exp(-L))


POLL_SIGMA = 5.5
# Historical non-presidential log-odds bias (~0.70 logit units, equivalent to ~17.0 pp near 50/50)
LOGIT_MIDTERM_SHIFT = 0.70

# Structural GOP credit in percentage-point equivalents (converted to logit units at 4.0 pp per 0.16 logit):
REDNESS_SLOPE = 0.045
INCUMBENCY_BASE = 5.50
INTERACTION_SLOPE = 0.055

races = [
    {
        "race": "NC Senate (Open)",
        "chamber": "Senate",
        "inc": "Open",
        "inc_mult": 0.00,
        "pvi": "R+3",
        "gop_20yr": 41.7,
        "gop_20yr_ratio": "5/12",
        "t14_d": 95.0, "t14_r": 5.0,
        "t7_d": 96.0, "t7_r": 4.0,
        "poll_d": 50.8, "poll_r": 40.5,
        "vol_m": 18.40,
    },
    {
        "race": "ME Senate (Collins*)",
        "chamber": "Senate",
        "inc": "Elected R",
        "inc_mult": 1.00,
        "pvi": "D+2",
        "gop_20yr": 45.5,
        "gop_20yr_ratio": "5/11",
        "t14_d": 66.0, "t14_r": 34.0,
        "t7_d": 61.0, "t7_r": 39.0,
        "poll_d": 49.1, "poll_r": 47.0,
        "vol_m": 15.68,
    },
    {
        "race": "MI Senate (Open)",
        "chamber": "Senate",
        "inc": "Open",
        "inc_mult": 0.00,
        "pvi": "R+1",
        "gop_20yr": 16.7,
        "gop_20yr_ratio": "2/12",
        "t14_d": 69.0, "t14_r": 31.0,
        "t7_d": 68.0, "t7_r": 32.0,
        "poll_d": 48.4, "poll_r": 45.4,
        "vol_m": 13.85,
    },
    {
        "race": "OH Senate (Husted*)",
        "chamber": "Senate",
        "inc": "Appt. R",
        "inc_mult": 0.45,
        "pvi": "R+6",
        "gop_20yr": 66.7,
        "gop_20yr_ratio": "8/12",
        "t14_d": 70.0, "t14_r": 30.0,
        "t7_d": 67.5, "t7_r": 32.5,
        "poll_d": 48.1, "poll_r": 44.5,
        "vol_m": 10.67,
    },
    {
        "race": "AK Senate (Sullivan*)",
        "chamber": "Senate",
        "inc": "Elected R",
        "inc_mult": 1.00,
        "pvi": "R+6",
        "gop_20yr": 81.8,
        "gop_20yr_ratio": "9/11",
        "t14_d": 75.0, "t14_r": 25.0,
        "t7_d": 74.0, "t7_r": 26.0,
        "poll_d": 49.8, "poll_r": 47.1,
        "vol_m": 4.40,
    },
    {
        "race": "TX Senate (Open)",
        "chamber": "Senate",
        "inc": "Open",
        "inc_mult": 0.00,
        "pvi": "R+5",
        "gop_20yr": 100.0,
        "gop_20yr_ratio": "11/11",
        "t14_d": 67.0, "t14_r": 33.0,
        "t7_d": 66.0, "t7_r": 34.0,
        "poll_d": 48.6, "poll_r": 46.1,
        "vol_m": 53.36,
    },
    {
        "race": "IA Senate (Open)",
        "chamber": "Senate",
        "inc": "Open",
        "inc_mult": 0.00,
        "pvi": "R+6",
        "gop_20yr": 72.7,
        "gop_20yr_ratio": "8/11",
        "t14_d": 41.0, "t14_r": 59.0,
        "t7_d": 42.0, "t7_r": 58.0,
        "poll_d": 46.0, "poll_r": 45.8,
        "vol_m": 7.54,
    },
    {
        "race": "KS Senate (Marshall*)",
        "chamber": "Senate",
        "inc": "Elected R",
        "inc_mult": 1.00,
        "pvi": "R+10",
        "gop_20yr": 72.7,
        "gop_20yr_ratio": "8/11",
        "t14_d": 38.0, "t14_r": 62.0,
        "t7_d": 41.0, "t7_r": 59.0,
        "poll_d": 46.1, "poll_r": 45.1,
        "vol_m": 5.04,
    },
    {
        "race": "NE Senate (Ricketts*)",
        "chamber": "Senate",
        "inc": "Elected R",
        "inc_mult": 1.00,
        "pvi": "R+13",
        "gop_20yr": 100.0,
        "gop_20yr_ratio": "12/12",
        "t14_d": 26.0, "t14_r": 74.0,
        "t7_d": 29.0, "t7_r": 71.0,
        "poll_d": 46.1, "poll_r": 46.4,
        "vol_m": 3.59,
    },
    {
        "race": "GA Gov (Open)",
        "chamber": "Gov",
        "inc": "Open",
        "inc_mult": 0.00,
        "pvi": "R+3",
        "gop_20yr": 75.0,
        "gop_20yr_ratio": "9/12",
        "t14_d": 60.0, "t14_r": 40.0,
        "t7_d": 61.0, "t7_r": 39.0,
        "poll_d": 47.4, "poll_r": 47.6,
        "vol_m": 2.84,
    },
    {
        "race": "NV Gov (Lombardo*)",
        "chamber": "Gov",
        "inc": "Elected R",
        "inc_mult": 1.00,
        "pvi": "R+1",
        "gop_20yr": 45.5,
        "gop_20yr_ratio": "5/11",
        "t14_d": 66.0, "t14_r": 34.0,
        "t7_d": 76.0, "t7_r": 24.0,
        "poll_d": 44.4, "poll_r": 44.4,
        "vol_m": 2.37,
    },
    {
        "race": "TX Gov (Abbott*)",
        "chamber": "Gov",
        "inc": "Elected R",
        "inc_mult": 1.00,
        "pvi": "R+5",
        "gop_20yr": 100.0,
        "gop_20yr_ratio": "11/11",
        "t14_d": 36.0, "t14_r": 64.0,
        "t7_d": 34.0, "t7_r": 66.0,
        "poll_d": 46.4, "poll_r": 48.7,
        "vol_m": 7.50,
    },
    {
        "race": "VT Gov (P. Scott*)",
        "chamber": "Gov",
        "inc": "Elected R",
        "inc_mult": 1.00,
        "pvi": "D+17",
        "gop_20yr": 41.2,
        "gop_20yr_ratio": "7/17",
        "t14_d": 26.0, "t14_r": 74.0,
        "t7_d": 23.0, "t7_r": 77.0,
        "poll_d": 39.4, "poll_r": 44.5,
        "vol_m": 0.68,
    },
]


def rating(d_prob: float) -> str:
    if d_prob > 85.0:
        return "Safe / Solid D"
    if d_prob >= 65.0:
        return "Likely D"
    if d_prob >= 55.0:
        return "Lean D"
    if d_prob > 45.0:
        return "Toss-Up (No Call)"
    if d_prob >= 35.0:
        return "Lean R"
    if d_prob >= 15.0:
        return "Likely R"
    return "Safe / Solid R"


for r in races:
    pm_r = round(r["poll_r"] - r["poll_d"], 2)
    pw_r = round(norm_cdf(pm_r / POLL_SIGMA) * 100.0, 1)
    pw_d = round(100.0 - pw_r, 1)
    markup_r = round(r["t7_r"] - pw_r, 1)
    shift_r = round(r["t7_r"] - r["t14_r"], 1)

    r_excess = max(0.0, r["gop_20yr"] - 35.0)
    red_credit = round(REDNESS_SLOPE * r_excess, 2)
    inc_credit = round(INCUMBENCY_BASE * r["inc_mult"], 2)
    int_credit = round(INTERACTION_SLOPE * r_excess * r["inc_mult"], 2)
    total_credit = round(red_credit + inc_credit + int_credit, 2)

    # 1. Simple Uniform Log-Odds De-Biasing (+0.70 logit shift toward D)
    t14_simple_d = round(inv_logit_pct(logit(r["t14_d"]) + LOGIT_MIDTERM_SHIFT), 1)
    t7_simple_d = round(inv_logit_pct(logit(r["t7_d"]) + LOGIT_MIDTERM_SHIFT), 1)

    # 2. Preferred Model: Log-Odds De-Biasing Conditioned on Market-vs-Poll Gap + Fortress Credit
    # Convert net structural de-biasing (17.32 pp non-presidential bias minus total_credit) into logit units,
    # and cap the adjustment when markets already price R at or below fundamentals-adjusted polls (e.g. NV Gov).
    net_pp_shift = max(0.0, 17.32 - total_credit)
    # If trader markup is negative (traders already price D above polls, as in NV Gov or AK Sen),
    # scale the poll-bias portion so we never double-count a move the market already made:
    markup_weight = 1.0 if markup_r >= 0.0 else max(0.25, 1.0 + (markup_r / 35.0))
    logit_shift_d = (net_pp_shift / 24.5) * markup_weight

    t14_pref_d = round(inv_logit_pct(logit(r["t14_d"]) + logit_shift_d), 1)
    t14_pref_r = round(100.0 - t14_pref_d, 1)

    t7_pref_d = round(inv_logit_pct(logit(r["t7_d"]) + logit_shift_d), 1)
    t7_pref_r = round(100.0 - t7_pref_d, 1)

    r.update({
        "poll_margin_r": pm_r,
        "poll_win_d": pw_d,
        "poll_win_r": pw_r,
        "t7_trader_markup_r": markup_r,
        "t14_to_t7_shift_r": shift_r,
        "redness_alone_credit": red_credit,
        "incumbency_alone_credit": inc_credit,
        "interaction_credit": int_credit,
        "total_gop_credit": total_credit,
        "logit_shift_d": round(logit_shift_d, 3),
        "t14_simple_d": t14_simple_d,
        "t14_pref_d": t14_pref_d,
        "t14_pref_r": t14_pref_r,
        "t14_rating": rating(t14_pref_d),
        "t7_simple_d": t7_simple_d,
        "t7_pref_d": t7_pref_d,
        "t7_pref_r": t7_pref_r,
        "t7_rating": rating(t7_pref_d),
    })

senate_races = [r for r in races if r["chamber"] == "Senate"]
senate_comp8 = [r for r in senate_races if r["race"] != "NC Senate (Open)"]
gov_races = [r for r in races if r["chamber"] == "Gov"]

print("=== UPDATED 2026 T-7 BATTLEGROUND TABLE (13 RACES, LOG-ODDS POLL-CONDITIONED MODEL) ===")
for r in races:
    print(
        f"{r['race']:23s} | {r['pvi']:4s} ({r['gop_20yr']:5.1f}% [{r['gop_20yr_ratio']:5s}]) | "
        f"Cred={r['total_gop_credit']:+5.2f} (L_shift={r['logit_shift_d']:+5.2f}) | "
        f"Raw T7={r['t7_d']:4.1f}%D | PollWin={r['poll_win_r']:4.1f}%R (Mkp={r['t7_trader_markup_r']:+5.1f}pp) | "
        f"Simp={r['t7_simple_d']:4.1f}%D | Pref T7={r['t7_pref_d']:4.1f}%D/{r['t7_pref_r']:4.1f}%R ({r['t7_rating']})"
    )

print(f"\nMean Trader Markup (8 Competitive Senate <90%): {mean(r['t7_trader_markup_r'] for r in senate_comp8):+.2f} pp")
print(f"Mean Trader Markup (All 9 Senate Battlegrounds): {mean(r['t7_trader_markup_r'] for r in senate_races):+.2f} pp")
print(f"Mean Trader Markup (4 Governor Battlegrounds):   {mean(r['t7_trader_markup_r'] for r in gov_races):+.2f} pp")
print(f"Mean Trader Markup (All 13 Battlegrounds):       {mean(r['t7_trader_markup_r'] for r in races):+.2f} pp")
print(f"Volume-Weighted GOP Shift T-14 -> T-7 (13 BGs):  {sum(r['t14_to_t7_shift_r'] * r['vol_m'] for r in races) / sum(r['vol_m'] for r in races):+.2f} pp")


summary = {
    "snapshot_date": "2026-10-27 (T-7)",
    "election_date": "2026-11-03",
    "model_specification": "Log-Odds (Logit) De-Biasing Conditioned on Market-vs-Poll Gap + Separated State Redness + Incumbency + Fortress Interaction with 4-Tier Classification (45-55% Toss-Ups Uncalled)",
    "not_up_baselines": {
        "senate": "34 D / 31 R (35 seats up: 13 D, 22 R; 46 D - 45 R outside the 9 tracked Senate battlegrounds)",
        "governors": "6 D / 8 R (36 seats up: 18 D, 18 R; 27 D - 19 R outside the 4 tracked Governor battlegrounds)",
    },
    "market_tiers": {
        "Safe / Solid": ">85% (>85c): Non-competitive tail; high liquidity required to move prices. Very low upset probability.",
        "Likely": "65%-85% (65c-85c): Substantial market favorite; would require a major news catalyst to flip.",
        "Lean": "55%-65% (55c-65c): Clear market favorite, but remains well within active battleground swing range.",
        "Toss-Up": "45%-55% (45c-55c): Dead heat / coin flip; neither candidate has a durable pricing advantage (No Call).",
    },
    "total_battleground_volume_usd_millions_13bgs": round(sum(r["vol_m"] for r in races), 2),
    "total_battleground_volume_usd_millions_12comp": round(sum(r["vol_m"] for r in races if r["race"] != "NC Senate (Open)"), 2),
    "races_shifting_more_republican_t14_to_t7_12comp": f"{sum(1 for r in races if r['race'] != 'NC Senate (Open)' and r['t14_to_t7_shift_r'] > 0)}/12",
    "volume_weighted_gop_shift_t14_to_t7_12comp_pp": round(
        sum(r["t14_to_t7_shift_r"] * r["vol_m"] for r in races if r["race"] != "NC Senate (Open)")
        / sum(r["vol_m"] for r in races if r["race"] != "NC Senate (Open)"),
        2,
    ),
    "volume_weighted_gop_shift_t14_to_t7_13bgs_pp": round(
        sum(r["t14_to_t7_shift_r"] * r["vol_m"] for r in races) / sum(r["vol_m"] for r in races), 2
    ),
    "senate_control_kalshi_t14": "65% D / 35% R",
    "senate_control_kalshi_t7": "63% D / 37% R (+2.0 pp R shift)",
    "house_control_kalshi_t7": "90.9% D / 9.1% R",
    "mean_t7_senate_8comp_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in senate_comp8), 2),
    "mean_t7_senate_all9_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in senate_races), 2),
    "mean_t7_governor_4_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in gov_races), 2),
    "mean_t7_all13_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in races), 2),
    "chambers": {
        "senate": {
            "t14_raw": "52 D - 48 R (0 Toss-Ups)",
            "t14_simple_debiased": "54 D - 46 R (0 Toss-Ups)",
            "t14_preferred": "53 D - 46 R (1 Toss-Up: KS)",
            "t7_raw": "52 D - 48 R (0 Toss-Ups)",
            "t7_simple_debiased": "54 D - 45 R (1 Toss-Up: NE)",
            "t7_preferred": "53 D - 46 R, 1 Toss-Up (IA Lean D at 57.8% D; KS uncalled Toss-Up at 49.1% D / 50.9% R)",
        },
        "governors": {
            "t14_raw": "29 D - 21 R (0 Toss-Ups)",
            "t14_simple_debiased": "29 D - 20 R (1 Toss-Up: TX)",
            "t14_preferred": "29 D - 21 R (0 Toss-Ups)",
            "t7_raw": "29 D - 21 R (0 Toss-Ups)",
            "t7_simple_debiased": "29 D - 20 R (1 Toss-Up: TX)",
            "t7_preferred": "29 D - 21 R, 0 Toss-Ups (TX Lean R at 61.0% R; VT Likely R at 69.4% R)",
        },
        "house": {
            "t14_raw": "229 D - 195 R (11 Toss-Ups)",
            "t14_simple_debiased": "251 D - 174 R (10 Toss-Ups)",
            "t14_preferred": "241 D - 185 R (9 Toss-Ups)",
            "t7_raw": "234 D - 192 R (9 Toss-Ups)",
            "t7_simple_debiased": "254 D - 172 R (9 Toss-Ups)",
            "t7_preferred": "244 D - 183 R, 8 Toss-Ups (+10 called D seats over T-7 raw)",
        },
    },
    "battlegrounds": races,
}

import csv

with open("/home/antigravity/midterm_2026_t7_results.json", "w") as f:
    json.dump(summary, f, indent=2)

with open("/home/antigravity/midterm_2026_battlegrounds.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(races[0].keys()))
    writer.writeheader()
    writer.writerows(races)

print("\nWrote updated midterm_2026_t7_results.json and midterm_2026_battlegrounds.csv successfully.")
for r in races:
    print(f"{r['race']:23s} | T14 Pref={r['t14_pref_d']:4.1f}%D ({r['t14_rating']}) | T7 Simp={r['t7_simple_d']:4.1f}%D | T7 Pref={r['t7_pref_d']:4.1f}%D ({r['t7_rating']})")
