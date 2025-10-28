
import sys
import os

# ensure Automation_Test is on sys.path so "pages", "utils" imports work reliably
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pytest
from utils.driver_factory import create_driver
from utils.screenshot_helper import take_screenshot

@pytest.fixture(scope="function")
def driver():
    driver = create_driver(headless=False)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, item.name)
