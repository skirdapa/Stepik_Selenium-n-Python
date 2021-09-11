"""
https://stepik.org/lesson/237240/step/7?unit=209628
Один тест будет падать, другой проходить. Нужно для демонстрации плагина pytest-rerunfailures,
который перезапускает упавшие тесты заданное количество раз
"""

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector('#magic_link')
