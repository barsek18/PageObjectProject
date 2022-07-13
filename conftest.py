from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en', help="Choose a browser language: --language=<your language>")


@pytest.fixture(scope='function')
def browser(request):
    user_lang = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    browser = None

    if user_lang==None:
        raise pytest.UsageError('--language should be specified')

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_lang)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield browser

    print('\nquit browser')
    browser.quit()
