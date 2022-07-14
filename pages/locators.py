from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    #LOGIN_USERNAME = (By.CSS_SELECTOR, "input#id_login-username:required")
    #LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password:required")
    #LOGIN_REDIRECT_PASSWORD = (By.XPATH, "//input[@id='id_login-redirect_url']/following::a")
    #LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")

    #REGISTRATION_USERNAME = (By.CSS_SELECTOR, "input#id_registration-email:required")
    #REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1:required")
    #REGISTRATION_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "input#id_registration-password2:required")
    #REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_LINK = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    ITEM_NAME_IN_THE_MESSAGE_LINK = (By.CSS_SELECTOR, "#messages :first-child > .alertinner > strong")
    ITEM_PRICE_IN_THE_MESSAGE_LINK = (By.CSS_SELECTOR, "#messages :nth-child(3) > .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert")
