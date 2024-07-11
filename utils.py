import json

def truncate_product_name(name):
    # Definir os caracteres de corte
    delimiters = [",", "|", "(", "-"]
    # Encontrar a primeira ocorrência de qualquer delimitador
    first_occurrence = min([name.find(d) for d in delimiters if name.find(d) != -1], default=len(name))
    # Retornar o nome truncado
    return name[:first_occurrence].strip()
      
      
def saveJson(products):
  # Salvar os detalhes dos produtos em um arquivo JSON
  with open('product_details.json', 'w', encoding='utf-8') as f:
      json.dump(products, f, ensure_ascii=False, indent=4)