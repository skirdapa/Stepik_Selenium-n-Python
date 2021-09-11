"""
https://stepik.org/lesson/236918/step/2?unit=209305
Маркировка тестов часть 1
Когда тестов становится много, хорошо иметь способ разделять тесты не только по названиям,
но также по каким-нибудь заданным нами категориям.

Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:

pytest -s -v -m smoke test_fixture8.py

Как же регистрировать метки?
Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
Текст после знака ":" является поясняющим — его можно не писать.
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

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
