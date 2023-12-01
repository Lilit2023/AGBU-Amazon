from pages_.basePage import BasePage
from selenium.webdriver.common.by import By


class DetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__resultPageLocator = (By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])[1]")
        self.__addToShoppingCartLocator = (By.ID, "add-to-cart-button")

    def click_to_result_element(self):
        resultPageElement = self._find_element(self.__resultPageLocator)
        self._click(resultPageElement)

    def click_to_add_button(self):
        addButtonElement = self._find_element(self.__addToShoppingCartLocator)
        self._click(addButtonElement)