import pytest
import os
from utils.driver_factory import get_driver as driver_init

@pytest.fixture
def get_driver():
    driver = driver_init()
    yield driver
    driver.quit()


# Hook for screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("get_driver")

        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            file_name = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(file_name)

            import allure
            allure.attach.file(file_name, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)