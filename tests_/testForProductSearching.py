import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class ProductSearching(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.driver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("lilmankan@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("amazonlilit2023@")
        time.sleep(6)
        loginPageObj.click_to_signin_button()
        time.sleep(15)

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def test_product_searching(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("coat")
        navigationBarObj.click_to_search_button()

    def tearDown(self):
        self.driver.close()

