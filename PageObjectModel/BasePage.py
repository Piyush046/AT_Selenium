from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def set_element_id(self, locator_value, input_value, timeout=10):
        """
        Waits for an element by ID, clicks it, and sends input_value to it.
        :param locator_value: The ID of the web element.
        :param input_value: The string value to send to the element.
        :param timeout: Maximum wait time in seconds (default is 10).
        """
        # Wait for the element to be present and visible
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.ID, locator_value))
        )
        element.click()
        element.send_keys(input_value)