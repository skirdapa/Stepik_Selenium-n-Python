"""
https://stepik.org/lesson/138920/step/4?unit=196194
Задание: поиск элементов с помощью Selenium
Вам нужно открыть страницу по ссылке http://suninjuly.github.io/simple_form_find_task.html и заполнить форму на этой странице с помощью Selenium. Если всё сделано правильно,
то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче.

!Обратите внимание, что время для ввода данных ограничено. Однако благодаря Selenium вы сможете выполнить задачу
до того, как время истечёт.

Для решения этой задачи мы подготовили для вас шаблон кода, в который нужно только подставить нужные значения
для поиска вместо слов value1, value2 и т.д. Обратите внимание, что значения нужно заключать в кавычки, т.к.
они должны передаваться в виде строки.
"""
from selenium import webdriver
import time


def fill_inputs(local_browser):
    input1 = local_browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = local_browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = local_browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = local_browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = local_browser.find_element_by_css_selector("button.btn")
    button.click()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fill_inputs(browser)

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла
