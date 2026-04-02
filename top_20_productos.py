import pandas as pd
import matplotlib.pyplot as plt

# CARGAR DATOS
productos = pd.read_csv('datos/products.csv', sep=';')
ordenes_detalle = pd.read_csv('datos/order_products.csv', sep=';')

# EDA – CALIDAD DE DATOS: productos
print("=" * 50)
print("PRODUCTOS – Estructura")
print("=" * 50)
productos.info()
print()
print(productos.head())

print("\n--- Completitud (nulos) ---")
nulos_productos = productos.isna().sum().reset_index()
nulos_productos.columns = ['columna', 'qty_nulos']
nulos_productos['rate_%'] = (nulos_productos['qty_nulos'] * 100) / len(productos)
print(nulos_productos)

print("\n--- Precision (duplicados completos) ---")
print(f"Filas completamente duplicadas: {productos.duplicated().sum()}")

print(f"product_id duplicados: {productos.duplicated(subset='product_id').sum()}")

print("\n--- Consistencia – valores únicos clave ---")
print(f"Productos únicos: {productos['product_id'].nunique()}")

# Sensibilidad – no hay datos sensibles esperados en este dataset
# (product_name, aisle_id, department_id son datos de catálogo)

# EDA – CALIDAD DE DATOS: ordenes_detalle
print("\n" + "=" * 50)
print("ORDENES DETALLE – Estructura")
print("=" * 50)
ordenes_detalle.info()
print()
print(ordenes_detalle.head())

print("\n--- Completitud (nulos) ---")
nulos_detalle = ordenes_detalle.isna().sum().reset_index()
nulos_detalle.columns = ['columna', 'qty_nulos']
nulos_detalle['rate_%'] = (nulos_detalle['qty_nulos'] * 100) / len(ordenes_detalle)
print(nulos_detalle)

print("\n--- Precision (duplicados completos) ---")
print(f"Filas completamente duplicadas: {ordenes_detalle.duplicated().sum()}")

dup_orden_producto = ordenes_detalle.duplicated(subset=['order_id', 'product_id']).sum()
print(f"Duplicados (order_id + product_id): {dup_orden_producto}")

print("\n--- Consistencia – add_to_cart_order negativos o cero ---")
print(ordenes_detalle[ordenes_detalle['add_to_cart_order'] <= 0].shape[0])


# LIMPIEZA (si aplica)
productos.drop_duplicates(inplace=True)
ordenes_detalle.drop_duplicates(inplace=True)

# MERGE – unir ordenes con productos
ordenes_full = ordenes_detalle.merge(productos, on='product_id', how='inner')

print("\n" + "=" * 50)
print("TABLA UNIFICADA (ordenes_full)")
print("=" * 50)
print(ordenes_full.shape)
print(ordenes_full.head())
# TOP 20 PRODUCTOS MÁS COMPRADOS

top_20 = (
    ordenes_full
    .groupby(['product_id', 'product_name'])['order_id']
    .count()
    .reset_index()
    .rename(columns={'order_id': 'qty_compras'})
    .sort_values('qty_compras', ascending=False)
    .head(20)
    .reset_index(drop=True)
)
top_20.index += 1

print("\n" + "=" * 50)
print("TOP 20 PRODUCTOS MÁS COMPRADOS")
print("=" * 50)
print(top_20.to_string())

# VISUALIZACIÓN
plt.figure(figsize=(12, 7))
plt.barh(top_20['product_name'], top_20['qty_compras'], color='steelblue')
plt.gca().invert_yaxis()
plt.xlabel('Cantidad de compras')
plt.title('Top 20 Productos más Comprados')
plt.tight_layout()
plt.show()
