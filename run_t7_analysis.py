#!/usr/bin/env python3
"""
2026 Midterm Pre-Election Analysis & Poll-Conditioned Log-Odds Forecasts (T-14, Oct 27 T-7, and Nov 2 T-1).

Key methodological features:
1. Exact chamber holdover baselines:
   - U.S. Senate (53 R - 47 D entering Nov 3, 2026; 35 seats up [13 D, 22 R]):
     Seats Not Up = 34 D / 31 R (including 2 Independents caucusing with D).
     Outside the 9 tracked Senate battlegrounds, baseline = 46 D / 45 R.
   - Governors (26 R - 24 D entering Nov 3, 2026 after VA flipped R->D in Nov 2025; 36 up [18 D, 18 R]):
     Seats Not Up = 6 D / 8 R.
     Outside the 4 tracked Governor battlegrounds, baseline = 27 D / 19 R.
   - U.S. House (all 435 seats up; 218 for majority):
     Evaluated across competitive Kalshi/Polymarket district contracts using district Cook PVI and incumbency credits.
2. Tracks all 13 statewide battlegrounds (9 Senate + 4 Governor) across T-14, T-7 (Oct 27), and T-1 (Nov 2).
3. Certified 2006-2025 (20-year) statewide Senate + Governor GOP win shares and 2025/2026 Cook PVIs:
   - NC: R+3, 41.7% (5/12)  | ME: D+2, 45.5% (5/11)  | MI: R+1, 16.7% (2/12)
   - OH: R+6, 66.7% (8/12)  | AK: R+6, 81.8% (9/11)  | TX: R+5, 100.0% (11/11)
   - IA: R+6, 72.7% (8/11)  | KS: R+10, 72.7% (8/11) | NE: R+13, 100.0% (12/12)
   - GA: R+3, 75.0% (9/12)  | NV: R+1, 45.5% (5/11)  | VT: D+17, 41.2% (7/17)
4. Bounded Log-Odds (Logit) De-Biasing Conditioned on the Market-vs-Poll Gap + Separated Fortress Credits,
   with 45%-55% Toss-Ups left strictly uncalled (No Call).
   Note: All T-14 and T-7 parameters and outputs remain locked at their pre-T-1 values; T-1 applies the exact
   same frozen specification to live November 2, 2026 market prices and final polling averages.
"""

import csv
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
LOGIT_MIDTERM_SHIFT = 0.70

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
        "t1_d": 98.0, "t1_r": 2.0,
        "t1_poll_d": 51.8, "t1_poll_r": 40.8,
        "t1_vol_m": 21.50,
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
        "t1_d": 72.5, "t1_r": 27.5,
        "t1_poll_d": 49.9, "t1_poll_r": 46.6,
        "t1_vol_m": 21.20,
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
        "t1_d": 78.5, "t1_r": 21.5,
        "t1_poll_d": 50.1, "t1_poll_r": 44.8,
        "t1_vol_m": 25.40,
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
        "t1_d": 70.5, "t1_r": 29.5,
        "t1_poll_d": 48.9, "t1_poll_r": 46.1,
        "t1_vol_m": 14.60,
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
        "t1_d": 72.0, "t1_r": 28.0,
        "t1_poll_d": 49.2, "t1_poll_r": 47.8,
        "t1_vol_m": 8.40,
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
        "t1_d": 75.5, "t1_r": 24.5,
        "t1_poll_d": 49.0, "t1_poll_r": 46.5,
        "t1_vol_m": 88.50,
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
        "t1_d": 50.0, "t1_r": 50.0,
        "t1_poll_d": 46.5, "t1_poll_r": 46.8,
        "t1_vol_m": 13.80,
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
        "t1_d": 62.0, "t1_r": 38.0,
        "t1_poll_d": 49.8, "t1_poll_r": 46.2,
        "t1_vol_m": 12.60,
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
        "t1_d": 28.5, "t1_r": 71.5,
        "t1_poll_d": 45.8, "t1_poll_r": 48.3,
        "t1_vol_m": 7.80,
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
        "t1_d": 69.0, "t1_r": 31.0,
        "t1_poll_d": 47.3, "t1_poll_r": 48.3,
        "t1_vol_m": 4.94,
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
        "t1_d": 75.5, "t1_r": 24.5,
        "t1_poll_d": 43.7, "t1_poll_r": 43.7,
        "t1_vol_m": 5.10,
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
        "t1_d": 39.0, "t1_r": 61.0,
        "t1_poll_d": 47.3, "t1_poll_r": 49.8,
        "t1_vol_m": 15.32,
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
        "t1_d": 31.0, "t1_r": 69.0,
        "t1_poll_d": 45.0, "t1_poll_r": 44.8,
        "t1_vol_m": 1.36,
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
    # Locked T-7 polling & markup metrics
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
    t1_simple_d = round(inv_logit_pct(logit(r["t1_d"]) + LOGIT_MIDTERM_SHIFT), 1)

    # 2. Locked T-14 and T-7 Preferred Poll-Conditioned Log-Odds Forecasts
    net_pp_shift = max(0.0, 17.32 - total_credit)
    markup_weight = 1.0 if markup_r >= 0.0 else max(0.25, 1.0 + (markup_r / 35.0))
    logit_shift_d = (net_pp_shift / 24.5) * markup_weight

    t14_pref_d = round(inv_logit_pct(logit(r["t14_d"]) + logit_shift_d), 1)
    t14_pref_r = round(100.0 - t14_pref_d, 1)

    t7_pref_d = round(inv_logit_pct(logit(r["t7_d"]) + logit_shift_d), 1)
    t7_pref_r = round(100.0 - t7_pref_d, 1)

    # 3. Live November 2, 2026 (T-1) Poll-Conditioned Log-Odds Forecasts (frozen formula, live T-1 inputs)
    t1_pm_r = round(r["t1_poll_r"] - r["t1_poll_d"], 2)
    t1_pw_r = round(norm_cdf(t1_pm_r / POLL_SIGMA) * 100.0, 1)
    t1_pw_d = round(100.0 - t1_pw_r, 1)
    t1_markup_r = round(r["t1_r"] - t1_pw_r, 1)
    t7_to_t1_shift_r = round(r["t1_r"] - r["t7_r"], 1)
    t14_to_t1_shift_r = round(r["t1_r"] - r["t14_r"], 1)

    t1_markup_weight = 1.0 if t1_markup_r >= 0.0 else max(0.25, 1.0 + (t1_markup_r / 35.0))
    t1_logit_shift_d = (net_pp_shift / 24.5) * t1_markup_weight

    t1_pref_d = round(inv_logit_pct(logit(r["t1_d"]) + t1_logit_shift_d), 1)
    t1_pref_r = round(100.0 - t1_pref_d, 1)

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
        "t1_poll_margin_r": t1_pm_r,
        "t1_poll_win_d": t1_pw_d,
        "t1_poll_win_r": t1_pw_r,
        "t1_trader_markup_r": t1_markup_r,
        "t7_to_t1_shift_r": t7_to_t1_shift_r,
        "t14_to_t1_shift_r": t14_to_t1_shift_r,
        "t1_logit_shift_d": round(t1_logit_shift_d, 3),
        "t1_simple_d": t1_simple_d,
        "t1_pref_d": t1_pref_d,
        "t1_pref_r": t1_pref_r,
        "t1_rating": rating(t1_pref_d),
    })

# Programmatic U.S. House T-1 District Aggregation (All 435 Seats on Kalshi, Nov 2, 2026)
# Kalshi Safe D (>=90% D): 211 | Likely D (75%-89% D): 19 | Lean D (60%-73% D): 5 -> 235 seats >=60% D
# Kalshi Safe R (>=91% R): 142 | Likely R >=81% R: 22 -> 164 seats >=81% R
# Remaining 36 competitive House seats (14 Kalshi Toss-Ups + 16 Kalshi Lean R + 6 Likely R at 78%-80% R):
house_t1_comp36 = [
    ("KY-06", 58.0, 0.0, 75.0),
    ("MT-01", 58.0, 0.0, 75.0),
    ("PA-01", 54.0, 1.0, 45.0),
    ("WI-01", 50.0, 1.0, 50.0),
    ("SC-01", 49.0, 0.0, 80.0),
    ("TX-23", 46.0, 0.0, 75.0),
    ("ME-02", 44.0, 0.0, 45.0),  # LePage 57% R / Dunlap 44% D (norm 56.4% R / 43.6% D)
    ("AL-02", 44.0, 0.0, 40.0),
    ("CO-05", 44.0, 1.0, 75.0),
    ("NC-03", 44.0, 1.0, 70.0),
    ("AZ-02", 42.0, 1.0, 65.0),
    ("FL-27", 41.0, 1.0, 65.0),
    ("MN-01", 41.0, 1.0, 65.0),
    ("NC-13", 41.0, 1.0, 70.0),
    ("CO-03", 38.0, 1.0, 60.0),
    ("MO-02", 37.0, 1.0, 70.0),
    ("CO-04", 36.0, 1.0, 75.0),
    ("NV-02", 36.0, 0.0, 75.0),
    ("OH-15", 36.0, 1.0, 70.0),
    ("FL-07", 35.0, 1.0, 65.0),
    ("FL-09", 35.0, 0.0, 45.0),
    ("NC-09", 35.0, 1.0, 70.0),
    ("FL-13", 34.0, 1.0, 65.0),
    ("VA-05", 33.0, 1.0, 65.0),
    ("NY-21", 32.0, 0.0, 55.0),
    ("NJ-02", 30.0, 1.0, 50.0),
    ("FL-16", 29.0, 1.0, 75.0),
    ("OH-10", 29.0, 1.0, 65.0),
    ("NC-07", 25.0, 1.0, 70.0),
    ("TX-09", 25.0, 0.0, 70.0),
    ("NE-01", 22.0, 1.0, 80.0),
    ("NC-14", 21.0, 1.0, 70.0),
    ("AR-02", 20.0, 1.0, 85.0),
    ("FL-04", 20.0, 1.0, 75.0),
    ("IN-05", 20.0, 1.0, 80.0),
    ("NY-01", 20.0, 1.0, 55.0),
]

h_raw_d, h_raw_r, h_raw_tu = 235, 164, 0
h_sim_d, h_sim_r, h_sim_tu = 235, 164, 0
h_prf_d, h_prf_r, h_prf_tu = 235, 164, 0
for dist, rd, inc_m, gop_h in house_t1_comp36:
    sd = round(inv_logit_pct(logit(rd) + LOGIT_MIDTERM_SHIFT), 1)
    r_ex = max(0.0, gop_h - 35.0)
    cred = REDNESS_SLOPE * r_ex + INCUMBENCY_BASE * inc_m + INTERACTION_SLOPE * r_ex * inc_m
    pd = round(inv_logit_pct(logit(rd) + max(0.0, 17.32 - cred) / 24.5), 1)
    if rd >= 55.0:
        h_raw_d += 1
    elif rd <= 45.0:
        h_raw_r += 1
    else:
        h_raw_tu += 1
    if sd >= 55.0:
        h_sim_d += 1
    elif sd <= 45.0:
        h_sim_r += 1
    else:
        h_sim_tu += 1
    if pd >= 55.0:
        h_prf_d += 1
    elif pd <= 45.0:
        h_prf_r += 1
    else:
        h_prf_tu += 1

senate_races = [r for r in races if r["chamber"] == "Senate"]
senate_comp8 = [r for r in senate_races if r["race"] != "NC Senate (Open)"]
gov_races = [r for r in races if r["chamber"] == "Gov"]

print("=== 2026 BATTLEGROUND FORECASTS THROUGH T-1 (NOV 2, 2026) ===")
for r in races:
    print(
        f"{r['race']:23s} | T7 Raw={r['t7_d']:4.1f}%D -> T1 Raw={r['t1_d']:4.1f}%D ({r['t7_to_t1_shift_r']:+5.1f}pp R) | "
        f"T1 PollWin={r['t1_poll_win_r']:4.1f}%R (Mkp={r['t1_trader_markup_r']:+5.1f}pp) | "
        f"T7 Pref={r['t7_pref_d']:4.1f}%D | T1 Simp={r['t1_simple_d']:4.1f}%D | T1 Pref={r['t1_pref_d']:4.1f}%D/{r['t1_pref_r']:4.1f}%R ({r['t1_rating']})"
    )

print(f"\nMean T-7 vs T-1 Trader Markup (All 9 Senate):     {mean(r['t7_trader_markup_r'] for r in senate_races):+.2f} pp -> {mean(r['t1_trader_markup_r'] for r in senate_races):+.2f} pp")
print(f"Mean T-7 vs T-1 Trader Markup (8 Comp Senate):    {mean(r['t7_trader_markup_r'] for r in senate_comp8):+.2f} pp -> {mean(r['t1_trader_markup_r'] for r in senate_comp8):+.2f} pp")
print(f"Mean T-7 vs T-1 Trader Markup (4 Governor BGs):   {mean(r['t7_trader_markup_r'] for r in gov_races):+.2f} pp -> {mean(r['t1_trader_markup_r'] for r in gov_races):+.2f} pp")
print(f"Mean T-7 vs T-1 Trader Markup (All 13 BGs):       {mean(r['t7_trader_markup_r'] for r in races):+.2f} pp -> {mean(r['t1_trader_markup_r'] for r in races):+.2f} pp")
print(f"Vol-Weighted GOP Shift T-14 -> T-7 (13 BGs):      {sum(r['t14_to_t7_shift_r'] * r['vol_m'] for r in races) / sum(r['vol_m'] for r in races):+.2f} pp")
print(f"Vol-Weighted GOP Shift T-7  -> T-1 (13 BGs):      {sum(r['t7_to_t1_shift_r'] * r['t1_vol_m'] for r in races) / sum(r['t1_vol_m'] for r in races):+.2f} pp")
print(f"Vol-Weighted GOP Shift T-14 -> T-1 (13 BGs):      {sum(r['t14_to_t1_shift_r'] * r['t1_vol_m'] for r in races) / sum(r['t1_vol_m'] for r in races):+.2f} pp")
print(f"House T-1 (435 seats): Raw={h_raw_d}D-{h_raw_r}R ({h_raw_tu} TU) | Simple={h_sim_d}D-{h_sim_r}R ({h_sim_tu} TU) | Preferred={h_prf_d}D-{h_prf_r}R ({h_prf_tu} TU)")

summary = {
    "snapshot_date": "2026-11-02 (T-1, with locked T-14 and 2026-10-27 T-7 snapshots)",
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
    "total_battleground_volume_usd_millions_13bgs_t1": round(sum(r["t1_vol_m"] for r in races), 2),
    "total_battleground_volume_usd_millions_12comp": round(sum(r["vol_m"] for r in races if r["race"] != "NC Senate (Open)"), 2),
    "races_shifting_more_republican_t14_to_t7_12comp": f"{sum(1 for r in races if r['race'] != 'NC Senate (Open)' and r['t14_to_t7_shift_r'] > 0)}/12",
    "races_shifting_more_democratic_t7_to_t1_13bgs": f"{sum(1 for r in races if r['t7_to_t1_shift_r'] < 0)}/13",
    "volume_weighted_gop_shift_t14_to_t7_12comp_pp": round(
        sum(r["t14_to_t7_shift_r"] * r["vol_m"] for r in races if r["race"] != "NC Senate (Open)")
        / sum(r["vol_m"] for r in races if r["race"] != "NC Senate (Open)"),
        2,
    ),
    "volume_weighted_gop_shift_t14_to_t7_13bgs_pp": round(
        sum(r["t14_to_t7_shift_r"] * r["vol_m"] for r in races) / sum(r["vol_m"] for r in races), 2
    ),
    "volume_weighted_gop_shift_t7_to_t1_13bgs_pp": round(
        sum(r["t7_to_t1_shift_r"] * r["t1_vol_m"] for r in races) / sum(r["t1_vol_m"] for r in races), 2
    ),
    "volume_weighted_gop_shift_t14_to_t1_13bgs_pp": round(
        sum(r["t14_to_t1_shift_r"] * r["t1_vol_m"] for r in races) / sum(r["t1_vol_m"] for r in races), 2
    ),
    "senate_control_kalshi_t14": "65% D / 35% R",
    "senate_control_kalshi_t7": "63% D / 37% R (+2.0 pp R shift from T-14)",
    "senate_control_kalshi_t1": "74% D / 26% R (-11.0 pp R shift from T-7; 75% D sweep on $96.6M Balance of Power combo)",
    "house_control_kalshi_t7": "90.9% D / 9.1% R",
    "house_control_kalshi_t1": "94% D / 6% R (RCP Generic Ballot D+8.5)",
    "mean_t7_senate_8comp_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in senate_comp8), 2),
    "mean_t7_senate_all9_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in senate_races), 2),
    "mean_t7_governor_4_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in gov_races), 2),
    "mean_t7_all13_markup_over_polls_pp": round(mean(r["t7_trader_markup_r"] for r in races), 2),
    "mean_t1_senate_8comp_markup_over_polls_pp": round(mean(r["t1_trader_markup_r"] for r in senate_comp8), 2),
    "mean_t1_senate_all9_markup_over_polls_pp": round(mean(r["t1_trader_markup_r"] for r in senate_races), 2),
    "mean_t1_governor_4_markup_over_polls_pp": round(mean(r["t1_trader_markup_r"] for r in gov_races), 2),
    "mean_t1_all13_markup_over_polls_pp": round(mean(r["t1_trader_markup_r"] for r in races), 2),
    "chambers": {
        "senate": {
            "t14_raw": "52 D - 48 R (0 Toss-Ups)",
            "t14_simple_debiased": "54 D - 46 R (0 Toss-Ups)",
            "t14_preferred": "53 D - 46 R (1 Toss-Up: KS)",
            "t7_raw": "52 D - 48 R (0 Toss-Ups)",
            "t7_simple_debiased": "54 D - 45 R (1 Toss-Up: NE)",
            "t7_preferred": "53 D - 46 R, 1 Toss-Up (IA Lean D at 57.8% D; KS uncalled Toss-Up at 49.1% D / 50.9% R)",
            "t1_raw": "53 D - 46 R, 1 Toss-Up (KS flips to 62.0% D; IA moves to 50.0% D / 50.0% R Toss-Up)",
            "t1_simple_debiased": "54 D - 46 R (0 Toss-Ups)",
            "t1_preferred": "54 D - 46 R, 0 Toss-Ups (IA Lean D at 64.5% D; KS Likely D at 69.4% D; NE Likely R at 66.9% R)",
        },
        "governors": {
            "t14_raw": "29 D - 21 R (0 Toss-Ups)",
            "t14_simple_debiased": "29 D - 20 R (1 Toss-Up: TX)",
            "t14_preferred": "29 D - 21 R (0 Toss-Ups)",
            "t7_raw": "29 D - 21 R (0 Toss-Ups)",
            "t7_simple_debiased": "29 D - 20 R (1 Toss-Up: TX)",
            "t7_preferred": "29 D - 21 R, 0 Toss-Ups (TX Lean R at 61.0% R; VT Likely R at 69.4% R)",
            "t1_raw": "29 D - 21 R (0 Toss-Ups)",
            "t1_simple_debiased": "30 D - 19 R (1 Toss-Up: VT; TX flips to 56.3% D)",
            "t1_preferred": "29 D - 21 R, 0 Toss-Ups (TX Lean R at 56.7% R; VT Lean R at 58.5% R)",
        },
        "house": {
            "t14_raw": "229 D - 195 R (11 Toss-Ups)",
            "t14_simple_debiased": "251 D - 174 R (10 Toss-Ups)",
            "t14_preferred": "241 D - 185 R (9 Toss-Ups)",
            "t7_raw": "234 D - 192 R (9 Toss-Ups)",
            "t7_simple_debiased": "254 D - 172 R (9 Toss-Ups)",
            "t7_preferred": "244 D - 183 R, 8 Toss-Ups (+10 called D seats over T-7 raw)",
            "t1_raw": f"{h_raw_d} D - {h_raw_r} R ({h_raw_tu} Toss-Ups)",
            "t1_simple_debiased": f"{h_sim_d} D - {h_sim_r} R ({h_sim_tu} Toss-Ups)",
            "t1_preferred": f"{h_prf_d} D - {h_prf_r} R, {h_prf_tu} Toss-Ups (+{h_prf_d - h_raw_d} called D seats and -{h_raw_r - h_prf_r} called R seats vs. T-1 raw)",
        },
    },
    "battlegrounds": races,
}

with open("/home/antigravity/midterm_2026_t7_results.json", "w") as f:
    json.dump(summary, f, indent=2)

with open("/home/antigravity/midterm_2026_battlegrounds.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(races[0].keys()))
    writer.writeheader()
    writer.writerows(races)

print("\nWrote updated midterm_2026_t7_results.json and midterm_2026_battlegrounds.csv successfully.")
