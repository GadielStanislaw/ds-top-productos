# Top 20 Productos más Comprados

Análisis exploratorio de datos (EDA) para identificar los 20 productos más comprados en un dataset de órdenes de e-commerce (estilo Instacart).

## Descripción

Este proyecto carga, limpia y analiza datos de productos y órdenes para determinar cuáles son los productos con mayor frecuencia de compra, y los visualiza en un gráfico de barras horizontal.

## Estructura del proyecto

```
├── datos/
│   ├── products.csv
│   ├── order_products.csv
│   ├── aisles.csv
│   ├── departments.csv
│   └── instacart_orders.csv
├── top_20_productos.py
└── README.md
```

## Requisitos

- Python 3.x
- pandas
- matplotlib

Instalar dependencias:

```bash
pip install pandas matplotlib
```

## Uso

```bash
python top_20_productos.py
```

## Lo que hace el script

1. **Carga** los datos de `products.csv` y `order_products.csv`
2. **EDA / Calidad de datos** — revisa nulos, duplicados y consistencia en ambas tablas
3. **Limpieza** — elimina filas duplicadas
4. **Merge** — une órdenes con productos por `product_id`
5. **Top 20** — agrupa por producto, cuenta compras y obtiene el ranking
6. **Visualización** — genera un gráfico de barras horizontal con los 20 productos más comprados
