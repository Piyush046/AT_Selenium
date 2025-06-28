
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




# Absolute XPath:
# - Starts from the root (/) of the HTML document.
# - Specifies the complete path to the element.
# - Example: /html/body/div[1]/form/input[1]
# - Disadvantage: Breaks easily if the page structure changes.

# Relative XPath:
# - Starts from anywhere in the document using //.
# - More flexible and robust.
# - Example: //input[@id='username']
# - Advantage: Less likely to break if the page layout


"""List	of	popular	attributes	available	for	By	class
	

LOCATOR_MAP = {
    "ID": By.ID,
    "XPATH": By.XPATH,
    "LINK_TEXT": By.LINK_TEXT,
    "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
    "NAME": By.NAME,
    "TAG_NAME": By.TAG_NAME,
    "CLASS_NAME": By.CLASS_NAME,
    "CSS_SELECTOR": By.CSS_SELECTOR
}


 
 """







driver = webdriver.Chrome()
driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/")




 #In Selenium, XPath is commonly used to locate elements on a web page for automation testing. Example:

""" //tagname[@attribute='value']"""      #This syntax for finding elements using XPath in Selenium."""

"""//*[@attribute='value']"""             #This syntax is used to find elements with a specific attribute value, regardless of the tag name.

driver.maximize_window()  # Maximize the browser window

element = driver.find_element(By.LINK_TEXT, "Create New Profile")  # Find the "Create New Profile" link
sleep(2) # Wait for 2 seconds to ensure the page is fully loaded
element.click()  # Click the link to open the registration form


lable_firstname = driver.find_element(By.XPATH, "//label[@for='id_firstName']")
print("Label for First Name: ", lable_firstname.text)  # Print the label text for the first name field
input_firstname = driver.find_element(By.XPATH, "//*[@id='id_firstName']")
input_firstname.send_keys("Piyush")  # Enter "Piyush" as the first name
input_value_firstname = input_firstname.get_attribute("value") 
 # Get the value entered in the first name field 
print("First Name Input Value: ", input_value_firstname)  # Print the first name value




