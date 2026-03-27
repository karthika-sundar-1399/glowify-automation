# =====================================================
# BASE PAGE - Parent Class for All Page Objects
# =====================================================
# This is a "Parent" or "Template" class for all pages in the website
# It contains common actions that every page needs (like clicking, typing, reading text)
# Other page classes inherit from this, so they can reuse these methods

# Import tools from Selenium for browser automation
from selenium.webdriver.common.by import By  # Used to find elements on the page (by ID, class, xpath, etc)
from selenium.webdriver.support.ui import WebDriverWait  # Waits for elements to be ready before acting
from selenium.webdriver.support import expected_conditions as EC  # Checks if elements are in the right state

# Define the BasePage class - the parent of all page classes
class BasePage:

    # Constructor method - runs when we create a new page object
    def __init__(self, driver):
        # Store the driver (browser) so we can control it
        self.driver = driver
        
        # Create a WebDriverWait object that will wait UP TO 10 seconds for elements to appear
        # This prevents tests from failing just because a page is slow to load
        self.wait = WebDriverWait(driver, 10)

    # Method to click on elements
    # locator: a tuple like (By.ID, "button_id") that identifies the element
    def click(self, locator):
        # Wait for the element to be clickable, then click it
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Method to type text into input fields
    # locator: identifies the input field on the page
    # text: the text we want to type
    def send_keys(self, locator, text):
        # Wait for the element to be visible, then type the text
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Method to read text from an element on the page
    # locator: identifies the element containing text
    def get_text(self, locator):
        # Wait for element to be visible, then return its text content
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    # Method to check if an element is visible on the page
    # locator: identifies which element to check
    def is_visible(self, locator):
        # Wait for element to be visible and return it if found
        return self.wait.until(EC.visibility_of_element_located(locator))