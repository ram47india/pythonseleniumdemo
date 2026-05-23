import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"autocomplete").send_keys("ind")
time.sleep(2)  #Wait for 3 seconds to allow the dynamic suggestions to load
#Dynamic Dropdowns
dynamic_dropdowns = driver.find_elements(By.CLASS_NAME,"ui-menu-item-wrapper")  #Locate all the dynamic dropdown suggestions
print(len(dynamic_dropdowns)) #Print the count of the dynamic dropdown suggestions
for dropdown in dynamic_dropdowns:
    if dropdown.text == "India":
        dropdown.click()
        # time.sleep(2)
        output = driver.find_element(By.ID,"autocomplete").get_attribute("value")  #Print the selected value from the input field
        print(output)
        assert output == "India"
        # break
#Checkboxes
check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(check_boxes))
for check_box in check_boxes:
    if check_box.get_attribute("value") == "option1":   #get the value attribute of the checkbox
        check_box.click()
        assert check_box.is_selected()  #Verify if the checkbox is selected
        time.sleep(2)
    if check_box.get_attribute("value") == "option2":   #get the value attribute of the checkbox
        check_box.click()
        assert check_box.is_selected()  #Verify if the checkbox is selected
        time.sleep(2)
    if check_box.get_attribute("value") == "option3":   #get the value attribute of the checkbox
        check_box.click()
        assert check_box.is_selected()  #Verify if the checkbox is selected
        time.sleep(2)
#Radio Buttons
radio_buttons = driver.find_elements(By.NAME,"radioButton")
radio_buttons[0].click()  #Select the third radio button using index
time.sleep(2)
assert radio_buttons[0].is_selected()  #Verify if the radio button is selected
radio_buttons[1].click()  #Select the third radio button using index
time.sleep(2)
assert radio_buttons[1].is_selected()  #Verify if the radio button is selected
radio_buttons[2].click()  #Select the third radio button using index
time.sleep(2)
assert radio_buttons[2].is_selected()  #Verify if the radio button is selected
#isDisplayed()
assert driver.find_element(By.ID,"displayed-text").is_displayed()   #Verify if the element is displayed
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
#Popup - Javascript Alert
name = "Ramkumar"
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
alertobj = driver.switch_to.alert
alerttext = alertobj.text
print(alerttext)
assert name in alerttext
alertobj.accept()