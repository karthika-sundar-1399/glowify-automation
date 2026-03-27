from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # increased wait

        # more stable locator (adjust if needed)
        self.first_product = (By.CSS_SELECTOR, ".product-card a")

    def select_first_product(self):
        # wait until at least one product is visible
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.first_product)
        )

        # click first product safely
        products[0].click()