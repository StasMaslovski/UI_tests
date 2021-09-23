from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.get_current_url(), 'login" is not present in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not present on the page'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM), 'registration form is not present on the page'
        assert True

    def register_new_user(self, email, password):
        self.open()
        self.fill_the_form(*LoginPageLocators.REG_ADDRESS, email)
        self.fill_the_form(*LoginPageLocators.REG_PASSWORD, password)
        self.fill_the_form(*LoginPageLocators.CONF_REG_PASSWORD, password)
        self.click_on_the_btn(*LoginPageLocators.REGISTER_BTN)
