from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # 🔥 better locator (more reliable)
        self.signup_link = (By.XPATH, "//a[contains(@href,'signup')]")

        # 🔥 login page indicator
        self.email_field = (By.NAME, "email")

    def go_to_signup(self):

        # 🔥 WAIT until login page fully loads
        self.wait.until(EC.presence_of_element_located(self.email_field))

        # 🔥 ensure correct page
        self.wait.until(lambda d: "login" in d.current_url)

        # 🔥 now click signup
        btn = self.wait.until(EC.element_to_be_clickable(self.signup_link))

        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)