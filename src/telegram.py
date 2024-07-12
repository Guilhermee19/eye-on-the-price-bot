import json
import requests
import datetime
from dotenv import load_dotenv
from time import sleep
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def getProducts():
    # Obter a data atual no formato 'YYYY-MM-DD'
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, 'assets')

    # Nome do arquivo com a data atual
    filename = os.path.join(assets_dir, f'products_{current_date}.json')
    
    data = load_json(filename)

    for store, items in data.items():
        for item in items:
            message = format_message(item)
            send_telegram_message(message)
            sleep(5)
        
    
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def format_message(item):
    return f" **{item['name']}** 😱\n\n_{item['price']}_ 🔥🔥🔥\n\n[Compre aqui !!]({item['link']})"


def send_telegram_message(message):
    # Agora você pode acessar suas variáveis de ambiente
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')

    # if(message == '-'): 
    #     return
    
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'  # Optional: Define the text formatting mode
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Failed to send message: {response.status_code} - {response.text}")
    else: 
        print(f"Enviado !")