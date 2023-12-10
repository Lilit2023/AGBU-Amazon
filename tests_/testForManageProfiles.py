import time
from pages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithLogin
from pages_.accountHolder import AccountHolderPage


class AccountHolder(BaseTestWithLogin):

    def test_product_searching(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.mouse_move_to_account_and_lists_button()
        time.sleep(4)
        navigationBarObj.click_to_manage_profiles_element()
        time.sleep(4)

        accountHolderObj = AccountHolderPage(self.driver)
        accountHolderObj.click_to_view_element()
        time.sleep(6)

        self.assertEqual("Profile Hub", self.driver.title)