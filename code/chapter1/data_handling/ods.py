import os
import ezodf

# Definir rutas
base_dir = os.path.dirname(__file__)
ruta_ods = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones.ods')
ruta_salida = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones_actualizadas.ods')

# Abrir archivo ODS
ezodf.config.set_table_expand_strategy('all')  # para leer todo
doc = ezodf.opendoc(ruta_ods)
sheet = doc.sheets[0]

# Leer encabezados
headers = [cell.value for cell in sheet.rows()[0]]
col_asoc = headers.index('Asociaci_n')
col_importe = headers.index('Importe')

# Añadir nueva columna si no existe
if 'Subvencion acumulada' not in headers:
    headers.append('Subvencion acumulada')
    sheet.rows()[0].append('Subvencion acumulada')
    nueva_col = len(headers) - 1
else:
    nueva_col = headers.index('Subvencion acumulada')

# Acumular subvenciones
acumulados = {}

# Procesar filas (desde la segunda)
for i, row in enumerate(sheet.rows()[1:], start=1):
    asociacion = row[col_asoc].value
    importe = float(str(row[col_importe].value).replace(',', '.').strip())
    acumulados[asociacion] = acumulados.get(asociacion, 0) + importe
    # Agregar el acumulado a la nueva celda
    if len(row) <= nueva_col:
        row.append(round(acumulados[asociacion], 2))
    else:
        row[nueva_col].set_value(round(acumulados[asociacion], 2))

# Guardar nuevo archivo
doc.saveas(ruta_salida)
print("Archivo ODS actualizado con columna 'Subvencion acumulada'.")