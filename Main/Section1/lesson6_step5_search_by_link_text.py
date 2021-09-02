"""
https://stepik.org/lesson/138920/step/5?unit=196194
Задание: поиск элемента по тексту в ссылке
В этой задаче мы попробуем искать элементы по тексту ссылки, для этого воспользуемся методом find_element_by_link_text:

link = browser.find_element_by_link_text(text)
В качестве аргумента в метод передается такой текст, ссылку с которым мы хотим найти. Это тот самый текст, который содержится между открывающим и закрывающим тегом <a> вот тут </a>

Допустим, на странице https://www.degreesymbol.net/ мы хотим найти ссылку с текстом "Degree symbol in Math" и перейти по ней. Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код:

link = browser.find_element_by_link_text("Degree Symbol in Math")
link.click()
А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:

link = browser.find_element_by_partial_link_text("Math")
link.click()
Обычно поиск по подстроке чуть более удобный и гибкий, но с ним надо быть вдвойне аккуратными и проверять, что находится нужный элемент.

Задание
На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

Добавьте в самый верх своего кода import math
Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
str(math.ceil(math.pow(math.pi, math.e)*10000))
(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде)

Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации

Заполните скриптом форму так же как вы делали в предыдущем шаге урока

После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
Важно! Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются реже, чем атрибуты элементов. Но лучше избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса, ваши тесты будут проходить только с определенным языком интерфейса. Применяйте этот метод с осторожностью и помните про возможные ограничения.

Читать больше:

https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text
"""
import math
from selenium import webdriver
import time

from Main.Section1.lesson6_step4_Selenium_search import fill_inputs

link_start = 'http://suninjuly.github.io/find_link_text'
link_encrypt = str(math.ceil(math.pow(math.pi, math.e) * 10000))


# def fill_inputs(local_browser):
#     input1 = local_browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = local_browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = local_browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = local_browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = local_browser.find_element_by_css_selector("button.btn")
#     button.click()


try:
    browser = webdriver.Chrome()
    browser.get(link_start)
    time.sleep(2)
    link = browser.find_element_by_link_text(link_encrypt)
    link.click()
    time.sleep(1)
    fill_inputs(browser)

finally:
    time.sleep(10)
    browser.quit()
