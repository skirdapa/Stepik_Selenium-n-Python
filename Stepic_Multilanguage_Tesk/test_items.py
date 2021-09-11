from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestFindAddToBasketButton:
    def test_guest_should_see_add_to_basket_button_pass(self, browser):
        browser.get(link)
        status = "Ok"  # Вводим переменную статус, что бы наш assert сработал в случае, если элемент не найден
        try:  # Пробуем найти элемент
            browser.find_element_by_css_selector(".btn-add-to-basket")
        except NoSuchElementException as e:  # Ловим исключение если не найден
            status = e.msg  # Сообщение об ошибке помещаем в статус
        finally:
            # Проверяем всё ли ок? Найден ли элемент?
            # Если да, то тест пройден, если нет, то выводим свой текст ошибки
            assert status == "Ok", f"Не смогли найти корзину :( Получили ошибку:{status}"

    def test_guest_should_see_add_to_basket_button_fail(self, browser):
        browser.get(link)
        status = "Ok"  # Вводим переменную статус, что бы наш assert сработал в случае, если элемент не найден
        try:  # Пробуем найти элемент
            browser.find_element_by_css_selector(".btn-add-to-basket-does-not-exist")
        except NoSuchElementException as e:  # Ловим исключение если не найден
            status = e.msg  # Сообщение об ошибке помещаем в статус
        finally:
            # Проверяем всё ли ок? Найден ли элемент?
            # Если да, то тест пройден, если нет, то выводим свой текст ошибки
            assert status == "Ok", f"Не смогли найти корзину :( Получили ошибку:{status}"
