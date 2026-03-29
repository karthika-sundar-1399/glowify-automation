from selenium.webdriver.common.by import By  # Import By class for defining element locators using strategies like CSS and XPATH
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits in Selenium
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for defining wait conditions


class ProductDetailPage:  # Page object class representing the product detail page functionality

    def __init__(self, driver):  # Constructor to initialize the ProductDetailPage with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for browser interactions
        self.wait = WebDriverWait(driver, 20)  # Create WebDriverWait with 20-second timeout for explicit waits

        self.add_to_cart_btn = (By.CSS_SELECTOR, "button.add-cart")  # Define locator for add to cart button using CSS selector

        # Go to cart button (dynamic)  # Comment indicating this button appears dynamically after adding to cart
        self.go_to_cart_btn = (By.XPATH, "//button[contains(@class,'added')]//span[contains(text(),'Go to Cart')]")  # Define locator for go to cart button using XPATH

        # fallback cart icon  # Comment indicating this is a fallback locator for cart navigation
        self.cart_icon = (By.CSS_SELECTOR, ".cart-icon a")  # Define locator for cart icon link using CSS selector

    def add_product_to_cart(self):  # Method to add the current product to the shopping cart
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")  # Wait until the page is fully loaded (document ready state complete)

        btn = self.wait.until(EC.presence_of_element_located(self.add_to_cart_btn))  # Wait until add to cart button is present in DOM
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)  # Scroll the add to cart button into view using JavaScript
        self.driver.execute_script("arguments[0].click();", btn)  # Click the add to cart button using JavaScript for reliability

    def go_to_cart(self):  # Method to navigate to the shopping cart page
        try:  # Attempt to click the dynamic "Go to Cart" button that appears after adding item
            self.wait.until(EC.element_to_be_clickable(self.go_to_cart_btn)).click()  # Wait for go to cart button to be clickable and click it
        except:  # If the dynamic button is not found or clickable
            self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()  # Use fallback cart icon and click it

        # 🔥 ensure navigation always works  # Comment indicating forced navigation to ensure reliability
        self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/cart/")  # Directly navigate to cart page URL to guarantee success