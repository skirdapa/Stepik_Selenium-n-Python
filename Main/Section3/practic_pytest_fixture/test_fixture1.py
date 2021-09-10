"""
Фикстуры юниттеста вида, запускаешиеся для классов или методов
https://stepik.org/lesson/237257/step/2?unit=209645
https://docs.pytest.org/en/latest/how-to/xunit_setup.html?highlight=teardown
"""

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nЗапускаем браузер для тестового комплекта")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\nЗакрываем браузер для тестового комплекта")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("\nЗапускаем браузер для второго тестового комплекта")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\nЗакрываем браузер для второго комплекта")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")