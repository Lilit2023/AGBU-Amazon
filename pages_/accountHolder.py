from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class WhosShopingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__viewLocator = (By.CLASS_NAME, "sc-kgTSHT fKJwkr")

    def click_to_view_element(self):
        viewLocator = self._find_element(self.__viewLocator)
        self._click(viewLocator)