import pandas as pd

# Definir los nombres de las columnas
column_names = ['manufacturer', 'title', 'price']

# Cargar los datos especificando que no hay fila de encabezado y asignando nombres de columnas
df = pd.read_csv('/home/brandon/PycharmProjects/ECommerceScrapingTool/data/products.csv', header=None, names=column_names)

# Inspeccionar los datos
print(df.head())
print(df.describe())
print(df.info())

# Limpiar campo de precios, eliminando caracteres no deseados como el símbolo de libra
df['price'] = df['price'].str.replace('£', '').replace(',', '', regex=True).astype(float)

# Tratar valores faltantes
df.dropna(subset=['price'], inplace=True)  # Eliminar filas donde el precio esté faltante
df['price'] = df['price'].fillna(df['price'].median())  # Imputar el precio faltante con la mediana

# Corrección de tipos de datos ya debería estar resuelta con el paso de limpieza
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Guardar los datos limpios
df.to_csv('/home/brandon/PycharmProjects/ECommerceScrapingTool/data/cleaned_products.csv', index=False)
