from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from Locator import HomePageLocator

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def test_title(self):
        """Returns the title of the Home page."""
        return self.driver.title

    def test_heading(self):
        """
        Locates the heading of the web page and returns its text.
        Assumes the heading has a class name defined in HomePageLocator.
        """
        heading_element = self.driver.find_element(
            By.CLASS_NAME, HomePageLocator.heading_xpath
        )
        return heading_element.text