import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pageobjects.checkout_confirmation import CheckoutConfirmation
from utils.browserutils import BrowseUtils


class Shoppage(BrowseUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.shop_link = (By.XPATH, "//a[contains(normalize-space(), 'Shop')]")
        self.product_card = (By.XPATH, "//div[@class='card h-100']")
        self.go_to_cart_checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def add_product_to_cart(self, product_name):
        self.wait.until(EC.element_to_be_clickable(self.shop_link)).click()

        products = self.wait.until(
            EC.presence_of_all_elements_located(self.product_card)
        )
        for product in products:
            productname = product.find_element(By.XPATH,"div/h4/a").text
            if productname == product_name:
                time.sleep(5)
                product.find_element(By.XPATH,"div/button").click()

    def goToCart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.go_to_cart_checkout_button)
        ).click()
        checkout_coonfirmation_page = CheckoutConfirmation(self.driver)
        return checkout_coonfirmation_page




