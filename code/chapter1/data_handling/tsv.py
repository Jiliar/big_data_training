import os
import csv

# Definir rutas
base_dir = os.path.dirname(__file__)
ruta_tsv = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones.tsv')
ruta_salida = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones_actualizadas.tsv')

# Leer y procesar
with open(ruta_tsv, mode='r', encoding='utf-8') as archivo_entrada:
    lector = csv.DictReader(archivo_entrada, delimiter='\t')
    filas = list(lector)

# Acumular subvenciones por asociación
acumulados = {}
for fila in filas:
    asociacion = fila['Asociaci_n']
    importe = float(str(fila['Importe']).replace(',', '.').strip())
    acumulados[asociacion] = acumulados.get(asociacion, 0) + importe
    fila['Subvención acumulada'] = f"{acumulados[asociacion]:.2f}"

# Escribir nuevo archivo
nombres_columnas = list(filas[0].keys())

with open(ruta_salida, mode='w', encoding='utf-8', newline='') as archivo_salida:
    escritor = csv.DictWriter(archivo_salida, fieldnames=nombres_columnas, delimiter='\t')
    escritor.writeheader()
    escritor.writerows(filas)

print("Archivo TSV actualizado con nueva columna 'Subvención acumulada'.")