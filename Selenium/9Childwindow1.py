import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagepractise/")
driver.find_element(By.XPATH,"//a[@class='blinkingText']").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
# email_text = driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']").text
email_text = driver.find_element(By.XPATH,"//p[@class='im-para red']").text.split(" ")
print("Length:",len(email_text))
for email in email_text:
    if email == "mentor@rahulshettyacademy.com":
        email_text = email
        break
driver.close()
driver.switch_to.window(windows_opened[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email_text)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.XPATH,"//input[@name='signin']").click()
time.sleep(3)
error_msg = driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").get_attribute("innerText")
print(error_msg)
assert error_msg == "Incorrect username/password."