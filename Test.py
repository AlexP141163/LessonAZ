import pandas as pd
import matplotlib.pyplot as plt

# Данные оценок
data = {
    'name': ['Наташа', 'Александр', 'Николай', 'Сергей', 'Оля', 'Нина', 'Тимофей', 'Анатолий', 'Ирина', 'Елена'],
    'Mathematics': [3, 5, 3, 4, 5, 3, 4, 3, 5, 4],
    'Geometry': [3, 4, 4, 3, 5, 4, 5, 3, 4, 3],
    'Chemistry': [4, 4, 3, 4, 5, 5, 4, 3, 3, 5],
    'History': [4, 5, 5, 4, 3, 4, 4, 5, 5, 4],
    'Biology': [3, 4, 5, 4, 3, 4, 3, 3, 4, 3]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Вычисление средних оценок по каждому предмету
subject_means = df.loc[:, 'Mathematics':'Biology'].mean()

# Вычисление средних оценок каждого ученика по всем предметам
df['Average'] = df.loc[:, 'Mathematics':'Biology'].mean(axis=1)

# Визуализация средних оценок по предметам
plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)
subject_means.plot(kind='bar', color='skyblue')
plt.title('Средние оценки по предметам')
plt.ylabel('Средняя оценка')
plt.xlabel('Предмет')
plt.xticks(rotation=45)
plt.ylim(0, 5)

# Визуализация средних оценок каждого ученика
plt.subplot(1, 2, 2)
df.sort_values('Average', inplace=True)
plt.bar(df['name'], df['Average'], color='lightgreen')
plt.title('Средние оценки каждого ученика')
plt.ylabel('Средняя оценка')
plt.xlabel('Имя ученика')
plt.xticks(rotation=90)
plt.ylim(0, 5)

# Отображение графиков
plt.tight_layout()
plt.show()