import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from time import sleep
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def test_valid_login(self):
        login = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        sleep(6)  # Wait for the dashboard to load
        header = dashboard.get_header_text()
        self.assertIn("Dashboard", header)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
