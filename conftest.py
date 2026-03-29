import pytest  # Import pytest framework for test fixtures and hooks
import os  # Import os module for file system operations like creating directories
from utils.driver_factory import get_driver as driver_init  # Import the WebDriver factory function with alias

@pytest.fixture  # Decorator to mark this function as a pytest fixture for reusable test setup
def get_driver():  # Fixture function to provide WebDriver instance to test functions
    driver = driver_init()  # Initialize and create a Chrome WebDriver instance using the factory function
    yield driver  # Yield the driver to the test function for use during test execution
    driver.quit()  # Clean up and close the driver after test execution (teardown)


# Hook for screenshot on failure  # Comment indicating automatic screenshot capture on test failure
@pytest.hookimpl(hookwrapper=True)  # Decorator to implement pytest hook with wrapper capability
def pytest_runtest_makereport(item):  # Hook function that runs after each test to generate test report
    outcome = yield  # Yield control to execute the test and capture the outcome
    report = outcome.get_result()  # Get the test execution result/report object

    if report.when == "call" and report.failed:  # Check if test failed during the call phase (not setup/teardown)
        driver = item.funcargs.get("get_driver")  # Retrieve the WebDriver instance from test function arguments

        if driver:  # Verify that driver instance exists before attempting to capture screenshot
            os.makedirs("reports/screenshots", exist_ok=True)  # Create screenshots directory if it doesn't exist (exist_ok prevents error if already exists)
            file_name = f"reports/screenshots/{item.name}.png"  # Generate screenshot file path using test name
            driver.save_screenshot(file_name)  # Capture and save browser screenshot to the specified file path

            import allure  # Import allure reporting module for test report enrichment
            allure.attach.file(file_name, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)  # Attach the screenshot to allure test report with PNG type