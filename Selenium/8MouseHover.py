import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(3)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() #Mouse Hover
time.sleep(5)
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()  #Right Click
time.sleep(3)
action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Reload']")).click().perform() #Left Click on Reload