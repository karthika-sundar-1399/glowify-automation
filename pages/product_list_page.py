# =====================================================
# PRODUCT LIST PAGE - Actions on the Products List Page
# =====================================================
# This class represents the Product List page (e.g., Lipsticks category)
# It contains methods to interact with products shown in a list/grid

# Import tools from Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListPage:

    # Constructor - Set up page elements
    def __init__(self, driver):
        # Store the browser driver
        self.driver = driver
        
        # Wait up to 10 seconds for elements to appear
        self.wait = WebDriverWait(driver, 10)

        # Find the first product in the product list
        # CSS_SELECTOR ".product-card a" means: find a link (<a>) inside a div with class "product-card"
        self.first_product = (By.CSS_SELECTOR, ".product-card a")

    # Method to click on the first product in the list
    def select_first_product(self):
        # Wait for the first product link to be clickable, then click it
        # This takes us to the product detail page
        self.wait.until(EC.element_to_be_clickable(self.first_product)).click()