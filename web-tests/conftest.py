import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def _chrome(headless: bool):
    opts = ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1366,768")
    return webdriver.Chrome(options=opts)

def _firefox(headless: bool):
    opts = FirefoxOptions()
    if headless:
        opts.add_argument("-headless")
    return webdriver.Firefox(options=opts)

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="https://example.com")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--headless", action="store_true", default=True)

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url")

@pytest.fixture
def driver(pytestconfig):
    browser = pytestconfig.getoption("--browser")
    headless = pytestconfig.getoption("--headless")
    if browser == "chrome":
        d = _chrome(headless)
    else:
        d = _firefox(headless)
    yield d
    d.quit()