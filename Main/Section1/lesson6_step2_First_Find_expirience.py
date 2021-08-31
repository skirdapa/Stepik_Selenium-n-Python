"""
Поиск элементов с помощью селениум
https://stepik.org/lesson/138920/step/2?unit=196194
"""
# Первый способ
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element_by_id("submit_button")

# Второй способ
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

# Что бы браузер не оставался открытым из за ошибок, можно использовать конструкцию try - finally
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element(By.ID, "submit_button")
    time.sleep(2)
    button.click()
finally:
    # Нужно всегда закрывать браузер, иначе он стается в оперативной памяти даже после закрытия окна вручную
    time.sleep(5)
    browser.quit()
