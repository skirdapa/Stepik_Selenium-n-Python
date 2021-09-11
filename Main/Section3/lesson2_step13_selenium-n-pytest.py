"""
https://stepik.org/lesson/36285/step/13?unit=162401
Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте.
Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё.
Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK1 = "http://suninjuly.github.io/registration1.html"
LINK2 = "http://suninjuly.github.io/registration2.html"
FIRST_NAME_SELECTOR = "div.first_block input.first"
LAST_NAME_SELECTOR = "div.first_block input.second"
EMAIL_SELECTOR = "div.first_block input.third"
BUTTON_SUBMIT_SELECTOR = "button.btn"
WELCOME_TEXT_SELECTOR = "h1"


class TestRegistration(unittest.TestCase):

    def test_registration_1(self, link=LINK1):
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_css_selector(FIRST_NAME_SELECTOR).send_keys("Джон")
        browser.find_element_by_css_selector(LAST_NAME_SELECTOR).send_keys("Сноу")
        browser.find_element_by_css_selector(EMAIL_SELECTOR).send_keys("j.snow@gameofthrone.cinema")
        browser.find_element_by_css_selector(BUTTON_SUBMIT_SELECTOR).click()
        welcome_text = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, WELCOME_TEXT_SELECTOR))
        )
        self.assertEqual(welcome_text.text, "Congratulations! You have successfully registered!",
                         "Welcome text is not expected")
        browser.quit()

    def test_registration_2(self, link=LINK2):
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_css_selector(FIRST_NAME_SELECTOR).send_keys("Джон")
        browser.find_element_by_css_selector(LAST_NAME_SELECTOR).send_keys("Сноу")
        browser.find_element_by_css_selector(EMAIL_SELECTOR).send_keys("j.snow@gameofthrone.cinema")
        browser.find_element_by_css_selector(BUTTON_SUBMIT_SELECTOR).click()
        welcome_text = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, WELCOME_TEXT_SELECTOR))
        )

        self.assertEqual(welcome_text.text, "Congratulations! You have successfully registered!",
                         "Welcome text is not expected")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
