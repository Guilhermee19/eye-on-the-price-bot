import json
import datetime
import os

def truncate_product_name(name):
    # Definir os caracteres de corte
    delimiters = [",", "|", "(", "-"]
    # Encontrar a primeira ocorrência de qualquer delimitador
    first_occurrence = min([name.find(d) for d in delimiters if name.find(d) != -1], default=len(name))
    # Retornar o nome truncado
    return name[:first_occurrence].strip()
      
      
def saveJson(products):
    # Obter a data atual no formato 'YYYY-MM-DD'
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, 'assets')

    # Nome do arquivo com a data atual
    filename = os.path.join(assets_dir, f'products_{current_date}.json')
    
    # Salvar os detalhes dos produtos em um arquivo JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)