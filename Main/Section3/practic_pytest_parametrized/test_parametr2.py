"""
Задание: параметризация тестов
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
Ваша задача — реализовать автотест со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

Правильным ответом на задачу в заданных шагах является число:

import time
import math

answer = math.log(int(time.time()))
Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания,
чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает
со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время
(https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.
"""
import math
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def get_answer():
    return str(math.log(int(time.time())))


class TestFindAlienMessage:

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                      'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1',
                                      'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1',
                                      'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1',
                                      'https://stepik.org/lesson/236905/step/1'])
    def test_correct_answer_in_stepic_page(self, browser, link):
        browser.get(link)
        input_answer = WebDriverWait(browser, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ember-text-area"))
        )
        input_answer.send_keys(get_answer())
        button_submit = WebDriverWait(browser, 20).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button_submit.click()
        smart_hints_text = WebDriverWait(browser, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        ).text

        assert smart_hints_text == "Correct!", "Текст ответа отличается"
