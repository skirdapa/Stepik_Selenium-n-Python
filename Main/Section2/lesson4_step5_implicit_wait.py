"""
https://stepik.org/lesson/181384/step/5?unit=156009
Неявное ожидание
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)  # Будем ждать появление элемента до 5 секунд

try:
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.find_element_by_css_selector("#verify").click()
    message = browser.find_element_by_css_selector("#verify_message")
    assert 'successful' in message.text
finally:
    browser.quit()
