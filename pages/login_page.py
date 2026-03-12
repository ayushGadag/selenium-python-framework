from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:


    def __init__(self,driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button =(By.ID ,"login-button")

    def login(self, user, pwd):
         wait = WebDriverWait(self.driver,10)
         self.driver.find_element(*self.username).send_keys(user)
         self.driver.find_element(*self.password).send_keys(pwd)
         self.driver.find_element(*self.login_button).click()