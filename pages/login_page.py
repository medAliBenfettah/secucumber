from utils.config import Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    #----------------------------------- LOCATORS -----------------------------------#
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    FORGET_PASSWORD_LINK = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    LOGIN_LOGO = (By.XPATH, "//div[@class='orangehrm-login-logo']/img")
    
    #-------------------------- Dashboard header locator to verify successful login -------------------------- #
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    USER_DROPDOWN = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL
        
    @allure.step("Navigate to Login Page")
    def open(self) -> None:
        self.navigate_to_url(self.url)
        self.maximize_window()
        
    @allure.step("Enter username")
    def enter_username(self, username: str) -> None:
        self.enter_text(self.USERNAME_INPUT, username, "Username Input")
        return self
    
    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.enter_text(self.PASSWORD_INPUT, password, "password Input")
        return self
    
    @allure.step("Click on login button {LOGIN_BUTTON}")   
    def click_login_button(self) -> None:     
        self.click(self.LOGIN_BUTTON, "login Button")
        
    @allure.step("Login with username: {username} and password: {password}")
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self
    
    @allure.step("Click on Forget Password link")
    def click_forget_password_link(self) -> None:
        self.click(self.FORGET_PASSWORD_LINK, "Forget Password Link")

    def is_login_page_displayed(self) -> bool:
        return self.is_element_visible(self.LOGIN_LOGO)
    
    def is_error_message_displayed(self) -> bool:
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=3)
        
    def is_login_successful(self) -> bool:
        return self.is_element_visible(self.DASHBOARD_HEADER, timeout=10)
    
    def is_user_dropdown_displayed(self) -> bool:
        return self.is_element_visible(self.USER_DROPDOWN, timeout=5)
    
    allure.step("Watch for the page to load")
    def wait_for_page_to_load(self) -> None:
        self.is_element_visible(self.LOGIN_LOGO, timeout=10)
        self.is_element_visible(self.LOGIN_LOGO, timeout=10)
    
    
        
    
    
    