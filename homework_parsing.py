from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome()
url = "https://www.divan.ru/category/divany"
driver.get(url)
time.sleep(5)
# Находим элементы с ценами
price_elements = driver.find_elements(By.CLASS_NAME, 'pY3d2')

# Извлекаем текст цен
prices = [price.text for price in price_elements]

# Записываем цены в CSV файл
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок
    for price in prices:
        writer.writerow([price])

# Закрываем драйвер
driver.quit()


