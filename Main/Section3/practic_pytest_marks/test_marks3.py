"""
https://stepik.org/lesson/236918/step/4?unit=209305
В PyTest есть стандартные метки, которые позволяют пропустить тест при сборе тестов для запуска
(то есть не запускать тест) или запустить, но отметить особенным статусом тот тест,
который ожидаемо упадёт из-за наличия бага, чтобы он не влиял на результаты прогона всех тестов.
Эти метки не требуют дополнительного объявления в pytest.ini.

Пропустить тест

Итак, чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip

Если маркировка skip добавляется к функции, где уже есть другие маркировки, то skip должен быть последним маркером,
иначе пропускаться не будет.
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

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        # этот тест будет пропущен из за маркировки
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
