from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class AccountHolderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.__viewLocator = (By.XPATH, "(//div[@class='sc-kgTSHT fKJwkr'])[1]")

    def click_to_view_element(self):
        viewLocator = self._find_element(self.__viewLocator)
        self._click(viewLocator)