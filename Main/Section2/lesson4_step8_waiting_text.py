"""
https://stepik.org/lesson/181384/step/8?unit=156009
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Main.repeat_code import calc_stepic_formula, print_code_into_console

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element_by_id("book")
    book_button.click()
    input_value = browser.find_element_by_id("input_value")
    answer = calc_stepic_formula(input_value.text)
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_id("solve").click()
    print_code_into_console(browser)
finally:
    browser.quit()
