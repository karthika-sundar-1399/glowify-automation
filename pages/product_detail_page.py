# =====================================================
# PRODUCT DETAIL PAGE - Actions on a Single Product Page
# =====================================================
# This class represents the Product Detail page (when you click on a product)
# It contains methods to add products to cart and navigate to the cart

# Import tools from Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailPage:

    # Constructor - Set up page elements
    def __init__(self, driver):
        # Store the browser driver
        self.driver = driver
        
        # Wait up to 20 seconds for elements to appear (longer timeout for product load)
        self.wait = WebDriverWait(driver, 20)

        # Find the "Add to Cart" button on the product page
        # CSS_SELECTOR "button.add-cart" means: find a button with class "add-cart"
        self.add_to_cart_btn = (By.CSS_SELECTOR, "button.add-cart")

        # Find the "Go to Cart" button that appears AFTER adding product to cart
        # This button is dynamic (appears only after clicking "Add to Cart")
        self.go_to_cart_btn = (By.XPATH, "//button[contains(@class,'added')]//span[contains(text(),'Go to Cart')]")

        # Find the cart icon as a backup way to go to cart
        # If "Go to Cart" button doesn't work, we can click the cart icon instead
        self.cart_icon = (By.CSS_SELECTOR, ".cart-icon a")

    # Method to add the current product to the shopping cart
    def add_product_to_cart(self):
        # STEP 1: Wait for the page to fully load
        # "document.readyState == complete" means all resources are loaded
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # STEP 2: Find the "Add to Cart" button
        btn = self.wait.until(EC.presence_of_element_located(self.add_to_cart_btn))
        
        # STEP 3: Scroll the button into view
        # Sometimes the button is below the visible area, so we scroll to it
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        
        # STEP 4: Click the button using JavaScript
        # JavaScript click is more reliable than regular Selenium click
        self.driver.execute_script("arguments[0].click();", btn)

    # Method to navigate to the shopping cart
    def go_to_cart(self):
        # Try to click the "Go to Cart" button (which appears after adding product)
        try:
            self.wait.until(EC.element_to_be_clickable(self.go_to_cart_btn)).click()
        except:
            # If "Go to Cart" button doesn't work, click the cart icon instead
            self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

        # Make sure we navigate to the cart URL as a backup
        # Sometimes clicks don't work properly, so we navigate directly
        self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/cart/")