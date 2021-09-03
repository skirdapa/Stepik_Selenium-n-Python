"""
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""
import math
from selenium import webdriver
import time
import os


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    submit_button = browser.find_element_by_css_selector("button[type=submit]")
    submit_button.click()
    # Подтверждаем переход
    browser.switch_to.alert.accept()

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
