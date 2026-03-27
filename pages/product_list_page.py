# Import required Selenium classes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Page Object Model for Product Listing Page
class ProductListPage:

    def __init__(self, driver):
        # Store driver instance
        self.driver = driver

        # Increased wait time (CI is slower than local)
        self.wait = WebDriverWait(driver, 30)

    def select_first_product(self):
        # 🔥 STEP 1: Wait for ALL anchor tags to load
        # Instead of relying on specific class (which may change),
        # I used generic locator to capture all links on page
        elements = self.wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        # 🔥 STEP 2: Loop through elements and find product link
        for el in elements:
            href = el.get_attribute("href")

            # Check if link belongs to a product page
            # (based on URL pattern containing 'product')
            if href and "product" in href:
                
                # 🔥 STEP 3: Scroll to element (important in Jenkins)
                # Sometimes element is not visible in viewport
                self.driver.execute_script("arguments[0].scrollIntoView();", el)

                # 🔥 STEP 4: Click the element
                el.click()

                # Stop after clicking first valid product
                break