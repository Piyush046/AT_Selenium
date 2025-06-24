from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from BasePage import BasePage  # Importing Parent Class BasePage
from Locator import CreatePageLocators  # Importing CreatePageLocators

class CreateNewProfile(BasePage):

    def __init__(self, driver):
        """
        Initializes the CreateNewProfile page with the given WebDriver instance.
        :param driver: The WebDriver instance to control the browser.
        """
        super().__init__(driver)
        self.driver = driver



    def get_title(self):
        """Returns the title of the web page."""

        title= self.driver.title
        return title

    
    