import string
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import random
import string


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
        register_page = LoginPage(browser, link)
        register_page.open()
        email = ''.join(random.sample(string.ascii_letters, 6)) + '@gmail.com'
        password = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        register_page.register_new_user(email, password)
        register_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_not_be_success_message()


    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_click_button_add_to_basket()
        prod_page.browser.implicitly_wait(5)
        prod_page.should_verificate_product_and_item_names()
        prod_page.should_verificate_product_and_item_price()



def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


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
    prod_page.open()
    prod_page.should_click_button_add_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.browser.implicitly_wait(5)
    prod_page.should_verificate_product_and_item_names()
    prod_page.should_verificate_product_and_item_price()


@pytest.mark.skip
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


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_click_button_add_to_basket()
    prod_page.should_disappeared_success_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_the_basket()
    basket_page.should_be_empty_basket_message()
