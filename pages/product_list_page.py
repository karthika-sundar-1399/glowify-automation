from selenium.webdriver.common.by import By  # Import By class for defining element locators using strategies like CSS selectors
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits in Selenium
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for defining wait conditions


class ProductListPage:  # Page object class representing the product list page functionality

    def __init__(self, driver):  # Constructor to initialize the ProductListPage with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for browser interactions
        self.wait = WebDriverWait(driver, 10)  # Create WebDriverWait with 10-second timeout for explicit waits

        self.first_product = (By.CSS_SELECTOR, ".product-card a")  # Define locator for the first product card link using CSS selector

    def select_first_product(self):  # Method to select and click on the first product in the list
        self.wait.until(EC.element_to_be_clickable(self.first_product)).click()  # Wait until the first product link is clickable, then click it
