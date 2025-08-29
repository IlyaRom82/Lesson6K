import threading
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.edge
def test_form_highlight_edge():
    driver = webdriver.Edge()  # Убедитесь, что msedgedriver в PATH
    wait = WebDriverWait(driver, 10)

    try:
        (driver.get
         ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
         )

        valid_data = {
            "first-name": "Ivan",
            "last-name": "Ivanov",
            "address": "Lenina 1",
            "e-mail": "ivan@example.com",
            "phone": "+79990001122",
            "city": "Moscow",
            "country": "Russia",
            "job-position": "QA Engineer",
            "company": "Company"
        }

        # Подсветка зелёным для валидных полей
        for name, value in valid_data.items():
            field = wait.until(EC.presence_of_element_located((By.NAME, name)))
            field.clear()
            field.send_keys(value)
            driver.execute_script(f"""
                var field = document.getElementsByName('{name}')[0];
                field.style.border = '2px solid green';
                setTimeout(function() {{ field.style.border = ''; }}, 5000);
            """)

        # Подсветка красным для zip
        zip_field = (wait.until
                     (EC.presence_of_element_located((By.NAME, "zip-code")))
                     )
        zip_field.clear()
        zip_field.send_keys("abc")
        driver.execute_script("""
            var field = arguments[0];
            field.style.border = '2px solid red';
            setTimeout(function() { field.style.border = ''; }, 5000);
        """, zip_field)

        # Жмём Validate
        submit_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_btn.click()

        # Автоматическое закрытие через 6 секунд
        threading.Timer(6, lambda: driver.quit()).start()

    except Exception as e:
        driver.quit()
        raise e
