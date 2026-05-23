import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[contains(@class,'tox-notification')]//button"))).click()
wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))
editor = driver.find_element(By.ID,"tinymce")
driver.execute_script("arguments[0].innerHTML = '';", editor)
time.sleep(2)
# editor.send_keys(Keys.CONTROL + "a")
# editor.send_keys(Keys.DELETE)
driver.execute_script("arguments[0].focus();", editor)
# editor.click()
driver.execute_script("arguments[0].innerText = 'Hello World!';",editor)
# editor.send_keys("Hello World!")
time.sleep(3)
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']").text)