import json
from datetime import datetime, timedelta
import os
import time


def wait_until(target_hour, target_minute):
    os.system('cls' if os.name=='nt' else 'clear')
    print("\n\n ------ O GATILHO DA COLETA É AS 10H ------ \n\n")
    
    """Aguarda até que seja a hora especificada."""
    while True:
        now = datetime.now()
        if now.hour == target_hour and now.minute == target_minute:
            break
        # Calcular quanto tempo esperar até a próxima verificação
        next_check = now.replace(second=0, microsecond=0) + timedelta(minutes=1)
        time_to_sleep = (next_check - now).total_seconds()
        time.sleep(time_to_sleep)
        

def truncate_product_name(name):
    # Definir os caracteres de corte
    delimiters = [",", "|", "(", "-"]
    # Encontrar a primeira ocorrência de qualquer delimitador
    first_occurrence = min([name.find(d) for d in delimiters if name.find(d) != -1], default=len(name))
    # Retornar o nome truncado
    return name[:first_occurrence].strip()
      
      
# def saveJson(site_name, products):

def saveJson(site_name, products):
    # Obter a data atual no formato 'YYYY-MM-DD'
    current_date = datetime.now().strftime('%Y-%m-%d')
    print(current_date)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, 'assets')

    # Nome do arquivo com a data atual
    filename = os.path.join(assets_dir, f'products_{current_date}.json')

    # Verificar se o arquivo já existe e carregar os dados existentes
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}

    # Adicionar ou atualizar os produtos para o site específico
    if site_name.lower() not in data:
        data[site_name.lower()] = []

    # Verificar e adicionar produtos não duplicados
    existing_links = {product['link'] for product in data[site_name.lower()]}
    
    for product in products:
        if product['link'] not in existing_links:
            data[site_name.lower()].append(product)
            existing_links.add(product['link'])

    # Salvar os detalhes dos produtos em um arquivo JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    