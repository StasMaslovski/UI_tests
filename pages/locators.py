from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-group > .btn:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    # Login form
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_ADDRESS = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    # BUTTON_LOGIN = (By.CSS_SELECTOR, '')

    # Registration form
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONF_REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BTN = (By.NAME, 'registration_submit')


class ItemPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
    WRITE_REVIEW = (By.CSS_SELECTOR, '#write_review')
    ITEM_PAGE_PRICE = (By.CSS_SELECTOR, '.price_color')
    ITEM_NAME = (By.CSS_SELECTOR, 'div > h1')
    PRICE_IN_THE_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    ITEM_NAME_IN_THE_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) > .alertinner')


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    ITEM_IN_THE_BASKET = (By.CSS_SELECTOR, '.thumbnail')
