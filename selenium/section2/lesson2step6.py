from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")
    result = browser.find_element(By.CSS_SELECTOR, "#answer")
    result.send_keys(y)

    ch_box = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    ch_box.click()
    r_button = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    r_button.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
