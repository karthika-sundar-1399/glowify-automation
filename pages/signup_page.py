from selenium.webdriver.common.by import By  # Import By class for defining element locators using strategies like NAME and XPATH
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits in Selenium
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for defining wait conditions
import time  # Import time module for generating unique timestamps


class SignupPage:  # Page object class representing the signup/registration page functionality

    def __init__(self, driver):  # Constructor to initialize the SignupPage with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for browser interactions
        self.wait = WebDriverWait(driver, 10)  # Create WebDriverWait with 10-second timeout for explicit waits

        self.name = (By.NAME, "name")  # Define locator for name input field using NAME attribute
        self.email = (By.NAME, "email")  # Define locator for email input field using NAME attribute
        self.password = (By.NAME, "password")  # Define locator for password input field using NAME attribute
        self.register_btn = (By.XPATH, "//button[contains(text(),'Register')]")  # Define locator for register button using XPATH

    def register_user(self):  # Method to fill out and submit the user registration form
        self.wait.until(EC.visibility_of_element_located(self.name)).send_keys("Test User")  # Wait for name field to be visible, then enter test name

        # 🔥 unique email (important)  # Comment indicating the importance of unique email generation
        unique_email = f"test{int(time.time())}@gmail.com"  # Generate unique email using current timestamp to avoid duplicates
        self.driver.find_element(*self.email).send_keys(unique_email)  # Find email field and enter the unique test email

        self.driver.find_element(*self.password).send_keys("Test@123")  # Find password field and enter test password
        self.driver.find_element(*self.register_btn).click()  # Find and click the register button to submit the form