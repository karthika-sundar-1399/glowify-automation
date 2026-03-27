# =====================================================
# CONFTEST.PY - Pytest Configuration and Fixtures
# =====================================================
# This file is automatically loaded by Pytest before running tests
# It contains setup/teardown code and fixtures shared across all tests
# A "fixture" is a reusable piece of test setup code

# Import required libraries
import pytest  # The testing framework we're using
import os  # For directory/file operations
from utils.driver_factory import get_driver as driver_init  # Import the browser driver factory

# ==================== FIXTURE: get_driver ====================
# A pytest fixture that provides a web driver for each test
# The @pytest.fixture decorator tells Pytest this is a fixture
@pytest.fixture
def get_driver():
    # SETUP: Create a new browser driver before each test
    driver = driver_init()
    
    # 'yield' means: run the test with this driver, then come back here when test finishes
    yield driver
    
    # TEARDOWN: Close the browser after the test completes
    # This is important to clean up and avoid leaving browser windows open
    driver.quit()


# ==================== HOOK: Auto Screenshot on Test Failure ====================
# A pytest hook that runs after each test to check if it failed
# If a test fails, this code captures a screenshot for debugging
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # 'yield' lets the test run first, then we check the result
    outcome = yield
    
    # Get the test result (passed or failed)
    report = outcome.get_result()

    # Check if this is a test failure (not setup/teardown failure)
    # 'report.when' tells us at which phase the failure happened
    # "call" means the actual test code failed
    if report.when == "call" and report.failed:
        # Try to get the driver used in this test
        driver = item.funcargs.get("get_driver")

        # Only take screenshot if driver is available
        if driver:
            # Create the screenshots folder if it doesn't exist
            # exist_ok=True means: don't error if folder already exists
            os.makedirs("reports/screenshots", exist_ok=True)
            
            # Create a filename for the screenshot
            # Using the test name: like "test_full_user_journey.png"
            file_name = f"reports/screenshots/{item.name}.png"
            
            # Take a screenshot of the failed test and save it
            driver.save_screenshot(file_name)

            # Attach the screenshot to the Allure report
            # Allure is a report generation tool that shows test results nicely
            import allure
            allure.attach.file(file_name, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)