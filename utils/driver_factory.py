from selenium import webdriver  # Import the main webdriver module from Selenium
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager for automatic ChromeDriver management
from selenium.webdriver.chrome.service import Service  # Import Service class for ChromeDriver service configuration

def get_driver():  # Function to create and return a configured Chrome WebDriver instance
    options = webdriver.ChromeOptions()  # Create ChromeOptions instance to configure browser behavior
    options.add_argument("--start-maximized")  # Add argument to start the browser in maximized window mode

    driver = webdriver.Chrome(  # Create Chrome WebDriver instance with specified configuration
        service=Service(ChromeDriverManager().install()),  # Use Service with auto-managed ChromeDriver from webdriver-manager
        options=options  # Apply the configured Chrome options
    )
    return driver  # Return the configured WebDriver instance for use in tests