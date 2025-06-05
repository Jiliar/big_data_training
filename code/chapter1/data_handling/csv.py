import os
import csv

base_dir = os.path.dirname(__file__)
ruta = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones.csv')

# CSV
# Lectura de un archivo CSV y creación de un diccionario con las subvenciones por asociación
with open(ruta, encoding='latin1') as fichero_csv:
    dict_lector = csv.DictReader(fichero_csv)
    asocs = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        if centro in asocs:
            asocs[centro] += subvencion
        else:
            asocs[centro] = subvencion

    print(asocs)

# Actualización de un archivo CSV para incluir una columna de subvenciones acumuladas
ruta_salida = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones_actualizadas.csv')

asocs = {}
filas = []

with open(ruta, encoding='latin1') as fichero_csv:
    dict_lector = csv.DictReader(fichero_csv)
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])

        # Acumular subvención por asociación
        if centro in asocs:
            asocs[centro] += subvencion
        else:
            asocs[centro] = subvencion

        # Agregar el valor actual acumulado a la línea
        nueva_linea = linea.copy()
        nueva_linea['Subvención acumulada'] = asocs[centro]
        filas.append(nueva_linea)

# Paso 2: Escribir el archivo nuevo con la nueva columna
with open(ruta_salida, 'w', newline='', encoding='latin1') as salida_csv:
    nombres_columnas = list(filas[0].keys())
    escritor = csv.DictWriter(salida_csv, fieldnames=nombres_columnas)
    escritor.writeheader()
    escritor.writerows(filas)

print("Archivo actualizado generado con nueva columna.")
