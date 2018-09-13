import unittest

from ddt import ddt, file_data
from selenium import webdriver


@ddt
class RegisterTest (unittest.TestCase):

    def setUp(self):
        # Create a new Chrome session
        self.driver = webdriver.Chrome(executable_path=r"chromedriver")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    @file_data("name.json")
    def test_by_product(self, name):


        self.driver.get("https://petroline.ua/")
        self.driver.find_element_by_href("filter/nasosy?pf_8_57=true").click()
        self.driver.find_element_by_href("product/nasosy/dc-tech_p45").click()
        self.driver.find_element_by_class_name("order-button").click()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("phone").send_keys(name)
        self.driver.find_element_by_class_name("ui blue submit button center").click()



    def tearDown(self):
         self.driver.quit()