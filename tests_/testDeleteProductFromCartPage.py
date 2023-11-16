import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.cartPage import CartPage
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.events import EventFiringWebDriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

class ProductDeletion(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_username_field("lilmankan@gmail.com")
        self.loginPageObj.click_to_continue_button()
        self.loginPageObj.fill_password_field("amazonlilit2023@")
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "signInSubmit"))).click()
        time.sleep(6)
        self.loginPageObj.click_to_signin_button()

    def test_for_delete_first_product(self):
        cartPageObj = CartPage(self.driver)
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nav-cart-count"))).click()
        cartPageObj.delete_first_product_from_cart()
        time.sleep(6)


    def tearDown(self):
        self.driver.close()