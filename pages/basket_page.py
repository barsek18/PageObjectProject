from email import message
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET_FORM), \
            "Product in basket is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no empty basket message on the page"
