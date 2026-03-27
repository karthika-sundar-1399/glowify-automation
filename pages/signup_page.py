# =====================================================
# SIGNUP PAGE - Actions We Can Do on the Sign Up Page
# =====================================================
# This class represents the Sign Up page of Glowify website
# It contains methods to register new users

# Import tools from Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Used to generate unique timestamps

class SignupPage:

    # Constructor - Set up page elements
    def __init__(self, driver):
        # Store the browser driver
        self.driver = driver
        
        # Wait up to 10 seconds for elements to appear
        self.wait = WebDriverWait(driver, 10)

        # Find the Name input field on the signup page
        self.name = (By.NAME, "name")
        
        # Find the Email input field on the signup page
        self.email = (By.NAME, "email")
        
        # Find the Password input field on the signup page
        self.password = (By.NAME, "password")
        
        # Find the Register button on the signup page
        self.register_btn = (By.XPATH, "//button[contains(text(),'Register')]")

    # Method to register a new user with test data
    def register_user(self):
        # STEP 1: Fill in the Name field
        # Wait for the name field to be visible, then type "Test User"
        self.wait.until(EC.visibility_of_element_located(self.name)).send_keys("Test User")

        # STEP 2: Fill in the Email field with a UNIQUE email
        # Why unique? Because each test run needs a different email
        # We use the current timestamp (seconds since 1970) to make it unique
        # Example: test1234567890@gmail.com
        unique_email = f"test{int(time.time())}@gmail.com"
        self.driver.find_element(*self.email).send_keys(unique_email)

        # STEP 3: Fill in the Password field
        # We use a test password: "Test@123"
        self.driver.find_element(*self.password).send_keys("Test@123")
        
        # STEP 4: Click the Register button to submit the form
        # This creates a new user account with the above details
        self.driver.find_element(*self.register_btn).click()