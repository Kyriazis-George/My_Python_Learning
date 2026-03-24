import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r'c:\Users\kyria\Desktop\Data Analysis Projects\Coffee Sales\index_2.csv')

#Index(['date', 'datetime', 'cash_type', 'money', 'coffee_name'], dtype='object')

# print(df.columns)

# print(df.isnull().sum())

top_products = df.groupby('coffee_name')['money'].sum().sort_values(ascending=False).head(5)
# print(top_products)

sales_by_cash = df.groupby('cash_type')['money'].sum()
# print(sales_by_cash)

df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)

df['date'] = pd.to_datetime(df['date'], dayfirst=True)
daily_sales = df.groupby('date')['money'].sum()
# print(daily_sales)

# sns.barplot(x=top_products.index, y=top_products.values)
# plt.title("Total Sales per category")
# plt.ylabel("Sales($)")
# plt.xlabel("Product Category")
# plt.show()

# sns.barplot(x=sales_by_cash.index, y=sales_by_cash.values)
# plt.title("Sales per payment")
# plt.ylabel("Number of sales")
# plt.xlabel("Product category")
# plt.show()

#Heatmap number of sales per Product per date
# sales_matrix = df.groupby(['date','cash_type'])['money'].sum().unstack()

# sns.heatmap(sales_matrix, annot=True, fmt=".0f", cmap="YlGnBu")
# plt.title("Payment Category per Date")
# plt.show()


