from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreatePageLocators:
    # Example locators for "Create New Profile" page
    FIRST_NAME_INPUT_ID = "id_firstName"
    LAST_NAME_INPUT_ID = "id_lastName"
    
class HomePageLocator:
    link_text_1 = "Create New Profile"
    heading_xpath="//h1"