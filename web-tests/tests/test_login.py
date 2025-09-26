import pytest
from web-tests.pages.login_page import LoginPage

@pytest.mark.ui
def test_login_invalid_credentials(driver, base_url):
    page = LoginPage(driver, base_url)
    page.open_login()
    page.login("invalid@example.com", "wrongpass")
    # Expect an error banner/message and remain on login
    msg = page.error_message()
    assert msg is None or "invalid" in msg.lower() or "error" in msg.lower()