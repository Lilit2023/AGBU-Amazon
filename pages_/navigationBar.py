from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")
        self.__searchFiledLocator = (By.ID, "twotabsearchtextbox")
        self.__searchingButtonLocator = (By.ID, "nav-search-submit-button")
        self.__amazonButtonLocator = (By.ID, "nav-logo-sprites")
        self.__allSearchButtonLocator = (By.ID, "searchDropdownBox")

    def click_to_cart_button(self):
        cartButtonElement = self.driver.find_element(self.__cartButtonLocator)
        self._click(cartButtonElement)


    def fill_search_field(self, text):
        fillSearchFieldElement = self._fill_field(self.__searchFiledLocator)
        self._fill_field(fillSearchFieldElement, text)

    def searching_button_element(self):
        searchingButtonElement = self._find_element(self.__searchingButtonLocator)
        self._click(searchingButtonElement)

    def click_to_amazon_button_locator(self):
        amazonButtonLocator = self.driver.find_element(self.__amazonButtonLocator)
        self._click(amazonButtonLocator)

    def click_all_search_button_locator(self):
        allSearchButtonLocator = self.driver.find_element(self.__allSearchButtonLocator)
        self._click(allSearchButtonLocator)
