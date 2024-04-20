import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV limpio
file_path = '/home/brandon/PycharmProjects/ECommerceScrapingTool/data/cleaned_products.csv'
df = pd.read_csv(file_path)

# Inspección inicial de los datos
print(df.head())  # Muestra las primeras filas para verificar la carga de datos
print(df.describe())  # Estadísticas descriptivas de los datos numéricos

# Precios promedio por fabricante, ordenados de menor a mayor
average_prices = df.groupby('manufacturer')['price'].mean().sort_values()
print("Precio promedio por fabricante ordenado:")
print(average_prices)

# Contar el número de productos por fabricante
print("Conteo de productos por fabricante:")
print(df['manufacturer'].value_counts())

# Los 5 productos más caros
print("Los 5 productos más caros:")
print(df.nlargest(5, 'price')[['manufacturer', 'title', 'price']])

# Los 5 productos más baratos
print("Los 5 productos más baratos:")
print(df.nsmallest(5, 'price')[['manufacturer', 'title', 'price']])

# Histograma de precios
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, color='blue', alpha=0.7)
plt.title('Distribución de Precios de Productos')
plt.xlabel('Precio (£)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Boxplot de precios por fabricante para visualizar la dispersión y los outliers, ordenados por el precio promedio
sorted_manufacturers = average_prices.index.tolist()
sorted_df = df.set_index('manufacturer').loc[sorted_manufacturers].reset_index()
plt.figure(figsize=(12, 8))
sorted_df.boxplot(column='price', by='manufacturer', grid=True)
plt.title('Boxplot de Precios por Fabricante Ordenado')
plt.xlabel('Fabricante')
plt.ylabel('Precio (£)')
plt.xticks(rotation=45)
plt.show()



