from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



driver = webdriver.Chrome()
driver.maximize_window() 


driver.get("https://callbomber.in/Call+Sms.php")


sleep(30)  # Wait for the page to load


number = driver.find_element(By.XPATH, "//input[@type='number']")
number.send_keys("")  # Replace with the desired phone number
term = driver.find_element(By.ID, "terms")
term.click()  # Click the terms checkbox
button = driver.find_element(By.CLASS_NAME, "fa fa-Bomb")
button.click()  # Click the button to start the call bombing


# Project has been shoutdown due to Capcha issues,
# Project may require additional steps or configurations to work properly.