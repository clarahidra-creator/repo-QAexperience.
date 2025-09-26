
# Web UI Tests – Selenium + PyTest (POM)

This module demonstrates a minimal **Page Object Model** setup with Selenium + PyTest for e‑commerce flows.

## Structure
```
web-tests/
  conftest.py          # Browser setup, CLI options
  pages/
    base_page.py
    login_page.py
  tests/
    test_login.py
```

## Usage (example)
```bash
pip install -r python/requirements.txt
pytest -q web-tests/tests/test_login.py --base-url https://example.com --browser chrome
```
