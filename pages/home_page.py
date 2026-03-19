from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.shop_menu = (By.XPATH, "//a[contains(text(),'Shop')]")
        self.lipstick_option = (By.XPATH, "//a[contains(@href,'lipsticks')]")

        self.profile_icon = (By.CSS_SELECTOR, "img, .profile-icon")

        self.dropdown = (By.XPATH, "//a[contains(text(),'Logout') or contains(text(),'My Orders')]")

    def open(self):
        self.driver.get("https://glowify-cosmetics-site.onrender.com/")

    def go_to_lipsticks(self):

        actions = ActionChains(self.driver)

        # 🔥 hover on Shop menu
        shop = self.wait.until(EC.visibility_of_element_located(self.shop_menu))
        actions.move_to_element(shop).perform()

        # 🔥 wait for dropdown item
        lipstick = self.wait.until(EC.visibility_of_element_located(self.lipstick_option))

        # 🔥 click lipstick
        lipstick.click()

    def is_logged_in(self):

        icon = self.wait.until(EC.element_to_be_clickable(self.profile_icon))
        icon.click()

        current_url = self.driver.current_url

        if "login" in current_url:
            return False

        try:
            self.wait.until(EC.visibility_of_element_located(self.dropdown))
            return True
        except:
            return False