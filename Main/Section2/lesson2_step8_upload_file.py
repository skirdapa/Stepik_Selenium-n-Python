"""
https://stepik.org/lesson/228249/step/8?unit=200781
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа
для этого задания.
"""
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element_by_css_selector("[name=firstname]")
    first_name.send_keys("Джон")
    last_name = browser.find_element_by_css_selector("[name=lastname]")
    last_name.send_keys("Рэмбо")
    email = browser.find_element_by_css_selector("[name=email]")
    email.send_keys("first@blood.org")
    upload_file_element = browser.find_element_by_css_selector("#file")
    # Получаем адрес текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Добавляем к ней имя файла
    file_path = os.path.join(current_dir, "some_file.txt")
    # отправляем
    upload_file_element.send_keys(file_path)
    submit_button = browser.find_element_by_css_selector("button[type=submit]")
    submit_button.click()
    # time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])

finally:
    time.sleep(5)
    browser.quit()
