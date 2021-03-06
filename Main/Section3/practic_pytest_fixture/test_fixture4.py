"""
https://stepik.org/lesson/237257/step/5?unit=209645
Область видимости scope
Для фикстур можно задавать область покрытия фикстур. Допустимые значения: “function”, “class”, “module”, “session”.
Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса,
один раз для модуля или один раз для всех тестов, запущенных в данной сессии.

Запустим все наши тесты из класса TestMainPage1 в одном браузере для экономии времени, задав scope="class"
в фикстуре browser
в данном примере браузер открылся один раз и тесты последовательно выполнились в этом браузере.
Здесь мы проделали это в качестве примера, но мы крайне рекомендуем всё же запускать отдельный экземпляр браузера
для каждого теста, чтобы повысить стабильность тестов. Фикстуры, которые занимают много времени
для запуска и ресурсов (обычно это работа с базами данных), можно вызывать и один раз за сессию запуска тестов.
"""

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")