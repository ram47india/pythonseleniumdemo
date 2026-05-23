import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Scroll Down by Pixels
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(3)
# Scroll Up by Pixels
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight);")
time.sleep(3)
# Screenshot
driver.get_screenshot_as_file("screen1.png")