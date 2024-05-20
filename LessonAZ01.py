import pandas as pd

df = pd.read_csv('cleaned.csv')
df_dz = pd.read_csv('dz.csv')
group = df_dz.groupby('City')['Salary'].mean()

print(df.head())   # Вывод 5 строк:
print('______________________________________')
print(df.describe())  # Вывод статистического описания:
print('______________________________________')
print(df.info())  # Вывод информации о данных:
print('_____________________________________')
print(group)   # Вывод средних зарплат по городам: