import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.saucedemoLogin import Login
from pageObjects.saucedemoHomePage import HomePage
from pageObjects.saucedemoCheckoutPage import CheckOut
from utilities.BaseClass import BaseClass
from pageObjects.saucedemoCartPage import CartPage
from TestData.saucedemoTestData import TestData
from selenium.webdriver.support import expected_conditions as EC


class TestSauceDemo(BaseClass):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver.implicitly_wait(5)
        login_page = Login(self.driver)
        # 1st user login
        login_page.get_user_name().send_keys("standard_user")
        login_page.get_password().send_keys("secret_sauce")
        login_page.get_login_button().click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Login", attachment_type=AttachmentType.PNG)
        login_page.get_menu_icon().click()
        login_page.get_logout_link().click()
        # 2nd user login
        login_page.get_user_name().send_keys("locked_out_user")
        login_page.get_password().send_keys("secret_sauce")
        login_page.get_login_button().click()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test= 'error']").text
        assert "Epic sadface: Sorry, this user has been locked out." in error_message

        # 3rd user login
        login_page.get_user_name().clear()
        login_page.get_user_name().send_keys("problem_user")
        login_page.get_login_button().click()
        self.driver.save_screenshot("problem_user.png")
        login_page.get_menu_icon().click()
        login_page.get_logout_link().click()
        self.driver.implicitly_wait(5)

    def test_add_to_cart(self):
        self.driver.implicitly_wait(5)
        self.login("standard_user", "secret_sauce")
        #wait.until(EC.presence_of_element_located(self.driver.find_element(By.XPATH, "//span[@class='title']")))
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)
        items_listed = self.driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
        for items in items_listed:
            items.click()

        home_page.get_cart_icon().click()
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        cart_page.get_checkout_button().click()
        self.driver.save_screenshot("after_cart.png")

    def test_check_out(self, get_data):
        check_out_page = CheckOut(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(check_out_page.first_name))
        check_out_page.get_first_name().send_keys(get_data["firstname"])
        check_out_page.get_last_name().send_keys(get_data["lastname"])
        check_out_page.get_zip_code().send_keys(get_data["ZIP"])
        check_out_page.get_continue_button().click()
        self.driver.save_screenshot("after_checkout.png")
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="checkout", attachment_type=AttachmentType.PNG)

    @pytest.fixture(params=TestData.checkout_data)
    def get_data(self, request):
        return request.param

    @allure.severity(allure.severity_level.CRITICAL)
    def test_overview(self):
        items_price = self.driver.find_elements(By.XPATH, "//div[@class= 'inventory_item_price']")
        total_price = 0
        for price in items_price:
            format_price = price.text.split('$')[1]
            total_price += float(format_price)
        print(total_price)
        total_price_on_screen = float(
            self.driver.find_element(By.XPATH, "//div[@class= 'summary_subtotal_label']").text.split('$')[1])
        print(total_price_on_screen)
        assert total_price == total_price_on_screen
        tax_amount = float(self.driver.find_element(By.XPATH, "//div[@class= 'summary_tax_label']").text.split('$')[1])
        total_price_to_paid = total_price + tax_amount
        total_price_to_paid_on_screen = float(
            self.driver.find_element(By.XPATH, "//div[@class= 'summary_info_label summary_total_label']").text.split(
                '$')[1])
        assert total_price_to_paid == total_price_to_paid_on_screen

        self.driver.find_element(By.ID, "finish").click()
        thank_you = self.driver.find_element(By.XPATH, "//h2[@class = 'complete-header']")
        assert thank_you.is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="thank you", attachment_type=AttachmentType.PNG)
