from selenium.webdriver.common.by import By

from pageObjects.saucedemoCartPage import CartPage


class HomePage:

    def __init__(self,  driver):
        self.driver = driver

    add_to_cart = (By.XPATH, "//button[@class = 'btn btn_primary btn_small btn_inventory']")
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")

    def get_add_to_cart(self):
        return self.driver.find_elements(*HomePage.add_to_cart)

    def get_cart_icon(self):
        return self.driver.find_element(*HomePage.cart_icon)
        # cart_page = CartPage(self.driver)
        # return cart_page

