from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.name = (By.NAME, "name")
        self.email = (By.NAME, "email")
        self.password = (By.NAME, "password")
        self.register_btn = (By.XPATH, "//button[contains(text(),'Register')]")

    def register_user(self):
        self.wait.until(EC.visibility_of_element_located(self.name)).send_keys("Test User")

        # 🔥 unique email (important)
        unique_email = f"test{int(time.time())}@gmail.com"
        self.driver.find_element(*self.email).send_keys(unique_email)

        self.driver.find_element(*self.password).send_keys("Test@123")
        self.driver.find_element(*self.register_btn).click()