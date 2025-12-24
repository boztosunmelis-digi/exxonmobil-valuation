import os
import pandas as pd

SPOT_PRICE = 115.98
AS_OF_STR = "December 2025"

def main():
    # Ensure folders exist
    os.makedirs("docs", exist_ok=True)
    os.makedirs("docs/figures", exist_ok=True)

    # Load final valuation export
    df = pd.read_csv("data/processed/xom_final_valuation.csv")
    row = df.iloc[0]

    wacc = float(row["wacc"])
    g_terminal = float(row["g_terminal"])
    ev_bn = float(row["enterprise_value_bn"])
    net_debt_bn = float(row["net_debt_bn"])
    equity_value_bn = float(row["equity_value_bn"])
    shares_bn = float(row["shares_outstanding_bn"])
    implied_price = float(row["implied_price_usd"])

    mispricing_pct = (SPOT_PRICE / implied_price - 1.0) * 100.0
    over_under = "overvalued" if mispricing_pct > 0 else "undervalued"

    md = f"""# ExxonMobil (XOM) — Analyst Summary (Stage 9)

**As of:** {AS_OF_STR}  
**Universe:** Integrated Oil & Gas  
**Methodologies:** DCF (intrinsic), Trading Comps (relative), Precedents (range framing), Infrastructure-style LBO (sponsor lens)

---

## Valuation Summary (auto-generated)

- **WACC:** **{wacc*100:.2f}%**
- **Terminal growth:** **{g_terminal*100:.2f}%**
- **Enterprise Value (EV):** **${ev_bn:,.1f}bn**
- **Net debt:** **${net_debt_bn:,.1f}bn**
- **Equity value:** **${equity_value_bn:,.1f}bn**
- **Shares outstanding:** **{shares_bn:.3f}bn**
- **Implied value per share:** **${implied_price:,.2f}**
- **Spot price:** **${SPOT_PRICE:,.2f}**
- **Mispricing:** **{mispricing_pct:+.0f}% ({over_under})**

---

## Figures

![EV vs WACC](figures/ev_vs_wacc.png)  
![Comps multiples](figures/comps_multiples_bar.png)  
![FCF yield](figures/fcf_yield_bar.png)  
![IRR sensitivity](figures/irr_sensitivity.png)
"""
    with open("docs/analyst_summary.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("Wrote: docs/analyst_summary.md")

if __name__ == "__main__":
    main()
