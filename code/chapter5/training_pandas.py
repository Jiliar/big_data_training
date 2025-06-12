import pandas as pd
import os

# Exploración de datos con Pandas : CSV
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, '..', '..', 'data', 'chapter5', 'titanic.csv')
df = pd.read_csv(path)

print(df.describe())

# Exploración de datos con Pandas : Excel
path = os.path.join(base_dir, '..', '..', 'data', 'chapter5', 'subvenciones_totales.xls')
df_dict = pd.read_excel(path, sheet_name=None)
print(df_dict['Totales'].head(10), sep="\n")

df1 = df_dict['Totales'] 

print("\n** Columns", df1.columns, sep="\n")
print("\n** Index", df1.index, sep="\n")
print("\n** Dtypes", df1.dtypes, sep="\n")
print("\n** Shape", df1.shape, sep="\n")
print("\n** Describe", df1.describe(include='all'), sep="\n")
print(df1.iloc[0:5, 0:3], sep="\n")  # Primeras 5 filas y 3 columnas
print(df1.loc[0:5, ['Asociación', 'Importe total']], sep="\n")  # Primeras 5 filas de columnas específicas

#Transformación de datos con Pandas

# Eliminar columnas innecesarias
print("\n** DataFrame original", df.columns, sep="\n")
df2 = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
print("\n** DataFrame después de eliminar columnas innecesarias", df2.columns, sep="\n")
# Eliminar filas con valores nulos
print("\n** DataFrame original", df2.shape, sep="\n")
df2 = df1.dropna()
print("\n** DataFrame después de eliminar filas con valores nulos", df2.shape, sep="\n")

# Convertir columnas categóricas a códigos numéricos
df2['Sex'] = df['Sex'].astype('category').cat.codes
df2['Embarked'] = df['Embarked'].astype('category').cat.codes
print(df2.head(10), sep="\n")

print(df.dtypes, sep="\n")
df['Is_Adult'] = df['Age'] > 18 
print("\n** DataFrame después de agregar columna Is_Adult", df.head(10), sep="\n")

# Guardar el DataFrame transformado en un nuevo archivo CSV
path = os.path.join(base_dir, '..', '..', 'data', 'chapter5', 'titanic_ml.csv')
df.to_csv(path, index=False)

# Guardar el DataFrame transformado en un nuevo archivo Excel
path = os.path.join(base_dir, '..', '..', 'data', 'chapter5', 'titanic_ml.xlsx')
df.to_excel(path, index=False)
path = os.path.join(base_dir, '..', '..', 'data', 'chapter5', 'titanic_ml.xls')
df.to_excel(path, index=False, engine='openpyxl')

# Guardar el DataFrame transformado en un nuevo archivo Excel con XlsxWriter
import xlsxwriter
path = os.path.join(base_dir, '..', '..', 'data', 'chapter5', 'titanic_2.xlsx')
writter = pd.ExcelWriter(path, engine='xlsxwriter')
df.to_excel(writter, sheet_name='Hoja1', index=False)
writter.close()