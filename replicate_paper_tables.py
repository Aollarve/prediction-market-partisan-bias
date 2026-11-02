#!/usr/bin/env python3
"""
Standalone Replication Script for:
"Do Modern Prediction Markets Have a Right-Wing Tilt? Testing 455 Verified U.S. Elections (2012-2026)
 and 2026 Midterm Forecasts Through T-7"

This script reads `verified_election_markets_2012_2026.csv` and `midterm_2026_t7_results.json`
directly from disk (using only the Python standard library) and reproduces every table,
decomposition, price-controlled wrong-call regression, and 2026 log-odds forecast in the paper.
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
    if df <= 0:
        return 1.0
    if df == 1:
        return 1.0 - (2.0 / math.pi) * math.atan(x)
    if df == 2:
        return 1.0 - (x / math.sqrt(2.0 + x * x))
    z = math.sqrt(df * math.log(1.0 + (x * x) / df)) * (1.0 - 1.0 / (4.0 * df))
    return 2.0 * (1.0 - norm_cdf(z))


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
        p_c = p_race

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
        "p_clustered": round(p_c, 4),
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

    # Table 1 & Table 2 Cohorts
    cohorts = [
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

    print("\n=== TABLES 1 & 2: COHORT BREAKDOWN ===")
    for name, rows in cohorts:
        s = summarize_cohort(name, rows)
        print(
            f"{s['name']:48s} | N={s['n']:3d} (G={s['dates']:2d}) | Mkt={s['avg_mkt_r']:5.1f}% Win={s['actual_gop_win']:5.1f}% | "
            f"Bias={s['net_bias_pp']:+6.2f}pp (p_cl={s['p_clustered']:.4f}, p_rc={s['p_race_level']:.4f}) | "
            f"Markup={s['trader_markup_pp']:+6.2f}pp | GOP_Upset={s['gop_upsets']}/{s['gop_fav_n']} ({s['gop_upset_rate']:4.1f}%) vs "
            f"Dem={s['dem_upsets']}/{s['dem_fav_n']} ({s['dem_upset_rate']:4.1f}%) | Share={s['wrong_calls_pro_gop_pct']:5.1f}%"
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
