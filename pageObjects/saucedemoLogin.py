from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    login_button = (By.ID, "login-button")
    menu_icon = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def get_user_name(self):
        return self.driver.find_element(*Login.user_name)

    def get_password(self):
        return self.driver.find_element(*Login.password)

    def get_login_button(self):
        return self.driver.find_element(*Login.login_button)

    def get_menu_icon(self):
        return self.driver.find_element(*Login.menu_icon)

    def get_logout_link(self):
        return self.driver.find_element(*Login.logout_link)