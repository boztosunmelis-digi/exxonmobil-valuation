# ExxonMobil (XOM) - Analyst Summary (Stage 9)

**As of:** December 2025  
**Universe:** Integrated Oil & Gas  
**Methodologies:** DCF (intrinsic), Trading Comps (relative), Precedents (range framing), Infrastructure-style LBO (sponsor lens)

---

## Investment View

Our intrinsic valuation framework (DCF) implies an equity value below the current spot price, indicating **overvalued risk** under base-case assumptions. The market’s premium multiples suggest investors are pricing in durability and capital return momentum beyond what is embedded in conservative cash-flow forecasts.

**Spot price (user input):** $115.98

---

## Valuation Summary

### 1) Intrinsic Value - DCF
- **WACC:** **9.06%**
- **Terminal growth:** **2.00%**
- **Enterprise Value (EV):** **$330.1bn**
- **Net debt:** **$28.2bn**
- **Equity value:** **$301.9bn**
- **Shares outstanding:** **4.285bn**
- **Implied value per share:** **$70.45**

**Market check:** XOM is currently **overvalued by 65%** vs the DCF base case.

![EV vs WACC](figures/ev_vs_wacc.png)

### 2) Relative Value - Trading Comps (Stage 6)

![Comps bar chart](figures/comps_multiples_bar.png)  
![FCF yield bar chart](figures/fcf_yield_bar.png)

### 3) Precedent Transactions (Stage 7)
Precedent EV/EBITDA multiples provide a range-based check against intrinsic value. Results depend on deal mix, cycle point, and synergy expectations.

### 4) Infrastructure-style LBO (Stage 8)

![IRR sensitivity](figures/irr_sensitivity.png)

A sponsor lens frames feasible leverage and equity IRR outcomes under conservative leverage and stable exit multiples. This is used as a plausibility bound rather than a primary valuation anchor.

---

## Artifacts Produced
- **Models:** `models/dcf/`, `models/comps/`, `models/lbo/`
- **Final valuation export:** `data/processed/xom_final_valuation.csv`
- **Figures:** `docs/figures/`
