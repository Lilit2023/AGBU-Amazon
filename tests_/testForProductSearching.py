import time

from pages_.navigationBar import NavigationBar
from tests_.baseTest import BestTestWithLogin
from pages_.resultPage import ResultPage

class ProductSearching(BestTestWithLogin):

    def test_product_searching(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("coat")
        navigationBarObj.click_to_search_button()

        resultPagObj = ResultPage(self.driver)
        resultPagObj.click_to_result_element()
        resultPagObj.click_to_add_button()
        time.sleep(6)

        self.assertEqual("Amazon.com Shopping Cart", self.driver.title)





