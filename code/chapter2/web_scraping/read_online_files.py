import requests
from contextlib import closing #permite leer directamente el valor devuelto por requests.get()
import csv
import codecs #para leer directamente los strings en formato utf-8
import matplotlib.pyplot as plt

url = 'https://web.archive.org/web/20151025152204/http://www.mambiente.munimadrid.es:80/opendata/horario.txt'
with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
    for row in reader:
        print(row)