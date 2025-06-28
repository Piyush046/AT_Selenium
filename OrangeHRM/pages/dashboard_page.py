from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.locators import DashboardPageLocators

class DashboardPage(BasePage):
    def get_header_text(self):
        return self.hind(By.CLASS_NAME, DashboardPageLocators.DASHBOARD_HEADER).text
