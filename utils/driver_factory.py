from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utils.config import Config

class DriverFactory:
    """Factory class responsible for creating WebDriver instances based on the given configuration."""
    
    @staticmethod
    def create_driver():
        browser = Config.BROWSER.lower()
        
        if browser == 'chrome':
            driver = DriverFactory._create_driver_chrome()
        elif browser == 'firefox':
            driver = DriverFactory._create_driver_firefox()
        elif browser == 'edge':
            driver = DriverFactory._create_driver_edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        return driver
    
    @staticmethod
    def _create_driver_chrome():
        """Create a Chrome WebDriver instance."""
        
        options = ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless=new")
            #options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        # Always create the Chrome driver; options may include headless args when configured
        driver = webdriver.Chrome(options=options)
        return driver
    
    @staticmethod
    def _create_driver_firefox():
        """Create a Firefox WebDriver instance."""
        
        options = FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        
        driver = webdriver.Firefox(options=options)
        return driver
    
    @staticmethod
    def _create_driver_edge():
        """Create an Edge WebDriver instance."""
        
        options = EdgeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        
        driver = webdriver.Edge(options=options)
        return driver
    
    @staticmethod
    def quit_driver(driver):
        if driver:
            driver.quit()
            
    
            