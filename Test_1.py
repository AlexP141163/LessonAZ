import csv
import numpy as np
import matplotlib.pyplot as plt

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