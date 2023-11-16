import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class LogIn(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_login(self):
        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field("lilmankan@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("amazonlilit2023@")
        time.sleep(6)
        loginPageObj.click_to_signin_button()
        #time.sleep(6)

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def test_negative_login(self):
        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field("lilmankan@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("lilit2023")
        loginPageObj.click_to_signin_button()

    def tearDown(self):
        self.driver.close()




