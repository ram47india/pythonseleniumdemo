from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#collect all veggie name into Browsersortedveggielist
veggielements = driver.find_elements(By.XPATH,"//tr/td[1]")
browsersortedveggielist = []
for element in veggielements:
    browsersortedveggielist.append(element.text)
originalveggielist = browsersortedveggielist.copy()
browsersortedveggielist.sort()
assert originalveggielist == browsersortedveggielist
