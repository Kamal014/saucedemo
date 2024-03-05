import inspect

import pytest
import logging
from pageObjects.saucedemoLogin import Login


@pytest.mark.usefixtures('browser_setup')
class BaseClass:
    def login(self, user_name, password):
        login_page = Login(self.driver)
        login_page.get_user_name().send_keys(user_name)
        login_page.get_password().send_keys(password)
        login_page.get_login_button().click()

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("E:/PYTHON/PythonTesting/SauceDemo/log/test_runner.log")
        formatter = logging.Formatter(("%(asctime)s :%(levelname)s : %(name)s :%(message)s"))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
