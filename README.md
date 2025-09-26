 QA & Data ETL Validation – Portfolio

This repository showcases **Manual QA**, **API testing**, and **Data/ETL validation** patterns I use in real projects.
It includes:
- Test plans and test cases (manual & exploratory)
- Postman collection for API tests
- Python data quality checks for ETL pipelines (staging → warehouse)
- SQL scripts for reconciliation and anomaly detection
- CI example (GitHub Actions) to run validations on every push

> Owner: **Clara Ilari** · QA Engineer / Data & ETL · LinkedIn: https://www.linkedin.com/in/clara-ilari-96177120/

## Structure
```
manual-tests/      # Test plan, test strategy, sample test cases
api-tests/         # Postman collection & README
python/            # ETL validation scripts with Pandas & PyTest
sql/               # Reconciliation queries & data quality SQL
data/              # Small sample datasets (CSV)
.github/workflows/ # CI example for automated checks
```

## Quick Start (Python validations)
```bash
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r python/requirements.txt
pytest -q
python python/validate_etl.py --staging data/staging_orders.csv --warehouse data/warehouse_orders.csv
```

## What this demonstrates
- **Idempotent loading & lineage**: raw → staging → warehouse
- **Data quality gates**: non-null, PK uniqueness, referential integrity, value ranges
- **Business checks**: totals by day, deltas vs. prior day, pricing sanity
- **API tests**: contract & functional tests (Postman collection)
- **Automation**: CI pipeline to run validations on push

---

**Complex Testing Challenge (excerpt used in my CV)**  
"In a recent project, I was responsible for validating large-scale ETL pipelines where inconsistent data across multiple sources created high defect rates in production. I designed a hybrid approach combining SQL profiling, Tricentis Data Integrity, and Python automated scripts to detect anomalies before deployment. This improved defect detection coverage by 35%, reduced production incidents by 25%, and significantly increased trust in analytics outputs used by leadership for decision-making."


## Web UI Tests (Selenium + PyTest, POM)
See `web-tests/` for a minimal Page Object Model.  
Run:
```bash
pip install -r python/requirements.txt
pytest -q web-tests/tests/test_login.py --base-url https://example.com --browser chrome
```
