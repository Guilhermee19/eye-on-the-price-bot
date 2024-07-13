from colorama import init, Fore, Style
from web_scraping import searchAmazon, searchKabum, searchMercadoLivre
from telegram import getProducts
from utils import wait_until
import os
import time


init()  # Inicializa a biblioteca colorama

def main():
  # Limpa o console no Windows
  os.system('cls')
  
  print(Fore.GREEN + "\n=== Web Scraping ===")
  print("[1] Automatização")
  print("[2] Amazon")
  print("[3] Kabum")
  print("[4] Mercado Livre")
  print("[9] Enviar Ofertas")
  print(Style.RESET_ALL)
  
  choose = input("> ")
  
  # actions
  if choose == "1": 
    # while True:
      # wait_until(10, 0)
      
      searchAmazon()
      searchKabum()
      getProducts()
      
      # Esperar um minuto para evitar múltiplas capturas na mesma hora
      # time.sleep(60)
        

  # actions
  if choose == "2": 
    searchAmazon()
    return "Amazon"
  
  # actions
  if choose == "3": 
    searchKabum()
    return "Kabum"
  
  # actions
  if choose == "4": 
    searchMercadoLivre()
    return "Kabum"
  
  # actions
  if choose == "9": 
    getProducts()
    return "Enviar Ofertas"
    
  else: 
    return "Opção inválida!"


if __name__ == "__main__":
  main()
