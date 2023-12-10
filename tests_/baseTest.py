import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
from testData_.testData import mainPageUrl, signInPageUrl, validUser


class BaseTestWithoutLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

    def tearDown(self):
        self.driver.close()


class BaseTestWithLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(signInPageUrl)
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_username_field(validUser.username)
        self.loginPageObj.click_to_continue_button()
        self.loginPageObj.fill_password_field(validUser.password)
        time.sleep(7)
        self.loginPageObj.click_to_signin_button()

    def tearDown(self):
        self.driver.close()