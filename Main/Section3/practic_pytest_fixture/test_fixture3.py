"""
https://stepik.org/lesson/237257/step/4?unit=209645

Явно закроем браузер. Финализаторы
"""

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nЗапускаем браузер")
    browser = webdriver.Chrome()
    yield browser
    print("\nВсе сделали, закрываем бразуер")
    browser.quit()


class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")