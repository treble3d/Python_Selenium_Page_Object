from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON_ADD)
        basket_button.click()
    def check_basket(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        bascet_product = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE)
        assert product.text == bascet_product.text, "product_name error"
        assert price.text == basket_price.text, "product_price error"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear"
