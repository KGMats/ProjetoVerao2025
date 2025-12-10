# codigo para enviar a mensagem formatada 

import json
import os
from random import choice
from datetime import date
from urllib.parse import quote
import selenium.webdriver as wb
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle
import time

def create_msg(meal: dict, classification: dict, msg_dict: dict, msg: str = ""):
    """
    meal: dict -> Refeição do dia.
    classification: dict -> Dicionário que classifica as refeições.
    msg_dict: dict -> Dicionário das mensagens.
    msg: str -> String adicionada no início de toda mensagem. 
    """
    proteina = meal["proteina"]
    guarnicao = meal["guarnicao"]
    salada = meal["salada"]
    sobremesa = meal["sobremesa"]
    suco = meal["suco"]

    proteina_msg = choice(msg_dict[classification["proteina"]])[:]
    guarnicao_msg = choice(msg_dict[classification["guarnicao"]])[:]
    salada_msg = choice(msg_dict[classification["salada"]])[:]
    sobremesa_msg = choice(msg_dict[classification["sobremesa"]])[:]
    suco_msg = choice(msg_dict[classification["suco"]])[:]

    for i in range(len(proteina_msg)):
        if proteina_msg[i] == "_":
            proteina_msg[i:i + 1] = proteina

    for i in range(len(guarnicao_msg)):
        if guarnicao_msg[i] == "_":
            guarnicao_msg[i:i + 1] = guarnicao

    for i in range(len(salada_msg)):
        if salada_msg[i] == "_":
            salada_msg[i:i + 1] = salada

    for i in range(len(sobremesa_msg)):
        if sobremesa_msg[i] == "_":
            sobremesa_msg[i:i + 1] = sobremesa
    
    for i in range(len(suco_msg)):
        if suco_msg[i] == "_":
            suco_msg[i:i + 1] = suco
    
    return quote(msg + proteina_msg + guarnicao_msg + salada_msg + sobremesa_msg + suco_msg)

def send_msg(msg: str):

    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\Bernardo\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver = wb.Chrome(options=options)
    driver.get(f"https://web.whatsapp.com/")
    load_cookies(driver)
    driver.get(f"https://web.whatsapp.com/send?&text={quote(msg)}")
    
    found = False
    while not found:
        try:
            box = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div[2]')
            found = True
        except:
            pass
    box.click()
    
    found = False
    while not found:
        try:
            forward_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/span[2]/div/div/div/div/div/div/div/span/div/div/div')
            found = True
        except:
            pass
    time.sleep(2)
    forward_button.click()

    found = False
    while not found:
        try:
            send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/div/span/button')
            found = True
        except:
            pass
    time.sleep(2)
    send_button.click()
    time.sleep(2)
    save_and_exit(driver)

def load_cookies(driver):
    try:
        cookies = pickle.load(open('.cookies.pkl', 'rb'))
        for cookie in cookies:
            driver.add_cookie(cookie)
    except Exception:
        pass

def save_and_exit(driver):
    pickle.dump(driver.get_cookies(), open('.cookies.pkl', 'wb'))
    driver.close()
    exit()

def get_quality(meal: dict, classification: dict):
    quality = {
        "proteina": "neutro"
        "guarnicao": "neutro"
        "salada": "neutro"
        "sobremesa": "neutro"
        "suco": "neutro"
        }
    
    proteina = meal["proteina"]
    guarnicao = meal["guarnicao"]
    salada = meal["salada"]
    sobremesa = meal["sobremesa"]
    suco = meal["suco"]

    proteina_simplificado = proteina.split()[0]
    if proteina_simplificado in classification:
        quality["proteina"] = classification[proteina_simplificado]

    guarnicao_simplificado = guarnicao.split()[0]
    if guarnicao_simplificado in classification:
        quality["guarnicao"] = classification[guarnicao_simplificado]

    salada_simplificado = salada.split()[0]
    if salada_simplificado in classification:
        quality["salada"] = classification[salada_simplificado]
    
    if sobremesa in classification:
        quality["sobremesa"] = classification[sobremesa]
    
    suco_simplificado = suco.split()[2]
    if suco_simplificado in classification:
        quality["suco"] = classification[suco_simplificado]





def send_lunch():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(diretorio_atual)
    caminho_arquivo = os.path.join(diretorio_raiz, config.week_meals_file)

    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        meal = json.load(file)[str(date.today())]["almoco"]["RU"]

    caminho_arquivo = os.path.join(diretorio_raiz, config.msgs)
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        msgs = json.load(file)

    quality = get_quality(meal)

    msg = create_msg(meal, quality, msgs)
    send_msg(msg)
    return

def send_dinner():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(diretorio_atual)
    caminho_arquivo = os.path.join(diretorio_raiz, config.week_meals_file)

    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        meal = json.load(file)[str(date.today())]["jantar"]["RU"]

    caminho_arquivo = os.path.join(diretorio_raiz, config.msgs)
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        msgs = json.load(file)

    quality = get_quality(meal)

    msg = create_msg(meal, quality, msgs)
    send_msg(msg)
    return











