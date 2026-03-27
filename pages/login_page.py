# =====================================================
# LOGIN PAGE - Actions We Can Do on the Login Page
# =====================================================
# This class represents the Login page of Glowify website
# It contains methods to interact with login page elements

# Import tools from Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    # Constructor - Set up page elements
    def __init__(self, driver):
        # Store the browser driver
        self.driver = driver
        
        # Wait up to 20 seconds for elements to appear
        self.wait = WebDriverWait(driver, 20)

        # Find the "Sign Up" link on the login page using XPath
        # This is a reliable way to find the link that takes you to signup
        self.signup_link = (By.XPATH, "//a[contains(@href,'signup')]")

        # Find the Email input field on the login page
        # This field is how we identify the login page (it's a page indicator)
        self.email_field = (By.NAME, "email")

    # Method to navigate to the Sign Up page
    def go_to_signup(self):
        # STEP 1: Wait until the login page is fully loaded
        # We check this by waiting for the email field to appear
        self.wait.until(EC.presence_of_element_located(self.email_field))

        # STEP 2: Double-check that we are on the login page
        # by making sure the URL contains "login"
        self.wait.until(lambda d: "login" in d.current_url)

        # STEP 3: Find and prepare the Sign Up button
        # Wait for it to be clickable before clicking
        btn = self.wait.until(EC.element_to_be_clickable(self.signup_link))

        # STEP 4: Click the Sign Up button
        # We have two ways - first try normal click
        try:
            btn.click()
        except:
            # If normal click fails (sometimes browsers block it), use JavaScript click
            self.driver.execute_script("arguments[0].click();", btn)