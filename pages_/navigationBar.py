from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__cartCountLocator = (By.ID, "nav-cart-count")
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")
        self.__searchFiledLocator = (By.ID, "twotabsearchtextbox")
        self.__searchingButtonLocator = (By.ID, "nav-search-submit-button")
        self.__amazonButtonLocator = (By.ID, "nav-logo-sprites")
        self.__searchAllButtonLocator = (By.ID, "searchDropdownBox")

    def get_cart_count_element(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        self._click(cartCountElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click(cartButtonElement)

    def fill_search_field(self, text):
        fillSearchFieldElement = self._find_element(self.__searchFiledLocator)
        self._fill_field(fillSearchFieldElement, text)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(self.__searchingButtonLocator)
        self._click(searchButtonElement)

    def click_to_amazon_button_locator(self):
        amazonButtonLocator = self.driver.find_element(self.__amazonButtonLocator)
        self._click(amazonButtonLocator)

    def click_to_search_all_dropdown_button(self):
        searchAllDropdownButton = self.driver.find_element(self.__searchAllButtonLocator)
        self._click(searchAllDropdownButton)
c