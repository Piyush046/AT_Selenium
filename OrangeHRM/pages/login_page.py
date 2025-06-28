from selenium.webdriver.common.by import By

class LoginPage:
    # Locators (all in the same page)
    USERNAME_INPUT = "username"
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def login(self, username, password):
        self.driver.find_element(By.NAME,self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.DASHBOARD_HEADER).is_displayed()
