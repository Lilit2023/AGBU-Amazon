from selenium.webdriver.common.by import By
from selenium import webdriver
from pages_.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordButtonLocator = (By.ID, "ap_password")
        self.__signInButtonLocator = (By.ID, "signInSubmit")
        self.__changeMailButtonLocator = (By.ID, "ap_change_login_claim")
        self.__detailsButtonLocator = (By.ID, "remember_me_learn_more_link")
        self.__forgotYourPasswordButtonLocator = (By.ID, "auth-fpp-link-bottom")

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordButtonLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_signin_button(self):
        signinButtonElement = self._find_element(self.__signInButtonLocator)
        self._click(signinButtonElement)

    def click_to_change_button(self):
        changeButtonLocator = self._find_element(self.__changeMailButtonLocator)
        self._click(changeButtonLocator)

    def click_to_details_button(self):
        clickDetailsButton = self._find_element(self.__detailsButtonLocator)
        self._click(clickDetailsButton)

    def click_to_forgot_your_password_button(self):
        clickForgotYourPassword = self._find_element(self.__forgotYourPasswordButtonLocator)
        self._click(clickForgotYourPassword)

    def validate_continue_button_text(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        if self._get_text(continueButtonElement) != "continue":
            print("Error: Wrong continue button text")
            exit(2)


