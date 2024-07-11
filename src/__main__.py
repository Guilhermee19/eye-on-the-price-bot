from colorama import init, Fore, Style
from web_scraping import searchAmazon, searchKabum, searchMercadoLivre
import os

init()  # Inicializa a biblioteca colorama

def main():
  # Limpa o console no Windows
  os.system('cls')
  
  print(Fore.GREEN + "\n=== Web Scraping ===")
  print("[1] Amazon")
  print("[2] Kabum")
  print("[3] Mercado Livre")
  print("[9] Enviar Ofertas")
  print(Style.RESET_ALL)
  
  choose = input("> ")
  
  # actions
  if choose == "1": 
    searchAmazon()
    return "Amazon"
  
  # actions
  if choose == "2": 
    searchKabum()
    return "Kabum"
  
  # actions
  if choose == "3": 
    searchMercadoLivre()
    return "Kabum"
    
  else: 
    return "Opção inválida!"


if __name__ == "__main__":
  main()
