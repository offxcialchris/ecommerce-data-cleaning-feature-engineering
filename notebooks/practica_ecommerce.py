#PASO 1
#Cargar y explorar el dataset
import pandas as pd
pd.options.future.infer_string = False

df = pd.read_csv("../data/pedidos_ecommerce.csv")

print('Forma del dataset:', df.shape)
print('\nPrimeras filas:')
print(df.head())
print('\nTipos de datos:')
print(df.dtypes)

#PASO 2
#Diagnosticar los valores nulos
print()
print(df.isnull().sum())
print()
print((df.isnull().sum() / len(df) * 100).round(2))

#PASO 3
#Aplicacion de estrategia

#TiempoEntregaDias
df['TiempoEntregaDias'] = df['TiempoEntregaDias'].fillna(df['TiempoEntregaDias'].median())

#MetodoPago
df['MetodoPago'] = df['MetodoPago'].fillna(df['MetodoPago'].mode()[0])

#ComentarioCliente
df = df.drop(columns=['ComentarioCliente'])

print('\nNulos restantes:', df.isnull().sum().sum())
print(df.shape)

#PASO 4
#Eliminar duplicados
print('\nFilas antes:', len(df))
df = df.drop_duplicates()
print('Filas despues:', len(df))
print(df.shape)

#PASO 5
#Verificar tipos de datos correctos
print()
df['MetodoPago'] = df['MetodoPago'].astype('category')
print(df.dtypes)
print()
print(df.isnull().sum())

#FEATURE ENGINEERING
#PASO 6
#Combinar columnas — MontoTotal
print()
df['MontoTotal'] = (df['CantidadArticulos'] * df['PrecioUnitario'].round(2))
print(df[['CantidadArticulos', 'PrecioUnitario', 'MontoTotal']].head())

#PASO 7
#Bandera binaria — PedidoGrande
print()
print(df['MontoTotal'].describe())

print()
umbral = df['MontoTotal'].median()
df['PedidoGrande'] = (df['MontoTotal'] > umbral).astype(int)
print(df['PedidoGrande'].value_counts())

#PASO 8
#Extraer texto con regex — Sector
print()
df['Sector'] = df['DireccionEnvio'].str.extract(r',\s*(.+)$')
print(df['Sector'].value_counts())
print()
print(df[['DireccionEnvio', 'Sector']].head())

#PASO 9
#Agrupar en categorías — VelocidadEntrega
print()
df['VelocidadEntrega'] = pd.cut(
    df['TiempoEntregaDias'],
    bins=[0, 2, 5, 10],
    labels = ['Rapida', 'Normal', 'Lenta']
)
print(df[['TiempoEntregaDias', 'VelocidadEntrega']].head(10) )

#Mediana vs. promedio, con datos reales
print()
tiempos = df['TiempoEntregaDias']
atipicos = tiempos[tiempos >= 20]
normales = tiempos[tiempos < 20]
print("Con atípicos -> Media:", round(tiempos.mean(), 2), "| Mediana:", tiempos.median())
print("Sin atípicos -> Media:", round(normales.mean(), 2), "| Mediana:", normales.median())

print()
print("="*50)
print("RESUMEN FINAL DEL DATASET")
print("="*50)
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")
print(f"\nColumnas nuevas creadas hoy:")
print([c for c in df.columns if c in ['MontoTotal','PedidoGrande','Sector','VelocidadEntrega']])
print(f"\nValores nulos restantes: {df.isnull().sum().sum()}")
print(df.head())
df.to_csv("../data/pedidos_ecommerce_limpio.csv", index=False)
print("\n■ Archivo guardado como: data/pedidos_ecommerce_limpio.csv")
