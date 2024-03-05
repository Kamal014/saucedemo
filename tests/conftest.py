import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(params=["chrome", "edge"], scope='class')
def browser_setup(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        request.cls.driver = driver
    elif request.param == "edge":
        driver = webdriver.Edge()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        request.cls.driver = driver
    request.cls.driver = driver
    yield
    driver.close()
