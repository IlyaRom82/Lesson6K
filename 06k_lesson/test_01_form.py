# PR placeholder: ничего не меняем, просто для отображения изменений
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.edge
def test_form_validation_edge():
    # Создаем экземпляр Edge
    driver = webdriver.Edge()  # msedgedriver должен быть в PATH

    try:
        # Открываем страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        # Ждем, пока DOM загрузится
        wait = WebDriverWait(driver, 10)
        (wait.until
         (EC.presence_of_element_located((By.TAG_NAME, "body")))
         )

        # Заполняем поля формы
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "first-name"))).send_keys("Иван")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "last-name"))).send_keys("Иванов")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "address"))).send_keys("ул. Ленина, 1")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "zip-code"))).send_keys("123456")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "city"))).send_keys("Москва")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "country"))).send_keys("Россия")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "e-mail"))).send_keys("ivan@example.com")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "phone"))).send_keys("+79990001122")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "job-position"))).send_keys("Тестировщик")
         )
        (wait.until
         (EC.presence_of_element_located(
             (By.NAME, "company"))).send_keys("Компания")
         )

        # Ждем 15 секунд, чтобы увидеть заполненную страницу
        time.sleep(15)

    finally:
        driver.quit()  # закрываем браузер после паузы
