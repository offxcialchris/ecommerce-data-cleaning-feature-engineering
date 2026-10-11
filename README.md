# practica_talendig_mes4_sem3_ecommerce_practica

# 🛒 Limpieza de datos y Feature Engineering — Pedidos de e-commerce

Práctica integradora del **Mes 4 · Data Science para IA (Talendig)**. Pipeline completo de limpieza y creación de variables sobre un registro de pedidos de una tienda online con clientes en distintos sectores de Santo Domingo.

## 📓 Notebook
👉 [`notebooks/practica_ecommerce.ipynb`](notebooks/practica_ecommerce.ipynb)

## Qué se hace
| Etapa | Detalle |
|---|---|
| **Exploración** | Forma, tipos de datos y diagnóstico de nulos |
| **Nulos** | `TiempoEntregaDias` → mediana (hay atípicos de 21–30 días) · `MetodoPago` → moda · `ComentarioCliente` → eliminada (>70 % nulos) |
| **Duplicados** | Se eliminan 4 filas repetidas (74 → 70 pedidos) |
| **Tipos** | `CategoriaProducto` de `int64` a `category` |
| **Feature engineering** | `MontoTotal` (cantidad × precio) · `PedidoGrande` (bandera según la mediana) · `Sector` (regex sobre la dirección) · `VelocidadEntrega` (`pd.cut`) |
| **Validación** | Mediana vs. promedio con y sin atípicos |

## 📂 Estructura
```
├── data/
│   ├── pedidos_ecommerce.csv           # datos originales (74 filas, 9 columnas)
│   └── pedidos_ecommerce_limpio.csv    # resultado final (70 filas, 12 columnas)
├── notebooks/
│   └── practica_ecommerce.ipynb
└── README.md
```

## 🛠️ Tecnologías
Python 3 · pandas · NumPy · Matplotlib · Jupyter

## ▶️ Cómo ejecutarlo
```bash
git clone https://github.com/offxcialchris/ecommerce-data-cleaning-feature-engineering.git
cd ecommerce-data-cleaning-feature-engineering
pip install pandas numpy matplotlib jupyter
jupyter notebook notebooks/practica_ecommerce.ipynb
```