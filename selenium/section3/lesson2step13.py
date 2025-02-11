import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RegistrationTest(unittest.TestCase):
    def test_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_class input[required]")
        first_name.send_keys("Мой ответ")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.second_class input[required]")
        last_name.send_keys("Мой ответ")
        email = browser.find_element(By.CSS_SELECTOR, "div.third_class input[required]")
        email.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test_second_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_class input[required]")
        first_name.send_keys("Мой ответ")
        last_name = browser.find_element(By.CSS_SELECTOR, "div.second_class input[required]")
        last_name.send_keys("Мой ответ")
        email = browser.find_element(By.CSS_SELECTOR, "div.third_class input[required]")
        email.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
