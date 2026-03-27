# =====================================================
# CHECKOUT PAGE - Actions on the Checkout/Payment Page
# =====================================================
# This class represents the Checkout page where users enter delivery details
# It contains methods to fill in address info and complete payment

# Import tools from Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    # Constructor - Set up page elements
    def __init__(self, driver):
        # Store the browser driver
        self.driver = driver
        
        # Wait up to 20 seconds for elements to appear
        self.wait = WebDriverWait(driver, 20)

        # Find input fields for delivery/billing details
        self.first_name = (By.NAME, "first_name")  # First name input field
        self.mobile = (By.NAME, "mobile")  # Mobile number input field
        self.address = (By.NAME, "address")  # Address input field
        self.city = (By.NAME, "city")  # City input field
        self.state = (By.NAME, "state")  # State input field
        self.pincode = (By.NAME, "pincode")  # Postal code input field

        # Find the "Place Order" button that submits the form
        self.place_order = (By.ID, "placeOrderBtn")

        # Find the Razorpay payment popup iframe
        # Razorpay is the payment gateway used by Glowify
        # An iframe is like a separate mini-browser window inside the page
        self.razorpay_frame = (By.CSS_SELECTOR, "iframe.razorpay-checkout-frame")

    # Method to fill in delivery and billing details
    def fill_details(self):
        # STEP 1: Wait for the first name field to be visible, then type "Test"
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys("Test")

        # STEP 2: Fill in the mobile number
        # Using a dummy Indian phone number
        self.driver.find_element(*self.mobile).send_keys("9876543210")
        
        # STEP 3: Fill in the address
        self.driver.find_element(*self.address).send_keys("Chennai")
        
        # STEP 4: Fill in the city
        self.driver.find_element(*self.city).send_keys("Chennai")
        
        # STEP 5: Fill in the state
        self.driver.find_element(*self.state).send_keys("Tamil Nadu")
        
        # STEP 6: Fill in the postal code
        self.driver.find_element(*self.pincode).send_keys("600001")

    # Method to click the "Place Order" button
    def place_order_click(self):
        # Click the button to submit the order
        # This will usually open the payment gateway popup
        self.driver.find_element(*self.place_order).click()

    # Method to verify that the payment popup appears
    def verify_payment_popup(self):
        # Wait for the Razorpay payment iframe to become available
        # Then switch into that iframe (so we can interact with payment elements)
        # Without switching into the iframe, we cannot access its elements
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.razorpay_frame))