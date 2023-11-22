import time
import unittest
from selenium import webdriver
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from pages_.navigationBar import NavigationBar
from pages_.loginPage import LoginPage
from testData_.testData import validUser, signInPageUrl


class SignOutPage(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(signInPageUrl)

        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field(validUser.username)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        time.sleep(6)
        loginPageObj.click_to_signin_button()

    def test_sign_out_page(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.mouse_move_to_account_and_lists_button()
        time.sleep(6)
        navigationBarObj.click_to_sign_out_element()
        time.sleep(6)

    def tearDown(self):
        self.driver.close()


