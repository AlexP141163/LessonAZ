import numpy as np
import matplotlib.pyplot as plt

# Генерация двух массивов из 50 случайных чисел каждый
x = np.random.rand(15)
print(x)
y = np.random.rand(15)
print(y)

# Создание диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.6)  # alpha управляет прозрачностью точек
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X координаты')
plt.ylabel('Y координаты')
plt.grid(True)
plt.show()