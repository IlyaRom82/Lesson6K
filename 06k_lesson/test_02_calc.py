import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.mark.chrome
def test_slow_calculator_chrome():
    # Опции для Chrome (по желанию)
    options = Options()
    options.add_argument("--start-maximized")  # сразу во весь экран
    # options.add_argument("--headless")  # если нужно без окна

    # Если chromedriver у тебя прописан в PATH, Service можно не указывать
    driver = webdriver.Chrome(options=options)

    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
     )

    try:
        # Установим задержку 45 секунд
        delay_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки 7 + 8 =
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
        ).click()

        # Проверяем, что через 45 секунд результат = 15
        result = WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15")
        )
        assert result, "❌ Результат калькулятора не равен 15"

    finally:
        driver.quit()
