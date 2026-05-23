import time

from selenium.webdriver.common.by import By

from Pageobjects.shop import Shoppage


class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@id='username']")
        self.password_input = (By.ID, "password")
        self.signin_button = (By.XPATH, "//input[@name='signin']")

    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password_input).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.signin_button).click()
        time.sleep(5)
        shop_page = Shoppage(self.driver)
        return shop_page


