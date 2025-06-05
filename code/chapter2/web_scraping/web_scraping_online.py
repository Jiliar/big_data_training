import requests
from bs4 import BeautifulSoup
import re


url = 'https://sede.inclusion.gob.es/fecha-y-hora-sede'
r = requests.get(url, verify=False)
print(r)

soup = BeautifulSoup(r.content, "html.parser")
cajaHora = soup.find("div" ,class_="fecha-hora")
if cajaHora:
    text = list(cajaHora.children)[1].get_text()
    divided_text = re.sub(r'[\r\n]+', ' ', text).split(" ")
    clean_text = [x for x in divided_text if x != '']
    resultado = ' '.join(clean_text)
    print(resultado)
else:
    print("Elemento no encontrado")

