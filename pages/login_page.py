from selenium.webdriver.common.by import By  # Import By class for defining element locators using strategies like XPATH and NAME
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits in Selenium
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for defining wait conditions


class LoginPage:  # Page object class representing the login page functionality

    def __init__(self, driver):  # Constructor to initialize the LoginPage with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for browser interactions
        self.wait = WebDriverWait(driver, 20)  # Create WebDriverWait with 20-second timeout for explicit waits

        # 🔥 better locator (more reliable)  # Comment indicating improved locator strategy for signup link
        self.signup_link = (By.XPATH, "//a[contains(@href,'signup')]")  # Define locator for signup link using XPATH with href attribute

        # 🔥 login page indicator  # Comment indicating this element serves as a page load indicator
        self.email_field = (By.NAME, "email")  # Define locator for email input field using NAME attribute

    def go_to_signup(self):  # Method to navigate from login page to signup page

        # 🔥 WAIT until login page fully loads  # Comment indicating wait for complete page load
        self.wait.until(EC.presence_of_element_located(self.email_field))  # Wait until email field is present in DOM (page loaded)

        # 🔥 ensure correct page  # Comment indicating verification of being on correct page
        self.wait.until(lambda d: "login" in d.current_url)  # Wait until URL contains 'login' to confirm we're on login page

        # 🔥 now click signup  # Comment indicating the signup link click action
        btn = self.wait.until(EC.element_to_be_clickable(self.signup_link))  # Wait until signup link is clickable

        try:  # Attempt standard click on signup button
            btn.click()  # Perform standard click on the signup link
        except:  # If standard click fails
            self.driver.execute_script("arguments[0].click();", btn)  # Use JavaScript click as fallback method