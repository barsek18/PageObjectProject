from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # open page "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # find button add to basket
    # click button add to basket
    # x = solve_quiz_and_get_code()
    # add locators
    # test the notification that the item has been added to the cart and it matches the product is actually added
    # test that the cost in the basket is the same as the price of the product
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()  # <--- lass BasePage
    prod_page.should_click_button_add_to_basket()  # <--- lass ProductPage
    prod_page.solve_quiz_and_get_code()  # <--- class BasePage
    prod_page.browser.implicitly_wait(5)  # <--- lass BasePage
    prod_page.should_verificate_product_and_item_names()  # <--- lass ProductPage
    prod_page.should_verificate_product_and_item_price()  # <--- lass ProductPage
