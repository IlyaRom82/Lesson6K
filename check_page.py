import requests

url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
try:
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        print("Страница доступна")
    else:
        print(f"Страница недоступна, статус код: {r.status_code}")
except Exception as e:
    print(f"Ошибка при доступе к странице: {e}")
