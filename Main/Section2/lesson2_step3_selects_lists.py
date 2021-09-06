"""
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота,
чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.



Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html.
Ваш код и для нее тоже должен пройти успешно.
"""
import time

from selenium import webdriver
import math

from selenium.webdriver.support.select import Select


def calc(a, b):
    return str(int(a)+int(b))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"

try:
    browser.get(link)
    time.sleep(1)
    num1 = browser.find_element_by_css_selector("#num1")
    num2 = browser.find_element_by_css_selector("#num2")
    summa = calc(num1.text, num2.text)
    # Пользуемся элементом select из библиотеки селениума, для работы с выпадающими списками
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(summa)

    button_submit = browser.find_element_by_css_selector("button[type=submit]")
    button_submit.click()
    # Переключаемся на высплывающее сообщение - алерт, и выводим его текст в консоль
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
finally:
    time.sleep(5)
    browser.quit()
