from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# In Selenium, there are two main types of waits:

# 1. Implicit Wait:
# - Tells WebDriver to poll the DOM for a certain amount of time when trying to find any element.
# - Applies globally to all elements.
# - Example:
#   driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear

# 2. Explicit Wait:
# - Waits for a certain condition to occur before proceeding further in the code.
# - Applies only to specific elements or conditions.
# - Uses WebDriverWait in combination with expected_conditions.
# - Example:
#   from selenium.webdriver.common.by import By
#   from selenium.webdriver.support.ui import WebDriverWait
#   from selenium.webdriver.support import expected_conditions as EC
#   element = WebDriverWait(driver, 10).until(
#       EC.presence_of_element_located((By.ID, "someId"))
#   )




# Example of Implicit Wait:
driver = webdriver.Chrome()
driver.maximize_window() 
#driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to be found

driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/")  # Open the target website
  # Will wait up to 10 seconds if not immediately found
element = driver.find_element(By.LINK_TEXT, "Create New Profile")  # Find the "Create New Profile" link
element.click()  # Click the link to open the registration form





# Example of Explicit Wait:


input_firstname = driver.find_element(By.XPATH, "//*[@id='id_firstName']")
input_firstname.send_keys("Piyush")  # Enter "Piyush" as the first name
input_value_firstname = input_firstname.get_attribute("value") 
 # Get the value entered in the first name field 

element2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_firstName"))
    
)  # Waits up to 10 seconds for the element with id 'username' to appear

