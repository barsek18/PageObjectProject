from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_click_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET_LINK)
        #print("BUTTON_ADD_TO_BASKET_LINK ... ok")
        button.click()

    def should_verificate_product_and_item_names(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LINK).text
        #print(f"PRODUCT_NAME ... {product_name}")
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_THE_MESSAGE_LINK).text
        #print(f"ITEM_NAME_IN_THE_MESSAGE ... {item_name}")
        assert product_name == item_name, "Product name and item name in the message  are different"

    def should_verificate_product_and_item_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LINK).text
        #print(f"PRODUCT_PRICE ... {product_price}")
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_THE_MESSAGE_LINK).text
        #print(f"ITEM_PRICE_IN_THE_MESSAGE ... {item_price}")
        assert product_price == item_price, "Product price and item price in the message  are different"
