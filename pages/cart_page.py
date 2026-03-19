from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.checkout_btn = (By.CSS_SELECTOR, "a.checkout-btn")

    def proceed_to_checkout(self):

        if "cart" not in self.driver.current_url:
            self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/cart/")

        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        btn = self.wait.until(EC.presence_of_element_located(self.checkout_btn))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)

        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

        # 🔥 Handle navigation manually
        current_url = self.driver.current_url

        if "login" in current_url:
            return

        if "cart" in current_url:
            self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/checkout/")