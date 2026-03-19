import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from datetime import datetime
import os
import allure


# ---------- ADD CLI OPTION (HEADLESS MODE) ----------
def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


# ---------- DRIVER FIXTURE ----------
@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")

    driver = get_driver(headless=headless)
    yield driver
    driver.quit()


# ---------- LOGIN FIXTURE ----------
@pytest.fixture
def logged_in_user(driver):
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    return driver


# ---------- SCREENSHOT + ALLURE ATTACHMENT ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/failure_{timestamp}.png"

            # Save screenshot
            driver.save_screenshot(screenshot_path)

            # Attach to Allure
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            print(f"Screenshot saved: {screenshot_path}")