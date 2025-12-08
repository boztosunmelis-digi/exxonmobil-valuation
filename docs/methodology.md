# ExxonMobil Valuation – Methodology

This document summarises the valuation logic implemented in the repository.

## 1. DCF Framework

- Forecasts 5 years of free cash flow for ExxonMobil (XOM).
- Uses an explicit forecast period followed by a terminal value.
- Terminal value can be computed via:
  - Gordon Growth model, or
  - Exit multiple approach (EV/EBITDA).
- Enterprise value = PV of forecast FCFs + PV of terminal value.

## 2. WACC

- WACC is built from:
  - Risk–free rate (US Treasuries),
  - Equity beta for integrated oil & gas peers,
  - Market risk premium,
  - Cost of debt consistent with Exxon’s credit profile,
  - Target capital structure (D/E).
- After–tax cost of debt is used: \( r_d (1 - T) \).

## 3. Trading Comparables

- Peer set: large-cap integrated energy names.
- Key multiples: EV/EBITDA, P/E, FCF yield.
- Used as a cross–check to the intrinsic DCF output.

## 4. Precedent Transactions

- Uses energy sector M&A deals to anchor valuation levels.
- Focus on deal EV/EBITDA and premium to undisturbed share price.

## 5. LBO Scenario

- Illustrative infrastructure–style LBO:
  - Leverage within conservative infrastructure ranges,
  - Debt schedule and exit at year 5,
  - Sponsor IRR profile based on entry/exit assumptions.

## 6. Limitations

- This framework is educational and not investment advice.
- All numbers are placeholders until real ExxonMobil data and assumptions are plugged into the models.
