from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
import pytest


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser,link,0)
    page.open()
    page.go_to_basket()
    page.should_basket_empty()
    page.should_message_basket_empty_present()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser,link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()