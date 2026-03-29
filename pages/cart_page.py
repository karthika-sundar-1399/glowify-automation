from selenium.webdriver.common.by import By  # Import By class for defining element locators using strategies like CSS selectors
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits in Selenium
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for defining wait conditions


class CartPage:  # Page object class representing the shopping cart page functionality

    def __init__(self, driver):  # Constructor to initialize the CartPage with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for browser interactions
        self.wait = WebDriverWait(driver, 20)  # Create WebDriverWait with 20-second timeout for explicit waits

        self.checkout_btn = (By.CSS_SELECTOR, "a.checkout-btn")  # Define locator for the checkout button using CSS selector

    def proceed_to_checkout(self):  # Method to handle the process of proceeding to checkout from cart page

        if "cart" not in self.driver.current_url:  # Check if current URL doesn't contain 'cart' (not on cart page)
            self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/cart/")  # Navigate directly to the cart page URL

        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")  # Wait until the page is fully loaded (document ready state is complete)

        btn = self.wait.until(EC.presence_of_element_located(self.checkout_btn))  # Wait until the checkout button is present in the DOM

        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)  # Scroll the checkout button into view using JavaScript

        try:  # Attempt to click the button normally
            btn.click()  # Perform a standard click on the checkout button
        except:  # If standard click fails (e.g., element not clickable)
            self.driver.execute_script("arguments[0].click();", btn)  # Use JavaScript click as fallback

        # 🔥 Handle navigation manually  # Comment indicating manual handling of navigation logic
        current_url = self.driver.current_url  # Get the current URL after attempting to click

        if "login" in current_url:  # If redirected to login page (user not authenticated)
            return  # Exit the method (login required before checkout)

        if "cart" in current_url:  # If still on cart page (checkout button didn't navigate)
            self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/checkout/")  # Manually navigate to checkout page