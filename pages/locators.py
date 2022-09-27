from selenium.webdriver.common.by import By

class ProductPageLocators():
    BASKET_BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-safe p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert")