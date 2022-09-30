from selenium.webdriver.common.by import By


class ProductPageLocators():
    BASKET_BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-safe p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "span>a.btn")
    BASKET_FULL = (By.CSS_SELECTOR, "form.basket_summary")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div.content p")

class LoginPageLocators():
    REG_EMAIL = (By.CSS_SELECTOR, "input[name=registration-email]")
    REG_PASSWORD = (By.CSS_SELECTOR, "input[name=registration-password1]")
    REG_PASSWORD_REP = (By.CSS_SELECTOR, "input[name=registration-password2]")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
    REG_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")