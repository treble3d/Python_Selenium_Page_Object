from .pages.basket_page import BasketPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser,link,0)
    page.open()
    page.go_to_basket()
    page.should_basket_empty()
    page.should_message_basket_empty_present()