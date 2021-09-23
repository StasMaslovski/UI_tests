from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert "Ваша корзина пуста" in self.get_value(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            'Should be message "Ваша корзина пуста", but there is no'

    def there_is_no_item_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_THE_BASKET), \
            "There are any items, but not should be"
