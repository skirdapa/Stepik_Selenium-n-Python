"""
https://stepik.org/lesson/228249/step/6?unit=200781
Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script,
чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
"""
import time

from selenium import webdriver
import math


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    time.sleep(1)
    x_element = browser.find_element_by_css_selector("#input_value")
    y = calc(x_element.text)
    answer_input = browser.find_element_by_css_selector("#answer")
    answer_input.send_keys(str(y))
    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    robot_checkbox.click()
    # находим и скроллим к ней методом из селениума, он возвращает координаты элемента и скроллит до них
    robot_radiobutton = browser.find_element_by_css_selector("#robotsRule")
    _ = robot_radiobutton.location_once_scrolled_into_view
    print(robot_radiobutton)
    robot_radiobutton.click()
    button_submit = browser.find_element_by_css_selector("button[type=submit]")
    # скроллим к найденной кнопки с помощью скрипта JS
    browser.execute_script("return arguments[0].scrollIntoView();", button_submit)
    button_submit.click()
    # Переключаемся на высплывающее сообщение - алерт, и выводим его текст в консоль
    alert = browser.switch_to.alert
    # Разибиваем текст на массив, элементы разделены пробелами, выбираем последний элемент
    print(alert.text.split()[-1])
finally:
    time.sleep(5)
    browser.quit()
