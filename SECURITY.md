# Security Policy

## Scope

This repository contains **analytical and educational financial models**
(DCF, WACC, trading comparables, precedent transactions, and LBO scenarios)
implemented in Python, Excel, and Jupyter notebooks.

It is **not a production system**, API, or deployed service, and it does not
process live user data.

The code and models are provided under the **MIT License** for learning,
research, and demonstration purposes only.

---

## Supported Versions

This repository does not maintain versioned releases with ongoing security
patches.

Users are expected to:
- run the code locally,
- inspect dependencies before installation, and
- update Python packages as needed via `requirements.txt`.

---

## Dependency Advisories

This repository may include development-time dependencies (e.g. Jupyter, nbconvert)
that trigger automated vulnerability alerts.

### nbconvert (Windows-only advisory)
A Dependabot advisory exists for `nbconvert` related to PDF conversion on Windows
platforms involving uncontrolled search paths.

**Impact assessment:**
- Affects Windows systems only
- Requires local execution (''jupyter nbconvert to pdf'')
- Not applicable to macOS/Linux workflows
- Not used in automated or production pipelines

**Mitigation:**
- PDF conversion is not required to run or reproduce this project
- Users are advised to avoid PDF export via nbconvert on Windows
- HTML/PNG exports are used for all documentation artifacts

---

## Reporting a Vulnerability

If you believe you have identified a **security issue** (e.g. malicious
dependency behavior, unsafe file handling, or unintended data exposure),
please report it responsibly.

### How to report
- Open a **private GitHub security advisory**, or
- Contact the repository maintainer directly via GitHub profile messaging.

### What to include
- A clear description of the issue
- Steps to reproduce (if applicable)
- Any relevant logs or screenshots

### Response expectations
- You can expect an acknowledgement within **7 days**
- If accepted, the issue will be addressed or documented
- If declined, a brief explanation will be provided

---

## Financial Disclaimer

This repository **does not constitute investment advice**.

All valuation outputs are:
- illustrative,
- assumption-driven, and
- subject to material uncertainty.

No responsibility is accepted for decisions made based on these models.
