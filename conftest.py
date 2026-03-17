import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from datetime import datetime
import os


# ---------- DRIVER FIXTURE ----------
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# ---------- LOGIN FIXTURE ----------
@pytest.fixture
def logged_in_user(driver):
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    return driver


# ---------- SCREENSHOT ON FAILURE ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    # Run only if test failed
    if rep.when == "call" and rep.failed:

        driver = item.funcargs["driver"]

        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"screenshots/failure_{timestamp}.png"

        driver.save_screenshot(screenshot_name)

        print(f"Screenshot saved: {screenshot_name}")