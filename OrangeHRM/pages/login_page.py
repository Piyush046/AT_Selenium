from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_username(self, username):
        self.find(By.NAME, LoginPageLocators.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find(By.CLASS_NAME, LoginPageLocators.LOGIN_BUTTON).click()
