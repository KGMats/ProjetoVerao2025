# codigo para enviar a mensagem formatada

import json
from pywhatkit import sendwhatmsg_to_group
from random import choice
from datetime import date

diAtual = date.today().isoformat()  #classe data do datetime que tem o método today, isoformat é o formato da data na chave do dict
with open("../weekly-quotes.json", "r", encoding= "utf8") as f: #abrir arquivo padrão
    msgs = json.load(f)

with open("../weekly-data.json", "r", encoding= "utf8") as f:
    ref = json.load(f)

sendwhatmsg_to_group("BmrEqCXJkUTHlEiZhCifUD", f"""{ref[diAtual]["almoco"]}""", 10, 00, 10, True)
try:
    sendwhatmsg_to_group("BmrEqCXJkUTHlEiZhCifUD", f"""{ref[diAtual]["jantar"]}""", 15, 00, 10, True)
#Domingo e feriados não tem janta
except KeyError:
    pass
