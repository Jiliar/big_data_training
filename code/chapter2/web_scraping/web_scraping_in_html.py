from bs4 import BeautifulSoup
import os

base_dir = os.path.dirname(__file__)
ruta = os.path.join(base_dir, '..', '..', '..','data', 'chapter2', 'mini.html')

with open(ruta, encoding='utf-8') as f:
    page = f.read()

    soup = BeautifulSoup(page, 'html.parser')
    print(soup.prettify())

    hijosDoc = list(soup.children)
    print("hijos del documento: "+str(hijosDoc))
    print("Número de hijos del documento: ", len(hijosDoc))

    html = hijosDoc[1]
    print(html)

    divs = soup.find_all('div')
    print("Número de divs: ", len(divs))
    print("Contenido del primer div: ", divs[0].text)
    print(divs[0].get_text())
    print(soup.find("div", id="date").get_text())