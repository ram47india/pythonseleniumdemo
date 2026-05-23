import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Pageobjects.login import Loginpage
from Pageobjects.shop import Shoppage
def test_e2eexecution(browseroptioninstance):

    driver = browseroptioninstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = Loginpage(driver)
    shop_page = login_page.login()
    shop_page.add_product_to_cart("Blackberry")
    checkout_confirmation_page = shop_page.goToCart()
    checkout_confirmation_page.checkout()
    checkout_confirmation_page.enter_delivery_address("ind")
    checkout_confirmation_page.validate_order_confirmation()

