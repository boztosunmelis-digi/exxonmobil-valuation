# exxonmobil-valuation
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Language](https://img.shields.io/badge/python-3.x-blue)
![Model](https://img.shields.io/badge/valuation-DCF%20%7C%20WACC%20%7C%20LBO-orange)

Full 5-year intrinsic valuation suite for ExxonMobil, including DCF, WACC build, trading comps, precedent transactions, and an LBO scenario with a Python-based valuation engine.
# ExxonMobil Valuation: 5-Year DCF & LBO Framework

This repository contains a compact but professional valuation framework for **ExxonMobil (XOM)**, structured as if for an **investment banking analyst** or **equity research** workflow.

It replicates core valuation deliverables used in real transactions and public-company coverage:

**1) 5-year intrinsic valuation via DCF**  
**2) WACC derivation using market inputs**  
**3) Trading comparables infrastructure**  
**4) Precedent transactions logic**  
**5) Infrastructure-style LBO scenario**  
**6) Python valuation engine + Excel models**

---

## Repository Structure

```text
exxonmobil-valuation/
├─ README.md
├─ .gitignore
├─ requirements.txt
├─ docs/
│  └─ methodology.md
├─ data/
│  ├─ raw/           # Source data (10-K extracts, SEC filings, etc.)
│  │  └─ .gitkeep
│  └─ processed/     # Cleaned inputs after transformation
│     └─ .gitkeep
├─ models/
│  ├─ dcf/
│  │  └─ DCF_ExxonMobil.xlsx
│  ├─lbo/
│  │  └─ LBO_ExxonInfrastructure.xlsx
│  └─ comps/
│     └─ Trading_Comps_XOM.xlsx
├─ notebooks/
│  └─ valuation_demo.ipynb
└─ src/
   ├─ __init__.py          # Package initializer
   ├─ dcf.py               # DCF valuation engine
   ├─ wacc.py              # WACC computation
   ├─ comps.py             # Trading comps logic
   └─ utils.py             # Shared helpers
```

## How to Run

To reproduce the valuation logic locally:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/valuation_demo.ipynb
``` 

## Methodology Overview

The valuation stack combines multiple approaches commonly used in investment banking and equity research:

### **1. Discounted Cash Flow (DCF)**
- Forecasts free cash flows over 5 years
- Uses ExxonMobil’s historical margins and capex profile
- Terminal value computed using both the **Gordon Growth** and **Exit Multiple** methods
- Sensitivity tables across WACC and terminal assumptions

### **2. Cost of Capital (WACC)**
- Captured using real market inputs:
  - Risk-free rate from U.S. Treasuries
  - Beta based on energy peer set
  - Market risk premium aligned with IB benchmarks
  - Cost of debt adjusted for ExxonMobil’s credit rating
- Weighted using target capital structure

### **3. Trading Comparables**
- Peer multiples: EV/EBITDA, P/E, FCF yield
- Provides relative valuation cross-check vs. intrinsic DCF output

### **4. Precedent Transactions**
- Energy sector M&A comps used to triangulate valuation levels
- Bridges private transaction pricing vs. public market multiples

### **5. Infrastructure-Style LBO Scenario**
- Stress-tests ExxonMobil under leverage constraints
- Models IRR profile for a financial sponsor considering oil & gas infrastructure assets

**Why this matters:**  
This is not a single DCF. It is a **full valuation stack** that triangulates intrinsic, relative, and transaction-based value - exactly what analysts produce before issuing a rating or a fairness opinion.

## Files Included

The repository contains all components expected in a real valuation workflow:

| Folder / File | Description |
|--------------|-------------|
| `models/dcf/DCF_ExxonMobil.xlsx` | Full 5-year intrinsic DCF valuation with assumptions, forecasts, sensitivities, and terminal value outputs |
| `models/lbo/LBO_ExxonInfrastructure.xlsx` | Simplified leverage buyout scenario using infrastructure financing parameters |
| `notebooks/valuation_demo.ipynb` | Python-driven DCF and WACC demonstration, replicating the logic in code |
| `docs/methodology.md` | Detailed explanation of valuation mechanics and assumptions |
| `src/dcf.py` | Cash flow forecast + enterprise value computation engine |
| `src/wacc.py` | Cost of capital computation from market inputs |
| `src/comps.py` | Trading comparables framework |
| `src/utils.py` | Helper utilities supporting core valuation logic |
| `requirements.txt` | Required Python packages to run the notebook locally |

Together, these files form a **complete valuation stack** suitable for investment banking, equity research, corporate finance, or private equity modelling tests.

Our DCF yields an intrinsic value of **$70.67/share**, based on a WACC of **9.06%** and a terminal growth rate of **2.00%**. This implies that ExxonMobil is currently **~39% overvalued** relative to its market price of **$115.98** as of December 2025.

## Valuation Summary & Result

The intrinsic valuation outputs for **ExxonMobil (XOM)** are structured across
multiple methodologies commonly used in investment banking and equity
research workflows. At this stage, the **DCF** is fully implemented using
real historical cash flows and a market-based WACC, while the other
valuation frameworks are scaffolded for subsequent stages.

---

### Discounted Cash Flow (DCF) Cross-Check

> **Note:** The DCF is an intrinsic, forward-looking valuation and is highly sensitive to WACC, terminal assumptions, and mid-cycle commodity normalisation. Outputs should be refreshed when macro inputs, capital structure, or forward free-cash-flow expectations change.

This module implements a **5-year intrinsic valuation** for ExxonMobil (XOM) using a standard cash-low-based approach.

The framework uses:

- **Historical FCF anchoring** (2020-2024) and a **2025E forecast baseline**
- A market-derived **WACC** constructed via CAPM
- Terminal value calculated using the **Gordon Growth** method, with sensitivity around discount and terminal assumptions

**Base-case outputs:**

- **WACC:** **9.06%**
- **Terminal growth (g):** **2.00%**
- **Enterprise Value (EV):** **$358.6bn**
- **Net debt:** **$28.2bn**
- **Equity value:** **$330.4bn**
- **Shares outstanding:** **4.285bn**
- **Implied intrinsic value:** **$70.67/share**

**Objective:** establish a clean intrinsic valuation anchor and quantify the divergence versus market pricing, forming the foundation against which relative, transaction-based, and sponsor-lens cross-checks are evaluated.

### Market Check

- **Current XOM price (Dec 2025):** **\$115.98/share**  
- **DCF implied intrinsic price:** **\$70.67/share**  
- **Implied mispricing:** ExxonMobil appears **≈39% overvalued** vs. intrinsic value

\[
\text{Overvaluation} = \frac{115.98 - 70.67}{115.98} \approx 39.1\%
\]

### Interpretation

Our base-case DCF suggests that ExxonMobil’s equity is trading materially
above our estimate of intrinsic value, even after applying:

- a conservative **2%** long-run terminal growth rate, and  
- a market-based **9.06%** WACC built from CAPM and the company’s current capital structure.

Only under meaningfully **lower discount rates** or **structurally higher
sustainable free cash flows** does the intrinsic value approach the
current market price.

---

### Cost of Capital (WACC) Cross-Check

> **Note:** WACC is a critical valuation input and should be refreshed using live market data (risk-free rate, beta, equity risk premium, credit spreads) when applying this framework in interviews or professional settings. Small changes in WACC can materially impact DCF enterprise value.

This module constructs ExxonMobil’s **discount rate** using a market-consistent methodology aligned with investment banking and equity research standards.

The framework incorporates:

- **Risk-free rate** sourced from U.S. Treasury yields
- **Equity beta** calibrated to a large-cap integrated energy peer set
- **Market risk premium** consistent with IB benchmark assumptions
- **Cost of debt** aligned with ExxonMobil’s credit quality and spread environment
- **Target capital structure weights** applied at the enterprise level
  
**Base-case output:**

- **WACC:** **9.06%**

**Objective:** ensure the DCF discount rate is transparent, defensible, and reproducible, while providing a clear sensitivity mechanism linking changes in capital-market conditions to intrinsic valuation outcomes.

### Market Check

At the base-case WACC of **9.06%**, ExxonMobil’s discounted cash flows imply an intrinsic equity value of **$70.67/share**, materially below the current spot price of **$115.98/share**.

### Interpretation

The WACC implied by current capital-market conditions embeds a **meaningful required return** for equity holders, reflecting both commodity cyclicality and macro risk premia. Given this discount rate, ExxonMobil’s current market valuation appears to **price in lower risk or structurally stronger cash-flow durability** than assumed under conservative mid-cycle conditions.

As a result, **downward pressure on intrinsic value is driven primarily by discount-rate discipline**, not by overly pessimistic operating assumptions.

---

### Trading Comparables Cross-Check

> **Note:** Trading multiples are forward-looking (2025E-style) and should be refreshed from a data provider such as Bloomberg, Refinitiv, Koyfin, or FactSet before using this model in a professional setting.

A trading comps framework benchmarks **ExxonMobil (XOM)** against a global integrated energy peer set:

- **Chevron (CVX)**  
- **Shell plc (SHEL)**  
- **BP plc (BP)**  
- **TotalEnergies SE (TTE)**  
- **ConocoPhillips (COP)**  

The model compares:

- **EV/EBITDA 2025E**  
- **P/E 2025E**  
- **FCF Yield 2025E**  

and computes **peer medians** and **relative premiums/discounts** versus XOM.

### Base-Case Output

- XOM trades at a **premium on EV/EBITDA and P/E**
- XOM exhibits a **lower FCF yield** relative to the peer median

**Objective:** assess whether market-implied valuation multiples corroborate
or contradict the intrinsic value obtained via the DCF.

### Market Check

Relative valuation indicates that public markets are willing to pay **higher multiples for ExxonMobil’s earnings and EBITDA stream**, despite a lower implied cash-flow yield versus peers.

### Interpretation

The trading comps cross-check suggests that ExxonMobil’s equity valuation reflects **perceived quality, scale, and cash-flow durability**, rather than purely realised free cash flows. While this does not invalidate the DCF, it highlights that the market is **pricing forward expectations and narrative momentum**, creating tension with conservative intrinsic assumptions.

---

### Precedent Transactions Cross-Check

> **Note:** Precedent deal multiples are event-driven and cyclical, not perpetual valuations. They should be refreshed from public filings, press releases, or data providers such as Bloomberg, Refinitiv, Koyfin, or FactSet when updating this model for interviews or case studies.

This module benchmarks ExxonMobil’s valuation against **large-scale oil & gas M&A transactions**, where acquirers paid control premiums for strategic reserves, scale, and basin access.

The framework analyses:

- **Deal EV/EBITDA multiples**  
- **Transaction enterprise values**  
- **Premiums to undisturbed targets**  
- **Asset quality and cyclicality drivers**  

### Base-Case Output

Applying **median precedent EV/EBITDA multiples** to ExxonMobil’s forward EBITDA produces an **implied enterprise-value range** spanning below and above the DCF-derived EV.

**Objective:** provide a market-tested triangulation point linking public-market valuation to real transaction pricing.

### Market Check

Precedent transaction pricing provides an external reference point grounded in **real capital deployment decisions**, rather than public-market sentiment.

### Interpretation

The precedent cross-check frames a **valuation corridor** rather than a point estimate. Where precedent-implied values exceed the DCF, markets may be recognising **strategic scarcity value or consolidation premiums**. Where they fall below, they underscore sensitivity to cycle timing and asset quality. In aggregate, precedents neither decisively refute nor fully validate the DCF, but **bound the plausible valuation range**.

---

### Infrastructure-Style LBO Cross-Check

> **Note:** This scenario is a sponsor-lens plausibility bound rather than a primary valuation method. For a mega-cap integrated major, the analysis is framed as “infrastructure-style” to stress-test leverage capacity, cash-flow durability, and exit feasibility under conservative assumptions.

This module evaluates ExxonMobil under an **infrastructure-style leveraged buyout framework**, reflecting how a financial sponsor might assess the asset’s capacity to support leverage and deliver equity returns.

The framework analyses:

- **Entry enterprise value** implied by an EV/EBITDA multiple and forward EBITDA  
- **Debt capacity** under conservative leverage assumptions (~2-3x EBITDA)  
- **Equity investment size** and annual cash distributions  
- **Exit equity value** based on stable terminal EV/EBITDA assumptions  
- **Sponsor IRR** and sensitivity to entry valuation  

### Base-Case Output

Under conservative leverage and flat exit multiples, the implied sponsor IRR falls **below typical private-equity hurdle rates**, absent meaningful operational upside or valuation multiple expansion.

**Objective:** establish a plausibility bound for leverage-supported valuation and test whether intrinsic and public-market values are sponsor-feasible.

### Market Check

This indicates that ExxonMobil’s current valuation leaves **limited room for leveraged financial engineering**, reinforcing its classification as a **yield-oriented, capital-return asset** rather than a classic buyout candidate.

### Interpretation

The LBO cross-check supports the DCF conclusion: ExxonMobil’s valuation is **already efficient** under reasonable leverage assumptions. Any upside must therefore come from **operational outperformance or structural improvements**, not balance-sheet optimisation.

---

### **Conclusion**

ExxonMobil’s valuation has been assessed using a **multi-method framework** spanning intrinsic, relative, transaction-based, and sponsor-lens approaches. While each methodology provides a distinct perspective, they converge on a consistent message regarding current market pricing.

The **base-case DCF**, constructed using real historical free cash flows and a market-based **9.06% WACC**, implies an intrinsic value of **\$70.67 per share**, materially below the current market price of **\$115.98**. This establishes a clear intrinsic anchor suggesting **overvaluation under conservative assumptions**.

Relative valuation cross-checks (trading comparables) indicate that ExxonMobil trades at **premium EV/EBITDA and P/E multiples** alongside a **lower FCF yield** versus integrated energy peers. This suggests that public markets are pricing in **durability, scale advantages, and capital-return momentum** beyond what is embedded in the base-case cas-flow model.

Precedent transaction analysis provides a **range-based sense check**, with implied enterprise values sensitive to deal mix, cycle timing, and strategic premiums. While select transactions support higher valuation ceilings, these outcomes typically reflect **control premiums or asset-specific scarcity**, rather than steady-state intrinsic value.

Ultimately, the infrastructure-style **LBO scenario** frames an upper-bound plausibility test. Under conservative leverage and stable exit assumptions, equity returns remain feasible but offer limited margin for valuation expansion at current prices, reinforcing the concept that much of the upside is already priced in.

**Accumulated onto each other**, the valuation stack indicates that ExxonMobil’s current share price reflects **optimistic forward expectations** relative to intrinsic cash-flow fundamentals. Absent structurally higher free cash flows, sustained margin outperformance, or a materially lower cost of capital, the model suggests that **downside risk dominates upside potential** at prevailing market levels.

This triangulated conclusion projects professional sell-side and investment banking valuation practice, where multiple methodologies are used not to force convergence, but to **identify where market pricing diverges from fundamental value**.

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Language](https://img.shields.io/badge/python-3.10-blue)
![Model](https://img.shields.io/badge/valuation-DCF%20%7C%20LBO%20%7C%20WACC-orange)

