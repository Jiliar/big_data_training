import os
import json

# Definir rutas
base_dir = os.path.dirname(__file__)
ruta = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones.json')
ruta_salida = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones_actualizadas.json')

# Leer archivo JSON
with open(ruta, encoding='utf-8') as fichero_json:
    data = json.load(fichero_json)

# Acumular subvenciones por asociación y añadir nueva clave
asocs = {}
for linea in data:
    centro = linea['Asociación']
    valor_str = linea['Importe en euros'].strip()
    valor_str = valor_str.replace('.', '').replace(',', '.')
    subvencion = float(valor_str)

    asocs[centro] = asocs.get(centro, 0) + subvencion
    linea['Subvención acumulada'] = asocs[centro]

# Escribir archivo JSON actualizado
with open(ruta_salida, 'w', encoding='utf-8') as fichero_json_salida:
    json.dump(data, fichero_json_salida, indent=4, ensure_ascii=False)

print("Archivo JSON actualizado con nueva clave 'Subvención acumulada'.")