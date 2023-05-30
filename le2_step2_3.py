from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим елементы с числами и переводим в текст
    num1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']").text
    num2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']").text

    # считаем сумму, переводя каждую строку в число, а потом обратно в строку
    x = str(int(num1) + int(num2))

    # находим поле ввода и вставляем
    select = Select(browser.find_element(By.CSS_SELECTOR, "[id='dropdown']"))
    select.select_by_value(x)

    browser.find_element(By.CSS_SELECTOR, "button.btn") .click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
