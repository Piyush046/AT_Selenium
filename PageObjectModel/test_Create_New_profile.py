import unittest
from selenium import webdriver
import createNewProfile

class Testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/create")

    def test_CreatePage(self):
        driver = self.driver
        home = createNewProfile.CreateNewProfile(driver)
        title = home.get_title()
        self.assertEqual("Create New Profile - Tasty Home Food Delivery Service", title)
        print("Page title is: ", title)
       
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()