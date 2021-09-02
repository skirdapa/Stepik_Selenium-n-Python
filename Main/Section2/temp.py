import time

from selenium import webdriver
browser = webdriver.Chrome()
# browser.execute_script("document.title='Новый заголовок';alert('Robots at work');")

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    time.sleep(1)
    # Если проскроллить к элементу то ошибки, что кнопка перекрыта футером - не будет
    # JS
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Selenium, метод возвращает словарь с координатами элемента
    # _ = button.location_once_scrolled_into_view
    button.click()
finally:
    time.sleep(5)
    browser.quit()
