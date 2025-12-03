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

week = [] #RETORNO (ESSE CODIGO DEVE SER UMA FUNCAO) DEVE SER UMA LISTA DE DICIONARIOS EM QUE CADA DICT = 1 DIA

#loop para cada dia da semana!!!!!!!!!!!! (NAO IMPLEMENTADO)

dia = {} #O PROGRAMA ABAIXO JA IMPLEMENTA CORRETAMENTE O TRATAMENTO DO INPUT PARA 1 DIA INTEIRO (ALMOCO E JANTA) FAZER ISSO APRA A SEMANA TODA DE VEZ

#[0] = str com o nome da proteina 
proteina = soup.find_all('div', class_ = "menu-item-name")
#print(f"almoco = {proteina[0]} e jantar = {proteina[2]}")
tmp = 0
for p in proteina:
    if (tmp == 0):
        dia['lunch'] = f'{p.text.strip()}'
    elif (tmp == 2):
        proteina_janta = f'{p.text.strip()}'
    tmp += 1

#[0] = padroes ('arroz e feijao'), [1] = especial, [2] = salada, [3] = sobremesa (output especial), [4] = refresco, [5] e [6] = obs (tirar?)
acompanhamentos = soup.find_all('div', class_ = "menu-item-description")
aux = 0
for list in acompanhamentos:
    if (aux == 1 or aux == 3):
        aux += 1
        continue
    if (aux == 0):
        prefix = 'l'
    else: #aux == 2
        prefix = 'd'
        dia['dinner'] = proteina_janta
    index = 0 #indice para controle do tipo de acompanhamento
    for a in list:
        if (a.text.strip() != ''):
            if (index == 0): #arroz e feijao
                dia[f'{prefix}standart'] = f'{a.text.strip()}'
            elif (index == 1):
                dia[f'{prefix}special'] = f'{a.text.strip()}'
            elif (index == 2):
                dia[f'{prefix}salad'] = f'{a.text.strip()}'
            elif (index == 3):
                dia[f'{prefix}dessert'] = f'{a.text.strip()}'
            elif (index == 4):
                dia[f'{prefix}drink'] = f'{a.text.strip()}'
            else:
                ...
                #EH PARA CONSIDERAR AS OBSERVACOES?
            index += 1
    aux += 1
print(dia)