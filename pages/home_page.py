from selenium.webdriver.common.by import By  # Import By class for defining element locators using strategies like XPATH and CSS
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits in Selenium
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for defining wait conditions
from selenium.webdriver.common.action_chains import ActionChains  # Import ActionChains for performing complex user interactions like hovering

class HomePage:  # Page object class representing the home page functionality

    def __init__(self, driver):  # Constructor to initialize the HomePage with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for browser interactions
        self.wait = WebDriverWait(driver, 20)  # Create WebDriverWait with 20-second timeout for explicit waits

        self.shop_menu = (By.XPATH, "//a[contains(text(),'Shop')]")  # Define locator for Shop menu link using XPATH
        self.lipstick_option = (By.XPATH, "//a[contains(@href,'lipsticks')]")  # Define locator for lipsticks option in dropdown using XPATH

        self.profile_icon = (By.CSS_SELECTOR, "img, .profile-icon")  # Define locator for profile icon using CSS selector

        self.dropdown = (By.XPATH, "//a[contains(text(),'Logout') or contains(text(),'My Orders')]")  # Define locator for logout/orders dropdown items using XPATH

    def open(self):  # Method to navigate to the home page URL
        self.driver.get("https://glowify-cosmetics-site.onrender.com/")  # Load the Glowify cosmetics website home page

    def go_to_lipsticks(self):  # Method to navigate to the lipsticks section via dropdown menu

        actions = ActionChains(self.driver)  # Create ActionChains instance for mouse actions

        # 🔥 hover on Shop menu  # Comment indicating hover action on Shop menu
        shop = self.wait.until(EC.visibility_of_element_located(self.shop_menu))  # Wait for Shop menu to be visible
        actions.move_to_element(shop).perform()  # Hover over the Shop menu to reveal dropdown

        # 🔥 wait for dropdown item  # Comment indicating wait for dropdown item to appear
        lipstick = self.wait.until(EC.visibility_of_element_located(self.lipstick_option))  # Wait for lipsticks option to be visible in dropdown

        # 🔥 click lipstick  # Comment indicating click action on lipstick option
        lipstick.click()  # Click on the lipsticks option to navigate to lipsticks page

    def is_logged_in(self):  # Method to check if user is currently logged in

        icon = self.wait.until(EC.element_to_be_clickable(self.profile_icon))  # Wait for profile icon to be clickable
        icon.click()  # Click on the profile icon to open user menu

        current_url = self.driver.current_url  # Get the current URL after clicking profile icon

        if "login" in current_url:  # If redirected to login page, user is not logged in
            return False  # Return false indicating user is not authenticated

        try:  # Attempt to find logout/orders dropdown items
            self.wait.until(EC.visibility_of_element_located(self.dropdown))  # Wait for dropdown menu items to be visible
            return True  # If dropdown items found, user is logged in
        except:  # If dropdown items not found (timeout exception)
            return False  # Return false indicating user is not logged in