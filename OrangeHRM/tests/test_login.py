import sys
import os
from time import sleep
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from selenium import webdriver
from pages.login_page import LoginPage

def test_login_dashboard():
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    print("Login successful, checking dashboard...")
    
    driver.quit()

if __name__ == "__main__":
    test_login_dashboard()
