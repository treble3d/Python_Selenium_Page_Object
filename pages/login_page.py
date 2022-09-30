from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_REP)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON)
        button.click()

