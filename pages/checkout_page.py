from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.first_name = (By.NAME, "first_name")
        self.mobile = (By.NAME, "mobile")
        self.address = (By.NAME, "address")
        self.city = (By.NAME, "city")
        self.state = (By.NAME, "state")
        self.pincode = (By.NAME, "pincode")

        self.place_order = (By.ID, "placeOrderBtn")

        self.razorpay_frame = (By.CSS_SELECTOR, "iframe.razorpay-checkout-frame")

    def fill_details(self):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys("Test")

        self.driver.find_element(*self.mobile).send_keys("9876543210")
        self.driver.find_element(*self.address).send_keys("Chennai")
        self.driver.find_element(*self.city).send_keys("Chennai")
        self.driver.find_element(*self.state).send_keys("Tamil Nadu")
        self.driver.find_element(*self.pincode).send_keys("600001")

    def place_order_click(self):
        self.driver.find_element(*self.place_order).click()

    def verify_payment_popup(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.razorpay_frame))