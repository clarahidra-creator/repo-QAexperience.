from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "input[type='email'], #email")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password'], #password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit'], .btn-login, #login")
    ERROR = (By.CSS_SELECTOR, ".error, .alert-danger")

    def open_login(self):
        self.open("/login")

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def error_message(self):
        try:
            return self.text_of(self.ERROR)
        except Exception:
            return None