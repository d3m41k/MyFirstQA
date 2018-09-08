from selenium import webdriver

# Driver initialization
driver = webdriver.Chrome(executable_path=r"../chromedriver")

# Open page
driver.get ("http://www.google.com")

driver.find_element_by_name("g").send_keys("Be QA Today")
driver.find_element_by_name("g").submit()

# Check the result

assert driver.find_element_by_link_text("Be QA Today").is_displayed()

#Close the driver
driver.guit ()
