import pandas as pd

df = pd.read_csv('cleaned.csv')
df_dz = pd.read_csv('dz.csv')
group = df_dz.groupby('City')['Salary'].mean()

print(df.head())
print('______________________________________')
print(df.describe())
print('______________________________________')
print(df.info())
print('_____________________________________')
print(group)