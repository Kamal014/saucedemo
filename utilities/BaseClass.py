import pytest

from pageObjects.saucedemoLogin import Login


@pytest.mark.usefixtures('browser_setup')
class BaseClass:
    def login(self, user_name, password):
        login_page = Login(self.driver)
        login_page.get_user_name().send_keys(user_name)
        login_page.get_password().send_keys(password)
        login_page.get_login_button().click()

