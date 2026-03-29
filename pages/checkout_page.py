from selenium.webdriver.common.by import By  # Import By class for defining element locators using various strategies like NAME, ID, CSS
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for implementing explicit waits in Selenium
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for defining wait conditions


class CheckoutPage:  # Page object class representing the checkout page functionality

    def __init__(self, driver):  # Constructor to initialize the CheckoutPage with a WebDriver instance
        self.driver = driver  # Store the WebDriver instance for browser interactions
        self.wait = WebDriverWait(driver, 20)  # Create WebDriverWait with 20-second timeout for explicit waits

        self.first_name = (By.NAME, "first_name")  # Define locator for first name input field using NAME attribute
        self.mobile = (By.NAME, "mobile")  # Define locator for mobile number input field using NAME attribute
        self.address = (By.NAME, "address")  # Define locator for address input field using NAME attribute
        self.city = (By.NAME, "city")  # Define locator for city input field using NAME attribute
        self.state = (By.NAME, "state")  # Define locator for state input field using NAME attribute
        self.pincode = (By.NAME, "pincode")  # Define locator for pincode input field using NAME attribute

        self.place_order = (By.ID, "placeOrderBtn")  # Define locator for place order button using ID attribute

        self.razorpay_frame = (By.CSS_SELECTOR, "iframe.razorpay-checkout-frame")  # Define locator for Razorpay payment iframe using CSS selector

    def fill_details(self):  # Method to fill in the checkout form with test data
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys("Test")  # Wait for first name field to be visible, then enter "Test"

        self.driver.find_element(*self.mobile).send_keys("9876543210")  # Find mobile field and enter test phone number
        self.driver.find_element(*self.address).send_keys("Chennai")  # Find address field and enter test address
        self.driver.find_element(*self.city).send_keys("Chennai")  # Find city field and enter test city
        self.driver.find_element(*self.state).send_keys("Tamil Nadu")  # Find state field and enter test state
        self.driver.find_element(*self.pincode).send_keys("600001")  # Find pincode field and enter test pincode

    def place_order_click(self):  # Method to click the place order button
        self.driver.find_element(*self.place_order).click()  # Find and click the place order button

    def verify_payment_popup(self):  # Method to verify and switch to the Razorpay payment popup iframe
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.razorpay_frame))  # Wait for Razorpay iframe to be available and switch to it