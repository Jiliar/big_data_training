# Este fragmento de código demuestra cómo obtener un archivo de texto de una URL utilizando la biblioteca de solicitudes en Python.
import requests

url = 'https://web.archive.org/web/20151025152204/http://www.mambiente.munimadrid.es:80/opendata/horario.txt'
response = requests.get(url)
print(response.status_code)
