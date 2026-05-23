import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

driver_chrome = webdriver.Chrome()
driver_chrome.get("https://rahulshettyacademy.com/")
driver_chrome.maximize_window()
print(driver_chrome.title)
print(driver_chrome.current_url)
time.sleep(2)
print("Chrome Test Completed")
driver_chrome.quit()

firefoxservice_obj = FirefoxService("C:\\Users\\SESA644934\\PycharmProjects\\PythonAutomationTesting\\Selenium\\geckodriver.exe")
driver_firefox = webdriver.Firefox(service=firefoxservice_obj)
driver_firefox.get("https://rahulshettyacademy.com/angularpractice/")
driver_firefox.maximize_window()
print(driver_firefox.title)
print(driver_firefox.current_url)
time.sleep(2)
print("Firefox Test Completed")
driver_firefox.quit()

edgeservice_obj = EdgeService(r"C:\Users\SESA644934\PycharmProjects\PythonAutomationTesting\Selenium\msedgedriver.exe")
driver_edge = webdriver.Edge(service=edgeservice_obj)
driver_edge.get("https://rahulshettyacademy.com/")
driver_edge.maximize_window()
print(driver_edge.title)
print(driver_edge.current_url)
time.sleep(2)
print("Edge Test Completed")
driver_edge.quit()