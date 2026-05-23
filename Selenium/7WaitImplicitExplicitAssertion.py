import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)  #Implicit Wait of 5 seconds for all elements
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(products)
assert count > 0
expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []
for product in products:    #Iterate through each product
    product.find_element(By.XPATH,"div/button").click() #Click on Add to Cart button for each product
    #i.e "//div[@class='products']/div//div/button"
    result = product.find_element(By.XPATH,"h4").text
    actual_list.append(result)
assert expected_list == actual_list  #Validate the expected and actual product lists
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
promo_result = driver.find_element(By.CLASS_NAME,"promoInfo")
assert promo_result.is_displayed()
print(promo_result.text)
assert "Code applied ..!" in promo_result.text
#sum validation
prices = driver.find_elements(By.XPATH,"//tr//td[5]/p")
sum = 0
for price in prices:
    print(price.text)
    sum = sum + int(price.text)
print("Sum:",sum)
total = driver.find_element(By.CSS_SELECTOR,".totAmt").text
print("Total:",total)
assert sum == int(total)
#validation of Total Amount after discount
disc_ampunt = driver.find_element(By.XPATH,"//span[@class='discountAmt']")
print("Discounted Amount:",disc_ampunt.text)
assert total > disc_ampunt.text
