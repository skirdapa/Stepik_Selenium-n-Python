"""
https://stepik.org/lesson/237240/step/2?unit=209628
В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра.
В самом тесте наш параметр тоже нужно передавать в качестве аргумента. Обратите внимание,
что внутри декоратора имя параметра оборачивается в кавычки, а в списке аргументов теста кавычки не нужны.

Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе
запустились с заданными параметрами. В таком случае отметка о параметризации должна быть перед объявлением класса
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nЗапускаем браузер для теста..")
    browser = webdriver.Chrome()
    yield browser
    print("\nзакрываем браузер..")
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestPythonEwerywhereMainPage:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_another_test(self, language):
        pass
