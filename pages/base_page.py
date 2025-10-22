import logging
from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from utils.config import Config
from utils.wait_helper import WaitHelper

import allure



logger = logging.getLogger(__name__)

class BasePage:
    """Base class that provides common methods for all page objects."""
    
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait_helper = WaitHelper()
        
    
    #----------------------------------- NAVIGATION METHODS -----------------------------------#
    def navigate_to_url(self, url: str) -> str:
        with allure.step(f"Navigating to URL: {url}"):
            logger.info(f"Navigating to URL: {url}")
            self.driver.get(url)
            
    def get_current_url(self) -> str:
        return self.driver.current_url
            
    def get_page_title(self) -> str:
        return self.driver.title

    #----------------------------------- ELEMENT METHODS -----------------------------------#
    
    def find_element(self, locator):
        """Method for finding a single element in the page. """
        
        try:
            element = self.wait_helper.wait_for_element_visible(self.driver, locator)
            return element
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Element_not_found",
                          attachment_type=allure.attachment_type.PNG)
            raise NoSuchElementException(f"Element with locator {locator} not found on the page.")
        
        
    def find_elements(self, locator):
        """Method for finding a multiple elements in the page. """
        return self.driver.find_elements(*locator)
    
    def click(self, locator, element_name="element"):
        with allure.step(f"Clicking on : {element_name} with locator: {locator}"):
            element = self.wait_helper.wait_element_clickable(self.driver, locator)
            element.click()
            
    def enter_text(self, locator, text, element_name="field"):
        with allure.step(f"Entering : '{text}' into : {element_name} with locator: {locator}"):
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            
    def get_element_text(self, locator) -> str:
            element = self.find_element(locator)
            return element.text
        
    def get_attribute(self, locator, attribute_name) -> Any:
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)
    
    #----------------------------------- Element State -----------------------------------#
    
    def is_element_visible(self, locator, timeout=Config.EXPLICIT_WAIT):
        try:
            self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            return True
        except TimeoutException:
            return False
        
    def wait_for_element_to_disappear(self, locator, timeout=Config.EXPLICIT_WAIT) -> None:
        """Wait for an element to disappear from the page, like (spinner/loading)..."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            pass 
        
    def take_screenshots(self, name="screenshots") -> None:
        """Take screenshots of the current page."""
        
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name,
                        attachment_type=allure.attachment_type.PNG)
        
    #----------------------------------- Windows Management -----------------------------------#
    
    def maximize_window(self) -> None:
        self.driver.maximize_window()
        
    def refresh_page(self) -> None:
        with allure.step("Refreshing the current page"):
            self.driver.refresh()