from selenium.webdriver.common.by import By  # Import By class for locating web elements using different strategies like ID, CSS, XPath
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions module for defining wait conditions

class BasePage:  # Base class for all page objects, providing common Selenium interaction methods

    def __init__(self, driver):  # Constructor method to initialize the page object with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for use in page methods
        self.wait = WebDriverWait(driver, 10)  # Create a WebDriverWait instance with a 10-second timeout for explicit waits

    def click(self, locator):  # Method to click on a web element identified by the given locator
        self.wait.until(EC.element_to_be_clickable(locator)).click()  # Wait until the element is clickable, then perform the click action

    def send_keys(self, locator, text):  # Method to send text input to a web element identified by the given locator
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)  # Wait until the element is visible, then send the specified text

    def get_text(self, locator):  # Method to retrieve the text content of a web element identified by the given locator
        return self.wait.until(EC.visibility_of_element_located(locator)).text  # Wait until the element is visible, then return its text content

    def is_visible(self, locator):  # Method to check if a web element identified by the given locator is visible on the page
        return self.wait.until(EC.visibility_of_element_located(locator))  # Wait until the element is visible and return the element (truthy if found)