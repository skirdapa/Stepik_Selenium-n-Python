"""
https://stepik.org/lesson/165493/step/7?unit=140087
Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
Но теперь значение переменной х спрятано в "сундуке", точнее,
значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.



Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
"""
import time

from selenium import webdriver
import math


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser.get(link)
    time.sleep(2)
    treasure = browser.find_element_by_css_selector("#treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    answer_input = browser.find_element_by_css_selector("#answer")
    answer_input.send_keys(str(y))
    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    robot_checkbox.click()
    robot_radiobutton = browser.find_element_by_css_selector("#robotsRule")
    robot_radiobutton.click()
    button_submit = browser.find_element_by_css_selector("button[type=submit]")
    button_submit.click()
    # Переключаемся на высплывающее сообщение - алерт, и выводим его текст в консоль
    alert = browser.switch_to.alert
    print(alert.text)
finally:
    time.sleep(5)
    browser.quit()
