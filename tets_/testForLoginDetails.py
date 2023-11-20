import time
import unittest
from selenium import webdriver
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from pages_.loginPage import LoginPage


class LoginDetails(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_login_page_details(self):
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_username_field("lilmankan@gmail.com")
        self.loginPageObj.click_to_continue_button()
        self.loginPageObj.click_to_details_button()
        time.sleep(6)