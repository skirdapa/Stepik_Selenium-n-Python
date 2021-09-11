"""
https://stepik.org/lesson/236918/step/3?unit=209305
Метки можно комбинировать использую логический операторы

pytest -s -v -m "not smoke" test_fixture8.py - запустятся все кроме smoke

pytest -s -v -m "smoke or regression" test_fixture8.py - запустятся и smoke и regression

pytest -s -v -m "smoke and win10" test_fixture81.py - запустятся только промаркированные двумя метками
"""
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nЗапускаем бразуер..")
    browser = webdriver.Chrome()
    yield browser
    print("\nЗакрываем браузер..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
