from .base_page import BasePage
from .locators import MainPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON_ADD)
        basket_button.click()
    def check_basket(self):
        product = self.browser.find_element(*MainPageLocators.PRODUCT_NAME)
        bascet_product = self.browser.find_element(*MainPageLocators.BASKET_PRODUCT_NAME)
        price = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*MainPageLocators.BASKET_PRODUCT_PRICE)
        assert product.text == bascet_product.text, "product_name error"
        assert price.text == basket_price.text, "product_price error"


