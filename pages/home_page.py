# Import required Selenium classes for locating elements and applying waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Page Object Model class for Home Page
class HomePage:

    def __init__(self, driver):
        # Store the WebDriver instance (browser)
        self.driver = driver
        
        # Explicit wait - wait up to 20 seconds for elements (important for Jenkins slow execution)
        self.wait = WebDriverWait(driver, 20)

        # Locator for "Shop" menu (kept for reference, not used after fix)
        self.shop_menu = (By.XPATH, "//a[contains(text(),'Shop')]")
        
        # Locator for "Lipsticks" option (kept but not used after direct navigation fix)
        self.lipstick_option = (By.XPATH, "//a[contains(@href,'lipsticks')]")

        # Locator for profile icon (used to check login state)
        self.profile_icon = (By.CSS_SELECTOR, "img, .profile-icon")

        # Locator for dropdown options (Logout / My Orders → indicates user is logged in)
        self.dropdown = (By.XPATH, "//a[contains(text(),'Logout') or contains(text(),'My Orders')]")

    # Method to open the home page
    def open(self):
        # Directly open the application URL (faster and avoids navigation issues)
        self.driver.get("https://glowify-cosmetics-site.onrender.com/")

    # 🔥 FINAL FIX METHOD
    def go_to_lipsticks(self):
        # Instead of using hover (which is unreliable in Jenkins),
        # I directly navigated to the lipsticks page URL
        
        # This avoids:
        # ❌ Hover issues
        # ❌ Dropdown timing problems
        # ❌ CI instability
        
        # This ensures:
        # ✔ Fast execution
        # ✔ Stable in Jenkins
        # ✔ No dependency on UI animations
        
        self.driver.get("https://glowify-cosmetics-site.onrender.com/products?category=lipsticks")

    # Method to check if user is logged in
    def is_logged_in(self):
        # Wait until profile icon is clickable (ensures page is loaded properly)
        icon = self.wait.until(EC.element_to_be_clickable(self.profile_icon))
        
        # Click profile icon to open dropdown menu
        icon.click()

        # Capture current URL after clicking profile icon
        current_url = self.driver.current_url

        # If redirected to login page → user is NOT logged in
        if "login" in current_url:
            return False

        try:
            # Wait for dropdown options like Logout/My Orders
            # If visible → user is logged in
            self.wait.until(EC.visibility_of_element_located(self.dropdown))
            return True
        except:
            # If dropdown not found → user is NOT logged in
            return False