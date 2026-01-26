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

This repository may include development-time or transitive dependencies that
trigger automated vulnerability alerts. These advisories are reviewed and
addressed using a risk-based, usage-aware security posture.

---

### nbconvert (Windows-only advisory)

A Dependabot advisory exists for `nbconvert` related to PDF conversion on Windows
platforms involving uncontrolled search paths.

**Impact assessment:**
- Affects Windows systems only
- Requires local execution (`jupyter nbconvert --to pdf`)
- Not applicable to macOS or Linux environments
- Not used in automated, CI, or production workflows

**Mitigation:**
- PDF export is not required to run or reproduce this project
- Documentation artifacts are exported as HTML or PNG
- Users on Windows are advised to avoid PDF conversion via `nbconvert`

---

### protobuf (JSON recursion depth advisory)

A denial-of-service (DoS) vulnerability has been reported in
`google.protobuf.json_format.ParseDict()` related to recursion depth bypass when
parsing nested `google.protobuf.Any` messages.

**Context:**
- `protobuf` is included only as a **transitive dependency** (e.g., via
  market-data libraries such as `yfinance`)
- This repository does **not** parse or deserialise untrusted JSON into protocol
  buffer messages
- The vulnerable API (`google.protobuf.json_format.ParseDict()`) is not invoked
  anywhere in the codebase

**Mitigation:**
- No untrusted JSON is parsed into protobuf structures
- No protobuf `Any` deserialisation logic is used
- Dependency updates are monitored, and parent libraries are kept current
- Risk is mitigated through constrained usage rather than forced pinning, given
  the **absence of an upstream patch** at the time of writing

---

### urllib3 (version constraint advisory)

A security advisory affecting older versions of `urllib3` was flagged via
automated dependency surveillance.

**Mitigation:**
- The project explicitly enforces `urllib3>=2.6.3` in `requirements.txt`
- Local environments have been updated accordingly
- No custom HTTP client logic is implemented beyond the standard library implementation

---

## Security posture

This repository does not process untrusted user input, does not deserialise
arbitrary JSON into protocol buffer messages, and does not expose network-facing
services.

Dependencies are used in a constrained, research-oriented context and are kept
up to date where feasible. Known upstream vulnerabilities without patched
releases are mitigated through controlled usage, scope limitation, and
continuous dependency surveillance.

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
