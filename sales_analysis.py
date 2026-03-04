import pandas as pd
import matplotlib.pyplot as plt

# Данные продаж
data = {
    "Month": ["Январь", "Февраль", "Март", "Апрель", "Май"],
    "Sales": [1500, 1800, 2200, 2000, 2500]
}

# Создаем таблицу
df = pd.DataFrame(data)

# Вывод данных
print("Данные продаж:")
print(df)

# Средние продажи
average_sales = df["Sales"].mean()
print("\nСредние продажи:", average_sales)

# Максимальные продажи
max_sales = df["Sales"].max()
print("Максимальные продажи:", max_sales)

# Построение графика
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Продажи по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Продажи")
plt.grid(True)

# Сохранение графика
plt.savefig("sales_chart.png")

plt.show()