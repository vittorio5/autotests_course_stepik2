from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import pytest
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page_number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_stepik_authorization(browser, page_number):
    browser.get(f"https://stepik.org/lesson/{page_number}/step/1")
    # находим кнопку "Войти" и кликаем её
    login_btn = browser.find_element(By.LINK_TEXT, "Войти")
    login_btn.click()
    # находим поле логина и вносим в него адрес почты
    email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_email"))
    )
    email.send_keys("***************")
    # находим поле пароля и вносим в него пароль
    passwrd = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_password"))
    )
    passwrd.send_keys("**********")
    # заходим на сайт
    enter = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    enter.click()
    time.sleep(2)
    # проверяем наличие кнопки "Решить снова" и жмём её, если она есть    
    try:
        solve_again = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".again-btn")))
        solve_again.click()
        ok_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'OK')]")))
        ok_btn.click()
    
    except TimeoutException:
        print('Всё нормально, старых решений нет')

    finally:
        time.sleep(2)
        # находим поле для ввода ответа
        answer_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area"))
        )
        # # очищаем поле ввода ответа
        # answer_field.clear()
        # вычисляем ответ по формуле
        answer = math.log(int(time.time()))
        # пишем ответ в поле
        answer_field.send_keys(answer)
        # находим кнопку отправки ответа и кликаем её
        answer_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        answer_btn.click()
        # находим поле с сообщением берем оттуда текст
        message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints"))
        )
        assert message.text == "Correct!", f"Текст для запоминания: {message}"

