import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")        #XPath Locator for Email
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()        #Link Text Locator
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter your email address']").send_keys("demo@gmail.com")   #CSS Selector Locator for Email in Forgot Password Page
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("Hello@123")
driver.find_element(By.XPATH,"//input[@id='confirmPassword']").send_keys("Hello@123")   #XPath Locator for Confirm Password
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()        #XPath with text() function
time.sleep(5)