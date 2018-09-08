import email
import unittest

from selenium import webdriver

class RegisterTest (unittest.TestCase):

    def setUp(self):
        # Create a new Chrome session
        self.driver = webdriver.Chrome(executable_path=r"chromedriver")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()


    def test_email_validation(self):
        email = "we1qw2sddd"

        self.driver.get("http://automationpractice.com")
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_id("email_create").send_keys(email)
        self.driver.find_element_by_id("SubmitCreate").click()

    def tearDown(self):
         self.driver.quit()