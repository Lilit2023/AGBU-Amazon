import time
from pages_.navigationBar import NavigationBar
from tests_.baseTest import BestTestWithLogin

class SignOutPage(BestTestWithLogin):

    def test_sign_out_page(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.mouse_move_to_account_and_lists_button()
        time.sleep(6)
        navigationBarObj.click_to_sign_out_element()
        time.sleep(6)
        self.assertEqual("Amazon Sign-In", self.driver.title)



