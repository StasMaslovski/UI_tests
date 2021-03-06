import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

MAIN_URL = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = MAIN_URL
        page = MainPage(browser, link)  # create exemplar of MainPage class
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = MAIN_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_from_main_page_to_basket_page()


def test_go_to_basket_page_from_main_page(browser):
    link = MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_from_main_page_to_basket_page()
    page = BasketPage(browser, link)
    page.there_is_no_item_in_the_basket()
    page.should_be_empty_basket()
