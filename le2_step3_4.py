from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find button
    browser.find_element(By.CSS_SELECTOR, "button.btn") .click()

    # tap confirm in modal
    confirm = browser.switch_to.alert
    confirm.accept()

    # находим елемент со значение для Х
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    
    # находим поле ввода и вставляем
    inputA = browser.find_element(By.ID, "answer")
    inputA.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn") .click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
