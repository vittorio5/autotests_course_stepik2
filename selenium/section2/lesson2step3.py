from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return str(int(x) + int(y))

try: 
    # link = "https://suninjuly.github.io/selects1.html"
    link = "https://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    sum = calc(num1, num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
