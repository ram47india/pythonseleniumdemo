from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")    # To start the browser maximized
chrome_options.add_argument("--headless=new")   # To run browser in headless mode
chrome_options.add_argument("--ignore-certificate-errors") # Applicable to Windows OS only
chrome_options.add_argument("--incognito")  # To open browser in incognito mode

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.get("https://10.233.43.176/")
print(driver.title)