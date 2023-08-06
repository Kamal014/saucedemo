from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    def get_first_name(self):
        return self.driver.find_element(*CheckOut.first_name)

    def get_last_name(self):
        return self.driver.find_element(*CheckOut.last_name)

    def get_zip_code(self):
        return self.driver.find_element(*CheckOut.zip_code)

    def get_continue_button(self):
        return self.driver.find_element(*CheckOut.continue_button)

