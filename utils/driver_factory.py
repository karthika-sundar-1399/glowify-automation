# =====================================================
# DRIVER FACTORY - Creates the WebDriver for Testing
# =====================================================
# This file is responsible for setting up and creating a web browser driver
# Think of it as "turning on" the browser before we start testing

# Import required libraries for Selenium
from selenium import webdriver  # This is the main library for browser automation
from webdriver_manager.chrome import ChromeDriverManager  # Automatically downloads Chrome driver
from selenium.webdriver.chrome.service import Service  # Configures how Chrome browser will run

# Function that creates and returns a web driver (browser)
def get_driver():
    # Create Chrome browser options/settings
    options = webdriver.ChromeOptions()
    
    # This argument makes the browser window open at maximum size
    # So the website takes full screen - helps in testing all elements
    options.add_argument("--start-maximized")

    # Actually create the Chrome browser with our settings
    # ChromeDriverManager() automatically downloads the correct Chrome driver
    # Service() tells Chrome how to run with these settings
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    # Return the driver so we can use it in our tests
    return driver