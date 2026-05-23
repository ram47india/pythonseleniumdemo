from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
print("New Window Text:",driver.find_element(By.TAG_NAME,'h3').text)
driver.close()
driver.switch_to.window(windows_opened[0])
parent_window_text = driver.find_element(By.TAG_NAME,'h3').text
print("Parent Window Text:",parent_window_text)
assert "Opening a new window" == parent_window_text