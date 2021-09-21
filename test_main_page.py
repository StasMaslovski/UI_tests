from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

MAIN_URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    link = MAIN_URL
    page = MainPage(browser, link)  # create exemplar of MainPage class
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
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
    page = ProductPage(browser, link)
    page.is_present_message_empty_basket()

