import json
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Pageobjects.logindatadriven import Loginpagedatadriven
from Pageobjects.shop import Shoppage

# test_data_path = 'Data/test_e2eTestFramework.json'
test_data_path = r'C:\Users\SESA644934\PycharmProjects\PythonAutomationTesting\Data\test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2eexecution(browseroptioninstance,test_list_item):

    driver = browseroptioninstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = Loginpagedatadriven(driver)
    print(login_page.get_title())
    shop_page = login_page.login(test_list_item["UserEmail"],test_list_item["UserPassword"])
    shop_page.add_product_to_cart(test_list_item["ProductName"])
    print(shop_page.get_title())
    checkout_confirmation_page = shop_page.goToCart()
    checkout_confirmation_page.checkout()
    checkout_confirmation_page.enter_delivery_address("ind")
    checkout_confirmation_page.validate_order_confirmation()
    print(checkout_confirmation_page.get_title())

