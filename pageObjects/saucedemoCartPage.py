from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.ID, "checkout")

    def get_checkout_button(self):
        return self.driver.find_element(*CartPage.checkout_button)
