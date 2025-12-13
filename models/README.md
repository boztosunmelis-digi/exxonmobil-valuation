# Valuation Models

This folder contains the **canonical, presentation-grade Excel valuation models**
generated from the Python valuation engine that underpins this project.

The Python codebase serves as the **single source of truth** for all financial
logic and assumptions, while the Excel files represent the **final analyst-facing
outputs** suitable for review, presentation, and scenario analysis.

---

## Discounted Cash Flow Models (`models/dcf/`)

This folder contains the Excel discounted cash flow models derived from the
Python DCF engine and aligned with the intrinsic valuation framework.

- `DCF_ExxonMobil.xlsx`  
  Core 5-year intrinsic valuation model incorporating operating forecasts,
  WACC-based discounting, and terminal value assumptions.

---

## Trading Comparables Models (`models/comps/`)

This folder contains Excel trading comparables models generated from the
Python valuation engine and aligned with **Stage 6** of the analysis.

These files represent the canonical, presentation-grade **relative valuation**
outputs (EV/EBITDA, P/E, FCF Yield) used to cross-check the intrinsic DCF and
assess market-implied expectations.

---

## Leveraged Buyout Models (`models/lbo/`)

This folder contains the infrastructure-style leveraged buyout models derived
from the Python LBO engine and aligned with **Stage 8** of the analysis.

- `LBO_ExxonInfrastructure.xlsx`  
  Illustrative sponsor-style LBO scenario focusing on leverage capacity,
  cash-flow durability, and IRR sensitivity under conservative assumptions.

---

## Model Governance

- **Python notebooks and modules** define all assumptions, calculations, and logic  
- **Excel files** are generated outputs and should not be manually altered  
- Any updates to valuation logic should be implemented in Python and
  regenerated to Excel to preserve model integrity
