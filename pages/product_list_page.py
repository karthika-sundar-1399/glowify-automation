from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductListPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.first_product = (By.CSS_SELECTOR, ".product-card a")

    def select_first_product(self):
        self.wait.until(EC.element_to_be_clickable(self.first_product)).click()