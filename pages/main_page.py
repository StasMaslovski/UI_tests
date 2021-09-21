from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_from_main_page_to_basket_page(self):
        self.click_on_the_btn(*MainPageLocators.BASKET_BTN)
