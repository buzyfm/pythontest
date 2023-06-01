import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    # находим елемент со значение для Х
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    # находим поле ввода и вставляем
    inputA = browser.find_element(By.ID, "answer")
    inputA.send_keys(y)
    browser.find_element(By.ID, "solve") .click()

finally:
    # берем текст из модалки и выводим в консоль
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()