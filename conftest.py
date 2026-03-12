import pytest
from utils.driver_factory import get_driver
from datetime import datetime
import os


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    # check if test failed
    if rep.when == "call" and rep.failed:

        # get driver instance from test
        driver = item.funcargs["driver"]

        # create screenshots folder if not exists
        os.makedirs("screenshots", exist_ok=True)

        # create timestamp for unique screenshot name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_name = f"screenshots/failure_{timestamp}.png"

        # save screenshot
        driver.save_screenshot(screenshot_name)

        print(f"Screenshot saved: {screenshot_name}")