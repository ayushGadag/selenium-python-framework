from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, user, pwd):
        self.enter_text(self.username, user)
        self.enter_text(self.password, pwd)
        self.click(self.login_button)