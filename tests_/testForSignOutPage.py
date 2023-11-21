import time
import unittest
from selenium import webdriver
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from pages_.navigationBar import NavigationBar
from pages_.loginPage import LoginPage


class SignOutPage(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field("lilmankan@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("amazonlilit2023@")
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


