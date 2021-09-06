"""
browser.switch_to.window(window_name)
Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]
Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]
https://stepik.org/lesson/184253/step/6?unit=158843
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку
и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""
import math
from selenium import webdriver
import time
import os


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    submit_button = browser.find_element_by_css_selector("button[type=submit]")
    submit_button.click()  # Сссылка откроется в новом окне
    new_window_name = browser.window_handles[1]  # Получаем имено нового окна
    print(new_window_name)
    browser.switch_to.window(new_window_name)

    x_text = browser.find_element_by_css_selector("#input_value").text
    y = calc(x_text)

    answer_input = browser.find_element_by_css_selector("#answer")
    answer_input.send_keys(str(y))

    submit_button = browser.find_element_by_css_selector("button[type=submit]")
    submit_button.click()
    alert_code = browser.switch_to.alert.text.split()[-1]
    print(alert_code)

finally:
    time.sleep(1)
    browser.quit()
