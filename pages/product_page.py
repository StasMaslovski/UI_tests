from .base_page import BasePage
from .locators import ItemPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def should_be_write_review_btn(self):
        assert self.is_element_present(
            *ItemPageLocators.WRITE_REVIEW), 'button "write review" is not present on the page'

    def should_be_item_page(self):
        assert 'catalogue' in self.get_current_url(), 'this is not excepted page'

    def add_item_to_the_cart(self):
        self.click_on_the_btn(*ItemPageLocators.ADD_TO_BASKET_BTN)

    def get_price_from_item_page(self):
        return self.get_value(*ItemPageLocators.ITEM_PAGE_PRICE)

    def get_price_from_the_message(self):
        return self.get_value(*ItemPageLocators.PRICE_IN_THE_MESSAGE)

    def get_item_name_on_the_item_page(self):
        return self.get_value(*ItemPageLocators.ITEM_NAME)

    def get_item_name_from_the_message(self):
        return self.get_value(*ItemPageLocators.ITEM_NAME_IN_THE_MESSAGE)

    def is_not_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE)

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ItemPageLocators.SUCCESS_MESSAGE)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"


