from .pages.product_page import ProductPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207'


@pytest.mark.parametrize('link', [f"{link}/?promo=offer0",
                                  f"{link}/?promo=offer1",
                                  f"{link}/?promo=offer2",
                                  f"{link}/?promo=offer3",
                                  f"{link}/?promo=offer4",
                                  f"{link}/?promo=offer5",
                                  f"{link}/?promo=offer6",
                                  pytest.param(
                                      f"{link}/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  f"{link}/?promo=offer8",
                                  f"{link}/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_item_page()
    page.should_be_write_review_btn()
    price1 = page.get_price_from_item_page()
    name1 = page.get_item_name_on_the_item_page()
    page.add_item_to_the_cart()
    page.solve_quiz_and_get_code()
    price2 = page.get_price_from_cart_page()
    name2 = page.get_item_name_on_the_cart_page()
    page.comparing_values(name1, name2)
    page.comparing_values(price1, price2)