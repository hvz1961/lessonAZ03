import pandas as pd
import matplotlib.pyplot as plt

# Загрузите данные из CSV файла
data = pd.read_csv('prices_cleaned.csv')

# Предположим, что колонка с ценами называется 'price'
# Если название колонки другое, измените 'price' на нужное название
prices = data['Price']

# Построить гистограмму
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=30, color='blue', edgecolor='black')
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()
