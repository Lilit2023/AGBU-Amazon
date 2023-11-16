from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__cartCountLocator = (By.ID, "nav-cart-count")
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")

    def get_cart_count_element(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        self._click(cartCountElement)
    def delete_first_product_from_cart(self):
        firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click(firstProductDeleteButtonElement)





