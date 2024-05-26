from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import matplotlib.pyplot as plt
import time
import csv

# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
driver = webdriver.Firefox()
#driver = webdriver.Firefox()

# URL страницы
url = 'https://divan.ru/category/divany-i-kresla'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()

def parse_price(price_str):
    # Удаление всех нечисловых символов
    cleaned_str = ''.join(filter(str.isdigit, price_str))
    # Преобразование строки в число
    return int(cleaned_str)

# Путь к файлу CSV для чтения
filename = 'prices.csv'

# Путь к файлу CSV для записи
output_filename = 'clean_prices.csv'

# Список для хранения очищенных и преобразованных цен
parsed_prices = []

# Чтение данных из CSV файла
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок, если он есть
    for row in reader:
        if row:  # Проверяем, не пустая ли строка
            price = parse_price(row[0])  # Предполагаем, что цена находится в первом столбце
            parsed_prices.append(price)

# Запись очищенных данных в новый CSV файл
with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Cleaned Price'])  # Записываем заголовок столбца
    for price in parsed_prices:
        writer.writerow([price])  # Записываем каждую цену как строку в CSV

# Найдем среднюю цену на диваны и выведем гистограмму цен на диваны:

# Путь к файлу CSV для чтения
filename = 'clean_prices.csv'

# Список для хранения цен
prices = []

# Чтение данных из CSV файла
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        if row:  # Проверяем, не пустая ли строка
            price = int(row[0])
            prices.append(price)

# Вычисление средней цены
average_price = np.mean(prices)
print(f"Средняя цена: {average_price:.2f} руб.")

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='blue', alpha=0.7)
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(True)
plt.show()