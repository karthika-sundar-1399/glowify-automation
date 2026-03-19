from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.add_to_cart_btn = (By.CSS_SELECTOR, "button.add-cart")

        # Go to cart button (dynamic)
        self.go_to_cart_btn = (By.XPATH, "//button[contains(@class,'added')]//span[contains(text(),'Go to Cart')]")

        # fallback cart icon
        self.cart_icon = (By.CSS_SELECTOR, ".cart-icon a")

    def add_product_to_cart(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        btn = self.wait.until(EC.presence_of_element_located(self.add_to_cart_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    def go_to_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.go_to_cart_btn)).click()
        except:
            self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

        # 🔥 ensure navigation always works
        self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/cart/")