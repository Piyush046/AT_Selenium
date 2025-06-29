from time import sleep  # Import sleep to pause execution

from selenium import webdriver  # Import Selenium WebDriver
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.support.ui import Select  # Import Select for dropdowns

"""
Automated Profile Creation Script for TastyFoodApp

This script uses Selenium WebDriver to automate the process of creating a new user profile on
the TastyFoodApp demo website.

Steps performed:
1. Opens the TastyFoodApp registration page.
2. Clicks the "Create New Profile" link.
3. Verifies the greeting text on the registration form.
4. Fills out the registration form fields:
   - First Name
   - Last Name
   - Gender
   - Username
   - Password
   - State (dropdown selection)
   - Fee Plan (dropdown selection)
   - Date
5. Clicks the registration button and accepts the confirmation alert.
6. Submits the form.
7. Prints the result message after submission.

Requirements:
- Python 3.x
- selenium package (`pip install selenium`)
- Chrome browser and ChromeDriver installed and available in PATH

Author: [ Piyush Pandey ]
Date: [15th June 2025]
"""


#CodeBased on the provided script:




driver = webdriver.Chrome()  # Start Chrome browser
driver.maximize_window()  # Maximize the browser window

driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/")  # Open the target website
element = driver.find_element(By.LINK_TEXT, "Create New Profile")  # Find the "Create New Profile" link
element.click()  # Click the link to open the registration form
sleep(2)  # Wait for 2 seconds for the page to load

greeting = driver.find_element(By.CLASS_NAME, "text")  # Find the greeting text element

# Check if the greeting text matches the expected string
if greeting.text == "Greetings, Please fill the form below to get enrolled into the World's Best Home Food Delivery Service":
    print("Text matched successfully!")  # Print if text matches
else:
    print("Text did not match.")  # Print if text does not match

firstname = driver.find_element(By.ID, "id_firstName")  # Find the first name input field
firstname.send_keys("Sourav")  # Enter "Sourav" as the first name
value1 = firstname.get_attribute("value")  # Get the value entered in the first name field
print("First Name: ", value1)  # Print the first name value

lastname = driver.find_element(By.ID, "id_lastName")  # Find the last name input field
lastname.send_keys("Basu")  # Enter "Basu" as the last name

gender = driver.find_element(By.ID, "id_gender_1").click()  # Select the gender radio button

username = driver.find_element(By.ID, "id_username")  # Find the username input field
username.send_keys("sourav123")  # Enter "sourav123" as the username

password = driver.find_element(By.ID, "id_password")  # Find the password input field
password.send_keys("sourav123")  # Enter "sourav123" as the password

state = driver.find_element(By.ID, "id_state")  # Find the state dropdown
Select(state).select_by_visible_text("Texas")  # Select "Texas" from the state dropdown

fee = driver.find_element(By.ID, "id_fee")  # Find the fee dropdown
Select(fee).select_by_visible_text("$200 : Platinum")  # Select "$200 : Platinum" from the fee dropdown

date = driver.find_element(By.ID, "id_date")  # Find the date input field
date.send_keys("2023-10-01")  # Enter the date

sleep(2)  # Wait for 2 seconds

button = driver.find_element(By.ID, "js_button")  # Find the registration button
print("Button status: ", button.is_enabled())  # Print if the button is enabled
button.click()  # Click the registration button

sleep(2)  # Wait for 2 seconds

driver.switch_to.alert.accept()  # Accept the alert popup

sleep(2)  # Wait for 2 seconds

submit_button = driver.find_element(By.NAME, "submit")  # Find the submit button
submit_button.click()  # Click the submit button

sleep(3)  # Wait for 3 seconds

result_thankyou = driver.find_element(By.XPATH, "//*[@class='text']")  # Find the result message
print("Result: ", result_thankyou.text)  # Print the result message

sleep(2)  # Wait for 2 seconds before ending the script