import os
import xml.etree.ElementTree as ET

base_dir = os.path.dirname(__file__)
ruta_xml = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones.xml')
ruta_salida_xml = os.path.join(base_dir, '..', '..', 'data', 'chapter1', 'subvenciones_actualizadas.xml')

def limpiar_importe(importe_str):
    importe_str = importe_str.strip().replace(' ', '').replace(',', '.')
    return float(importe_str)


tree = ET.parse(ruta_xml)
root = tree.getroot()

acumulados = {}

# Iterar sobre cada fila (Row)
for row in root.findall('Row'):
    asociacion = row.find('Asociaci_n').text
    importe_texto = row.find('Importe').text
    
    importe = limpiar_importe(importe_texto)
    acumulados[asociacion] = acumulados.get(asociacion, 0) + importe
    
    # Añadir nuevo elemento 'SubvencionAcumulada' si no existe ya
    sub_acum = row.find('SubvencionAcumulada')
    if sub_acum is None:
        sub_acum = ET.Element('SubvencionAcumulada')
        row.append(sub_acum)
    sub_acum.text = f"{acumulados[asociacion]:.2f}"

# Guardar archivo XML actualizado
tree.write(ruta_salida_xml, encoding='utf-8', xml_declaration=True)

print("Archivo XML actualizado con nueva clave 'SubvencionAcumulada'.")