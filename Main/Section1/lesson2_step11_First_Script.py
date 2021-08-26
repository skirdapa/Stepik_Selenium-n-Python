"""
Запуск браузера и первый скрипт
https://stepik.org/lesson/25969/step/11?unit=196192
"""

import time

#  webdriver - это и есть набор команд для управления браузеров
from selenium import webdriver

#  инициализируем драйвер браузера. После этой команды открывается окно браузера
driver = webdriver.Chrome()


# С помощью метода  get перейдем на нужную страницу
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Найдем поле для ввода текста с помощью css селектора
textarea = driver.find_element_by_css_selector(".textarea")
time.sleep(5)

# Запишем текст ответа в поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем браузеру, что бы нажал на кнопку.
submit_button.click()
time.sleep(5)

# закрываем браузер

time.sleep(5)
driver.quit()
