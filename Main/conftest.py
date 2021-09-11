from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Выберите браузер: chrome или firefox")
    parser.addoption('--language', action='store', default='ru',
                     help='Выберите язык: ru, en и тд.')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("Запускаем Chrome браузер...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("Запускаем Firefox браузер...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--Браузер может быть только Chrome или Firefox")
    yield browser
    print("...закрываем браузер")
    browser.quit()
