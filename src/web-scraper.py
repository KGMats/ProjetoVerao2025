from bs4 import BeautifulSoup #bibioteca para filtrar o texto do site
import requests #biblioteca para pegar o texto do site

#link do site a ser utilizado
url = 'https://sistemas.prefeitura.unicamp.br/apps/cardapio/index.php' 

#retrieves data from a web server.
page = requests.get(url) 

#html do site 
soup = BeautifulSoup(page.text, 'html.parser') 
#print(soup.prettify())

#soup.find (acha a primeira instancia de um objeto html), possibilita o .text
#soup.find_all (acha toda as instancias daquele tipo de objeto html)
#soup.find_all('div', class_ = '') para buscas especificas com base na classe

#cardapio = soup.find_all('div', class_ = "menu-item")
#print(cardapio)

week = []

#loop para cada dia da semana

dia = {}

#loop para cada refeicao => instancias no dicionario

proteina = soup.find_all('div', class_ = "menu-item-name")
#print(f"almoco = {proteina[0]} e jantar = {proteina[2]}")
aux = 0
for p in proteina:
    if (aux == 0 or aux == 2):
        print(p.text.strip())
    aux += 1

acompanhamentos = soup.find_all('div', class_ = "menu-item-description")
aux = 0
for list in acompanhamentos:
    teste = []
    if (aux == 1 or aux == 3):
        aux += 1
        continue
    for a in list:
        if (a.text.strip() != ''):
            teste.append(a.text.strip())
    print(teste)
    aux += 1

