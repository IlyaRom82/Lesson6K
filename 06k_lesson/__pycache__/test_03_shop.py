# PR placeholder: ничего не меняем, просто для отображения измененийgit add .
import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

def test_shop_total():
    # Путь к geckodriver
    gecko_path = r"C:\Users\ontar\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe"
    service = Service(gecko_path)

    # Настройки Firefox
    options = Options()
    options.headless = False  # для отладки
    browser = webdriver.Firefox(service=service, options=options)

    try:
        browser.set_page_load_timeout(180)  # таймаут на загрузку страницы
        wait = WebDriverWait(browser, 60)   # явные ожидания до 60 секунд

        url = "https://www.saucedemo.com/"

        # Retry открытия страницы
        for attempt in range(3):
            try:
                browser.get(url)
                break
            except Exception as e:
                print(f"Попытка {attempt+1} не удалась: {e}")
                time.sleep(10)
        else:
            pytest.fail("Не удалось открыть сайт после 3 попыток")

        # Авторизация
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        browser.find_element(By.ID, "login-button").click()

        # Добавляем товары
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Переходим в корзину
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # Заполняем форму
        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
        browser.find_element(By.ID, "last-name").send_keys("Иванов")
        browser.find_element(By.ID, "postal-code").send_keys("123456")
        browser.find_element(By.ID, "continue").click()

        # Проверяем итоговую сумму
        total_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
        assert total_text == "Total: $58.29", f"Итоговая сумма неверная: {total_text}"

    finally:
        browser.quit()

