import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def browser_setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
