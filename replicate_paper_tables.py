#!/usr/bin/env python3
"""
Standalone Replication Script for:
"Partisan Pricing Bias in U.S. Political Prediction Markets: Empirical Evidence Across 455 Elections (2012-2026)"
(`partisan_pricing_bias_in_us_political_prediction_markets.md`) and `supplemental_tables.md`.

Author: Andres Ollarvez

This script reads `verified_election_markets_2012_2026.csv` and `midterm_2026_t7_results.json`
directly from disk (using only the Python standard library) and reproduces every table,
exact Student-t p-value, decomposition, price-controlled wrong-call regression, Brier
calibration score, and locked 2026 pre-election forecast summary.
"""

import csv
import json
import math
from collections import defaultdict
from statistics import mean, stdev


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def t_pval_exact(t_stat: float, df: int) -> float:
    x = abs(t_stat)
    if df <= 0 or x == 0.0:
        return 1.0
    phi0 = math.atan(math.sqrt(df) / x)
    n_steps = 400
    h = phi0 / n_steps
    log_pref = math.log(2.0) + math.lgamma(0.5 * (df + 1.0)) - 0.5 * math.log(math.pi) - math.lgamma(0.5 * df)

    def f(phi: float) -> float:
        if phi <= 0.0:
            return math.exp(log_pref) if df == 1 else 0.0
        return math.exp(log_pref + (df - 1.0) * math.log(math.sin(phi)))

    acc = f(0.0) + f(phi0)
    for i in range(1, n_steps):
        acc += (4.0 if i % 2 == 1 else 2.0) * f(i * h)
    return min(1.0, max(0.0, acc * h / 3.0))


def ols_fit(y, X):
    n = len(y)
    k = len(X[0])
    XtX = [[sum(X[i][r] * X[i][c] for i in range(n)) for c in range(k)] for r in range(k)]
    Xty = [sum(X[i][r] * y[i] for i in range(n)) for r in range(k)]
    aug = [XtX[r][:] + [Xty[r]] for r in range(k)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(col, k + 1):
            aug[col][j] /= div
        for r in range(k):
            if r != col:
                factor = aug[r][col]
                for j in range(col, k + 1):
                    aug[r][j] -= factor * aug[col][j]
    beta = [aug[r][k] for r in range(k)]
    y_hat = [sum(X[i][j] * beta[j] for j in range(k)) for i in range(n)]
    y_bar = mean(y)
    ss_tot = sum((yi - y_bar) ** 2 for yi in y)
    ss_res = sum((y[i] - y_hat[i]) ** 2 for i in range(n))
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 0.0

    # Compute standard errors via (X'X)^(-1)
    aug_inv = [XtX[r][:] + [1.0 if r == c else 0.0 for c in range(k)] for r in range(k)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(aug_inv[r][col]))
        aug_inv[col], aug_inv[piv] = aug_inv[piv], aug_inv[col]
        div = aug_inv[col][col]
        for j in range(2 * k):
            aug_inv[col][j] /= div
        for r in range(k):
            if r != col:
                fac = aug_inv[r][col]
                for j in range(2 * k):
                    aug_inv[r][j] -= fac * aug_inv[col][j]
    inv_XtX = [row[k:] for row in aug_inv]
    sigma2 = ss_res / max(1, n - k)
    ses = [math.sqrt(max(0.0, sigma2 * inv_XtX[j][j])) for j in range(k)]
    return beta, ses, r2


def load_dataset(csv_path="verified_election_markets_2012_2026.csv"):
    with open(csv_path, newline="") as f:
        records = list(csv.DictReader(f))
    for r in records:
        r["race_id"] = int(r["race_id"])
        r["gop_win"] = int(r["gop_win"])
        r["gop_fav"] = int(r["gop_fav"])
        r["fav_upset"] = int(r["fav_upset"])
        r["diverse_or_female_dem"] = int(r["diverse_or_female_dem"])
        r["gop_20yr_win_share"] = int(r["gop_20yr_win_share"])
        for num_col in [
            "cook_pvi_num",
            "turnout_vep_pct",
            "poll_margin_r_minus_d",
            "poll_win_prob_r_55sd",
            "mkt_t1_r",
            "net_market_bias_pp",
            "poll_bias_pp",
            "trader_markup_pp",
            "brier_mkt",
            "brier_poll",
        ]:
            r[num_col] = float(r[num_col])
    return records


def summarize_cohort(name, rows):
    n = len(rows)
    avg_mkt = mean(r["mkt_t1_r"] for r in rows)
    avg_win = mean(r["gop_win"] * 100.0 for r in rows)
    avg_poll = mean(r["poll_win_prob_r_55sd"] for r in rows)
    biases = [r["net_market_bias_pp"] for r in rows]
    markups = [r["trader_markup_pp"] for r in rows]
    brier_m = mean(r["brier_mkt"] for r in rows)
    brier_p = mean(r["brier_poll"] for r in rows)
    clusters = [r["election_date"] for r in rows]

    se_race = stdev(biases) / math.sqrt(n) if n > 1 else 0.0
    t_race = mean(biases) / se_race if se_race > 0 else 0.0
    p_race = t_pval_exact(t_race, max(1, n - 1))

    by_c = defaultdict(list)
    for b, c in zip(biases, clusters):
        by_c[c].append(b)
    G = len(by_c)
    if G > 1:
        ss_c = sum((sum(v - mean(biases) for v in vals)) ** 2 for vals in by_c.values())
        var_c = (G / (G - 1.0)) * ss_c / (n * n)
        se_c = math.sqrt(max(1e-12, var_c))
        t_c = mean(biases) / se_c
        p_c = t_pval_exact(t_c, G - 1)
    else:
        p_c = None

    gop_favs = [r for r in rows if r["gop_fav"] == 1]
    dem_favs = [r for r in rows if r["gop_fav"] == 0]
    gop_upsets = sum(1 for r in gop_favs if r["gop_win"] == 0)
    dem_upsets = sum(1 for r in dem_favs if r["gop_win"] == 1)
    tot_upsets = gop_upsets + dem_upsets

    return {
        "name": name,
        "n": n,
        "dates": G,
        "avg_mkt_r": round(avg_mkt, 1),
        "actual_gop_win": round(avg_win, 1),
        "net_bias_pp": round(mean(biases), 2),
        "poll_bias_pp": round(avg_poll - avg_win, 2),
        "trader_markup_pp": round(mean(markups), 2),
        "brier_mkt": round(brier_m, 4),
        "brier_poll": round(brier_p, 4),
        "p_clustered": round(p_c, 4) if p_c is not None else None,
        "p_race_level": round(p_race, 4),
        "gop_fav_n": len(gop_favs),
        "gop_upsets": gop_upsets,
        "gop_upset_rate": round(100.0 * gop_upsets / len(gop_favs), 1) if gop_favs else 0.0,
        "dem_fav_n": len(dem_favs),
        "dem_upsets": dem_upsets,
        "dem_upset_rate": round(100.0 * dem_upsets / len(dem_favs), 1) if dem_favs else 0.0,
        "tot_upsets": tot_upsets,
        "wrong_calls_pro_gop_pct": round(100.0 * gop_upsets / tot_upsets, 1) if tot_upsets else 0.0,
    }


def main():
    records = load_dataset()
    print(f"Loaded {len(records)} verified elections (2012-2026).")

    # Table 1, Table 2 & Table 6 Cohorts
    cohorts = [
        ("All 455 Verified Elections (2012-2026)", records),
        ("Table 1 Row 1: Pre-2016 Control (2012-14)", [r for r in records if r["era"] == "Pre2016"]),
        ("Table 1 Row 2: All Modern (2016-2026)", [r for r in records if r["era"] == "Modern"]),
        ("Table 1 Row 3: Pres Top-of-Ticket (16/20/24)", [r for r in records if r["cycle_group"] == "Pres_Top"]),
        ("Table 1 Row 4: Pres-Year Down-Ballot (16/20/24)", [r for r in records if r["cycle_group"] == "Pres_Downballot"]),
        ("Table 1 Row 5: Modern Midterms Pool (18 & 22)", [r for r in records if r["cycle_group"] in ("Midterm_2018", "Midterm_2022")]),
        ("Table 1 Row 5a: 2018 Midterms Alone", [r for r in records if r["cycle_group"] == "Midterm_2018"]),
        ("Table 1 Row 5b: 2022 Midterms Alone", [r for r in records if r["cycle_group"] == "Midterm_2022"]),
        ("Table 1 Row 6: Modern Specials / Off-Yr (17-26)", [r for r in records if "Special" in r["cycle_group"]]),
        ("Table 1 Row 7: All Modern Non-Pres (Rows 5+6)", [r for r in records if r["cycle_group"] in ("Midterm_2018", "Midterm_2022", "Special_PreDobbs", "Special_PostDobbs")]),
        ("Table 1 Row 8: All Modern Down-Ballot (Rows 4+7)", [r for r in records if r["era"] == "Modern" and r["cycle_group"] != "Pres_Top"]),
        ("Table 2 Row 2: Pre-Dobbs Specials (17-Jun 22)", [r for r in records if r["cycle_group"] == "Special_PreDobbs"]),
        ("Table 2 Row 3: Pre-Dobbs Non-Pres (17-Jun 22)", [r for r in records if r["cycle_group"] in ("Midterm_2018", "Special_PreDobbs")]),
        ("Table 2 Row 4: Post-Dobbs Specials (Jul 22-26)", [r for r in records if r["cycle_group"] == "Special_PostDobbs"]),
        ("Table 2 Row 5: Post-Dobbs Non-Pres (Jul 22-26)", [r for r in records if r["cycle_group"] in ("Midterm_2022", "Special_PostDobbs")]),
    ]

    print("\n=== TABLES 1, 2 & 6: COHORT BIAS, MARKUP, UPSETS & BRIER CALIBRATION ===")
    for name, rows in cohorts:
        s = summarize_cohort(name, rows)
        pcl_str = f"{s['p_clustered']:.4f}" if s["p_clustered"] is not None else "  N/A "
        print(
            f"{s['name']:48s} | N={s['n']:3d} (G={s['dates']:2d}) | Mkt={s['avg_mkt_r']:5.1f}% Win={s['actual_gop_win']:5.1f}% | "
            f"Bias={s['net_bias_pp']:+6.2f}pp (p_cl={pcl_str}, p_rc={s['p_race_level']:.4f}) | "
            f"Markup={s['trader_markup_pp']:+6.2f}pp | GOP_Upset={s['gop_upsets']}/{s['gop_fav_n']} ({s['gop_upset_rate']:4.1f}%) vs "
            f"Dem={s['dem_upsets']}/{s['dem_fav_n']} ({s['dem_upset_rate']:4.1f}%) | Brier={s['brier_mkt']:.4f} vs {s['brier_poll']:.4f}"
        )

    nonpres = [r for r in records if r["cycle_group"] in ("Midterm_2018", "Midterm_2022", "Special_PreDobbs", "Special_PostDobbs")]

    # Price-controlled wrong-call regressions
    X_all = [[1.0, float(r["gop_fav"]), max(r["mkt_t1_r"], 100.0 - r["mkt_t1_r"]) - 50.0] for r in nonpres]
    y_all = [r["fav_upset"] * 100.0 for r in nonpres]
    b_all, se_all, _ = ols_fit(y_all, X_all)
    t_all = b_all[1] / se_all[1]

    clear = [r for r in nonpres if r["market_tier"] != "1_TossUp_45_55"]
    X_clr = [[1.0, float(r["gop_fav"]), max(r["mkt_t1_r"], 100.0 - r["mkt_t1_r"]) - 55.0] for r in clear]
    y_clr = [r["fav_upset"] * 100.0 for r in clear]
    b_clr, se_clr, _ = ols_fit(y_clr, X_clr)
    t_clr = b_clr[1] / se_clr[1]

    print("\n=== PRICE-CONTROLLED WRONG-CALL REGRESSIONS ===")
    print(f"All Non-Pres Favorites (N={len(nonpres)}): Excess GOP Upset = {b_all[1]:+.2f} pp (SE={se_all[1]:.2f}, t={t_all:.2f})")
    print(f"Clear Favorites >=55c  (N={len(clear)}): Excess GOP Upset = {b_clr[1]:+.2f} pp (SE={se_clr[1]:.2f}, t={t_clr:.2f})")

    # Table 3, S3, S4 & Structural Regressions
    print("\n=== TABLE 3 & S3: STATE REDNESS & SEAT INCUMBENCY (N=225) ===")
    struct_groups = [
        ("1. Red States (>=65% GOP)", [r for r in nonpres if r["redness_tier"] == "Red_State"]),
        ("2. Purple States (35-65%)", [r for r in nonpres if r["redness_tier"] == "Purple_State"]),
        ("3. Blue States (<=35% GOP)", [r for r in nonpres if r["redness_tier"] == "Blue_State"]),
        ("4. GOP-Held Seat (All)", [r for r in nonpres if r["seat_status"] in ("Elected_R_Inc", "Open_Appt_R")]),
        ("4a. Elected GOP Incumbent", [r for r in nonpres if r["seat_status"] == "Elected_R_Inc"]),
        ("4b. Open / Appt. GOP Seat", [r for r in nonpres if r["seat_status"] == "Open_Appt_R"]),
        ("5. Dem-Held Seat", [r for r in nonpres if r["seat_status"] == "Dem_Seat"]),
    ]
    for sname, srows in struct_groups:
        s = summarize_cohort(sname, srows)
        print(
            f"{s['name']:28s} | N={s['n']:3d} | Win={s['actual_gop_win']:5.1f}% | "
            f"PollBias={s['poll_bias_pp']:+6.2f}pp | Markup={s['trader_markup_pp']:+6.2f}pp | "
            f"TotalBias={s['net_bias_pp']:+6.2f}pp (p_rc={s['p_race_level']:.4f}) | GOP_Upset={s['gop_upsets']}/{s['gop_fav_n']} ({s['gop_upset_rate']:4.1f}%)"
        )

    y_win = [float(r["gop_win"]) for r in nonpres]
    X_red = [[1.0, 1.0 if r["redness_tier"] == "Red_State" else 0.0, 1.0 if r["redness_tier"] == "Purple_State" else 0.0] for r in nonpres]
    X_inc = [[1.0, 1.0 if r["seat_status"] == "Elected_R_Inc" else 0.0, 1.0 if r["seat_status"] == "Open_Appt_R" else 0.0] for r in nonpres]
    _, _, r2_red = ols_fit(y_win, X_red)
    _, _, r2_inc = ols_fit(y_win, X_inc)
    y_bias = [r["net_market_bias_pp"] for r in nonpres]
    X_demo = [
        [
            1.0,
            float(r["diverse_or_female_dem"]),
            1.0 if r["redness_tier"] == "Red_State" else 0.0,
            1.0 if r["redness_tier"] == "Purple_State" else 0.0,
            1.0 if r["seat_status"] == "Elected_R_Inc" else 0.0,
            1.0 if r["seat_status"] == "Open_Appt_R" else 0.0,
        ]
        for r in nonpres
    ]
    b_dem, se_dem, _ = ols_fit(y_bias, X_demo)
    t_dem = b_dem[1] / se_dem[1]
    p_dem = t_pval_exact(t_dem, len(nonpres) - len(X_demo[0]))
    print(f"Actual Win R^2: Redness Tiers = {r2_red:.3f}, Incumbency Tiers = {r2_inc:.3f}")
    print(f"Demographic Control Coef (N=225): {b_dem[1]:+.2f} pp (SE={se_dem[1]:.2f}, t={t_dem:.2f}, p={p_dem:.4f})")

    # Table 4 & Table 5
    print("\n=== TABLE 4: PLATFORMS (NON-PRESIDENTIAL & KALSHI VERIFIED) ===")
    plat_groups = [
        ("PredictIt Non-Pres (2017-24)", [r for r in nonpres if "PredictIt" in r["platforms"]]),
        ("Polymarket Non-Pres (2021-26)", [r for r in nonpres if "Polymarket" in r["platforms"]]),
        ("Kalshi Non-Pres Specials (24-26)", [r for r in nonpres if "Kalshi" in r["platforms"]]),
        ("Kalshi All Down-Ballot (24-26)", [r for r in records if "Kalshi" in r["platforms"] and r["office"] != "Pres"]),
        ("Kalshi All Verified (Oct 24-26)", [r for r in records if "Kalshi" in r["platforms"]]),
    ]
    for pname, prows in plat_groups:
        s = summarize_cohort(pname, prows)
        print(
            f"{s['name']:32s} | N={s['n']:3d} | Mkt={s['avg_mkt_r']:5.1f}% Win={s['actual_gop_win']:5.1f}% | "
            f"Markup={s['trader_markup_pp']:+6.2f}pp | Bias={s['net_bias_pp']:+6.2f}pp (p_rc={s['p_race_level']:.4f}) | "
            f"Upsets={s['gop_upset_rate']:4.1f}% vs {s['dem_upset_rate']:4.1f}%"
        )

    print("\n=== TABLE 5: 4 MARKET PROBABILITY TIERS (N=225) ===")
    for tlabel, trows in [
        ("1. Toss-Up (45%-55%)", [r for r in nonpres if r["market_tier"] == "1_TossUp_45_55"]),
        ("2. Lean (55%-65%)", [r for r in nonpres if r["market_tier"] == "2_Lean_55_65"]),
        ("3. Likely (65%-85%)", [r for r in nonpres if r["market_tier"] == "3_Likely_65_85"]),
        ("4. Safe / Solid (>85%)", [r for r in nonpres if r["market_tier"] == "4_Safe_gt85"]),
        ("Excl. Toss-Ups (>=55%)", clear),
    ]:
        s = summarize_cohort(tlabel, trows)
        print(
            f"{s['name']:24s} | N={s['n']:3d} ({s['gop_fav_n']}R/{s['dem_fav_n']}D) | "
            f"GOP_Upset={s['gop_upsets']}/{s['gop_fav_n']} ({s['gop_upset_rate']:4.1f}%) | "
            f"Dem_Upset={s['dem_upsets']}/{s['dem_fav_n']} ({s['dem_upset_rate']:4.1f}%) | "
            f"Bias={s['net_bias_pp']:+6.2f}pp (Markup={s['trader_markup_pp']:+6.2f}pp, p={s['p_race_level']:.4f}) | "
            f"Brier={s['brier_mkt']:.4f} vs {s['brier_poll']:.4f}"
        )

    with open("midterm_2026_t7_results.json") as f:
        m26 = json.load(f)
    print("\n=== 2026 PRE-ELECTION SNAPSHOT SUMMARY (T-14 -> T-7 -> T-1) ===")
    print(
        "Senate Control (T-14 -> T-7 -> T-1):",
        m26["senate_control_kalshi_t14"],
        "->",
        m26["senate_control_kalshi_t7"],
        "->",
        m26["senate_control_kalshi_t1"],
    )
    print("Senate Preferred (T-7 -> T-1):", m26["chambers"]["senate"]["t7_preferred"], "->", m26["chambers"]["senate"]["t1_preferred"])
    print("Gov Preferred    (T-7 -> T-1):", m26["chambers"]["governors"]["t7_preferred"], "->", m26["chambers"]["governors"]["t1_preferred"])
    print("House Preferred  (T-7 -> T-1):", m26["chambers"]["house"]["t7_preferred"], "->", m26["chambers"]["house"]["t1_preferred"])


if __name__ == "__main__":
    main()
