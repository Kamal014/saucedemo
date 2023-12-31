import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='class')
def browser_setup(request):
    #service = ChromeService(executable_path="E:\PYTHON\PythonTesting\chromedriver.exe")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()