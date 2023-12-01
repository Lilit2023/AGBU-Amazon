import time
from pages_.loginPage import LoginPage
from testData_.testData import validUser, userWithInvalidPassword, userWithInvalidUsername, signInPageUrl
from tests_.baseTest import BestTestWithLogin
from tests_.baseTest import BestTestWithOutLogin

class LogIn(BestTestWithOutLogin):

    def test_positive_login(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(validUser.username)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        time.sleep(6)
        loginPageObj.click_to_signin_button()
        time.sleep(6)

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

#class NegativeLogIn(BestTestWithOutLogin):
    def test_negative_login(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(userWithInvalidUsername.userName)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(userWithInvalidPassword.password)
        loginPageObj.click_to_signin_button()

        self.assertTrue(loginPageObj.is_incorrect_password_error_message_appear(), "Error: Should show incorrect password aller, but did not match message or did not show")






