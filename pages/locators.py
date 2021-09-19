from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


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
    # BUTTON_REGISTER = (By.CSS_SELECTOR, '')
