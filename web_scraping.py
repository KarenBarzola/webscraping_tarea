import pandas

import requests

from bs4 import BeautifulSoup

import pandas as pd

# obtengo la pagina a analizar
url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)
#print(html_doc.text)

# parsear a la pagina web
soup = BeautifulSoup(html_doc.text, 'html.parser')

#print(soup.prettify())

# titulo = soup.title
# print(titulo)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
#
# print(soup.p)

titulo_datos = soup.h1.string
print(titulo_datos)

tabla = soup.table
print(tabla)

tabla = soup.find('table')

filas = tabla.find_all('tr')


nombres = []
apellido = []


for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas)>0:
    # datos = [celda.get_text(strip=True) for celda in celdas]
    # print(datos)


        nombres.append(celdas[1].string)
        apellido.append(celdas[2].string)


print(nombres)
print(apellido)


df = pandas.DataFrame({'Nombres':nombres,'Apellido':apellido})
df.to_csv('clientes.csv', index=False, encoding='utf-8')