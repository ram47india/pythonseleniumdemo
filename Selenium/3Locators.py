# Locators- ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, CSS Selector, XPath
# ID - Unique identifier for an element
# Name - Name attribute of an element
# XPath - XML Path Language, used to navigate through elements and attributes in an XML document
# Abosulute XPath - Full path from the root element to the desired element
# Example - /html/body/div[1]/div[2]/input
# Relative XPath - Path from a specific element to the desired element
# Example - //input[@id='username']
# XPath Syntax - //tagname[@attributename='attributvalue']
# Example - //input[@id='username']
# CSS Selector - Cascading Style Sheets, used to style and layout web pages
# CSS Selector Syntax - tagname[attributename='attributvalue']
# Example - input[id='username']
# CSS ID Syntax - #idvalue
# Example - #username
# CSS Class Syntax- .classvalue
# Example - .inputtext
# Link Text - The exact text of a hyperlink
# Partial Link Text - A portion of the text of a hyperlink
# Tag Name - The name of an HTML tag
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver .get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"div[class='form-group'] input[name='name']").send_keys("Ramkumar")   #CSS Selector Locator
driver.find_element(By.NAME,'email').send_keys("ram@gmail.com")         #Name Locator
driver.find_element(By.ID,'exampleInputPassword1').send_keys("123456")  #ID Locator
driver.find_element(By.ID,"exampleCheck1").click()                      #ID Locator
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()               #CSS ID Locator
driver.find_element(By.XPATH,"(//input[@name = 'name'])[2]").send_keys("HelloTesting")  #XPath Locator


driver.find_element(By.XPATH,"//input[@type='submit']").click()           #XPath Locator
success_message =  driver.find_element(By.CLASS_NAME,"alert-success").text
print(success_message)

time.sleep(2)
