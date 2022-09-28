from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FULL), \
            "Basket is not empty, but should be"

    def should_message_basket_empty_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Basket empty message is not present"
