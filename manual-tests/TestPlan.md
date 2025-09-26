
# Test Plan – Web + Data (E‑commerce Module)

## Scope
- Web flows: Login, Catalog, Cart, Checkout, Orders
- Data flows: Orders ETL (staging → DWH), KPIs (revenue, conversion)

## Strategy
- Manual tests for critical UX; automation for regression (web/API)
- Data quality checks at staging & warehouse
- Environments: DEV/STAGE; Browsers: Chrome/Firefox; Mobile: Android WebView

## Exit Criteria
- 0 critical defects open; < 2 high severity open with workarounds
- Data quality gates green (PK unique, non-null, totals within ±2%)
