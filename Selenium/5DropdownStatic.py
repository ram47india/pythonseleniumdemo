import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
dropdown = Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
dropdown.select_by_visible_text("Teacher")          #Select by Visible Text
time.sleep(2)
drop_value = driver.find_element(By.XPATH,"//select[@class='form-control']").get_attribute("value")
assert drop_value ==  "teach"
dropdown.select_by_index(2)         #Select by Index
drop_value = driver.find_element(By.XPATH, "//select[@class='form-control']").get_attribute("value")
assert drop_value == "consult"
time.sleep(2)
dropdown.select_by_value("stud")    #Select by Value
time.sleep(2)
drop_value = driver.find_element(By.XPATH, "//select[@class='form-control']").get_attribute("value")
assert drop_value == "stud"
