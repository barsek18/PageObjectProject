from .pages.product_page import ProductPage
import pytest


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.skip(reason="Product name and item name in the message are different")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    prod_page = ProductPage(browser, link)
    prod_page.open()  # <--- lass BasePage
    prod_page.should_click_button_add_to_basket()  # <--- lass ProductPage
    prod_page.solve_quiz_and_get_code()  # <--- class BasePage
    prod_page.browser.implicitly_wait(5)  # <--- lass BasePage
    prod_page.should_verificate_product_and_item_names()  # <--- lass ProductPage
    prod_page.should_verificate_product_and_item_price()  # <--- lass ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_click_button_add_to_basket()
    prod_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_click_button_add_to_basket()
    prod_page.should_disappeared_success_message()
