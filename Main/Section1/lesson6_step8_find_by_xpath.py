"""
https://stepik.org/lesson/138920/step/8?unit=196194
Задание: поиск элемента по XPath
На этот раз воспользуемся возможностью искать элементы по XPath.

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3,
при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit",
и наша задача нажать в коде именно на неё.

Ваши шаги:

В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit.
XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
Запустите ваш код.
Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код,
который нужно отправить в качестве ответа на это задание.
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
    button = local_browser.find_element_by_xpath("//button[@type='submit']")
    button.click()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/find_xpath_form"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fill_inputs(browser)
        alert = browser.switch_to.alert
        print(alert.text)
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла
