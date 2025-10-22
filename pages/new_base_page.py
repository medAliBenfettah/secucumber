from typing import Tuple, Optional, Any
import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By

import allure

from utils.wait_helper import WaitHelper
from utils.config import Config

logger = logging.getLogger(__name__)


Locator = Tuple[By, str]


class ElementNotFoundError(RuntimeError):
    pass


class BasePage:
    """BasePage provides common browser/page operations for Page Objects.

    Usage:
      page = BasePage(driver)
      page.navigate_to_url("https://example.com")

    Design decisions:
    - Accepts locators as (By.METHOD, "value") tuples everywhere.
    - Uses WaitHelper for explicit waits; falls back to WebDriverWait where needed.
    - Adds logging and Allure steps/attachments to help debugging.
    """

    def __init__(self, driver: WebDriver, wait_helper: Optional[WaitHelper] = None):
        self.driver = driver
        self.wait_helper = wait_helper or WaitHelper()

    # ----------------------- Navigation -----------------------
    def navigate_to_url(self, url: str) -> None:
        with allure.step(f"Navigate to URL: {url}"):
            logger.info("Navigating to URL: %s", url)
            self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self) -> str:
        return self.driver.title

    # ----------------------- Element queries -----------------------
    def find_element(self, locator: Locator, timeout: Optional[int] = None) -> WebElement:
        """Find element and wait until visible (default explicit wait).

        locator: tuple(By, value)
        """
        timeout = timeout or Config.EXPLICIT_WAIT
        try:
            # Prefer WaitHelper if it implements a visible wait
            if hasattr(self.wait_helper, "wait_for_element_visible"):
                return self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            # Fallback to WebDriverWait
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            logger.exception("Element not found: %s", locator)
            with allure.step(f"Attach screenshot on failure for locator: {locator}"):
                try:
                    allure.attach(self.driver.get_screenshot_as_png(), name="element_not_found",
                                  attachment_type=allure.attachment_type.PNG)
                except WebDriverException:
                    logger.exception("Failed to capture screenshot")
            raise ElementNotFoundError(f"Element not found: {locator}") from e

    def find_elements(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    # ----------------------- Actions -----------------------
    def click(self, locator: Locator, element_name: Optional[str] = None, timeout: Optional[int] = None) -> None:
        element_name = element_name or str(locator)
        with allure.step(f"Clicking {element_name}"):
            logger.info("Clicking element %s", locator)
            timeout = timeout or Config.EXPLICIT_WAIT
            try:
                if hasattr(self.wait_helper, "wait_element_clickable"):
                    el = self.wait_helper.wait_element_clickable(self.driver, locator, timeout)
                else:
                    el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
                el.click()
            except TimeoutException as e:
                logger.exception("Element not clickable: %s", locator)
                raise ElementNotFoundError(f"Element not clickable: {locator}") from e

    def enter_text(self, locator: Locator, text: str, element_name: Optional[str] = None,
                   timeout: Optional[int] = None) -> None:
        element_name = element_name or str(locator)
        with allure.step(f"Enter '{text}' into {element_name}"):
            logger.info("Entering text into %s: %s", locator, text)
            el = self.find_element(locator, timeout)
            el.clear()
            el.send_keys(text)

    def get_element_text(self, locator: Locator, timeout: Optional[int] = None) -> str:
        el = self.find_element(locator, timeout)
        return el.text

    def get_attribute(self, locator: Locator, attribute_name: str, timeout: Optional[int] = None) -> Any:
        el = self.find_element(locator, timeout)
        return el.get_attribute(attribute_name)

    # ----------------------- State checks & waits -----------------------
    def is_element_visible(self, locator: Locator, timeout: Optional[int] = None) -> bool:
        timeout = timeout or Config.EXPLICIT_WAIT
        try:
            if hasattr(self.wait_helper, "wait_for_element_visible"):
                self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            else:
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(self, locator: Locator, timeout: Optional[int] = None) -> bool:
        timeout = timeout or Config.EXPLICIT_WAIT
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            logger.debug("Element did not disappear within %s seconds: %s", timeout, locator)
            return False

    # ----------------------- Utilities -----------------------
    def take_screenshot(self, name: str = "screenshot") -> None:
        try:
            png = self.driver.get_screenshot_as_png()
            allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)
        except WebDriverException:
            logger.exception("Failed to take screenshot")

    def refresh_page(self) -> None:
        with allure.step("Refresh page"):
            logger.info("Refreshing page %s", self.get_current_url())
            self.driver.refresh()

    def maximize_window(self) -> None:
        try:
            self.driver.maximize_window()
        except WebDriverException:
            logger.exception("Failed to maximize window")
