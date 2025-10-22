from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.config import Config

class WaitHelper:
    """Class for handling timeouts and waits"""
    
    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=Config.EXPLICIT_WAIT):
        """Wait for an element to be visible on the page."""
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    @staticmethod
    def wait_element_clickable(driver, locator, timeout=Config.EXPLICIT_WAIT):
        """Wait for an element to be clickable on the page."""
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    @staticmethod
    def wait_for_element_presence(driver, locator, timeout=Config.EXPLICIT_WAIT):
        """Wait for an element to be present in the DOM."""
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    @staticmethod
    def wait_for_element_text_visible(driver, locator, text, timeout=Config.EXPLICIT_WAIT):
        """Wait for an element to contain specific text."""
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.text_to_be_present_in_element(locator, text))