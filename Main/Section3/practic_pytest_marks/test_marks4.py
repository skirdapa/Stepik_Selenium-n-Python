"""
https://stepik.org/lesson/236918/step/5?unit=209305
XFail: помечать тест как ожидаемо падающий
если он неожиданно пройдет, то будет помечен xpassed - неожиданно прошедший
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

    @pytest.mark.xfail(reason="Бага, чинят")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")
