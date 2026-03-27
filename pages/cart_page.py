# =====================================================
# CART PAGE - Actions on the Shopping Cart Page
# =====================================================
# This class represents the Shopping Cart page
# It contains methods to proceed to checkout

# Import tools from Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    # Constructor - Set up page elements
    def __init__(self, driver):
        # Store the browser driver
        self.driver = driver
        
        # Wait up to 20 seconds for elements to appear
        self.wait = WebDriverWait(driver, 20)

        # Find the "Checkout" button on the cart page
        # CSS_SELECTOR "a.checkout-btn" means: find a link with class "checkout-btn"
        self.checkout_btn = (By.CSS_SELECTOR, "a.checkout-btn")

    # Method to click the Checkout button and proceed to payment
    def proceed_to_checkout(self):
        # STEP 1: Make sure we are on the cart page
        # If "cart" is not in the URL, navigate to it
        if "cart" not in self.driver.current_url:
            self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/cart/")

        # STEP 2: Wait for the page to fully load
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # STEP 3: Find the Checkout button
        btn = self.wait.until(EC.presence_of_element_located(self.checkout_btn))

        # STEP 4: Scroll the button into view (it might be below the visible area)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)

        # STEP 5: Click the button (try normal click first, then JavaScript click if needed)
        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

        # STEP 6: Handle different scenarios after clicking checkout
        # Get the current URL to see where we ended up
        current_url = self.driver.current_url

        # If checkout button took us to login page, stop here
        # (The test will then register a new user)
        if "login" in current_url:
            return

        # If we are still on the cart page, navigate to checkout manually
        # Sometimes the click doesn't work as expected
        if "cart" in current_url:
            self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/checkout/")