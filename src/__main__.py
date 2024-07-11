from colorama import init, Fore, Style
from web_scraping import searchAmazon
import os

init()  # Inicializa a biblioteca colorama

def main():
  # Limpa o console no Windows
  os.system('cls')
  
  print(Fore.GREEN + "\n=== Web Scraping ===")
  print("[1] Amazon")
  print(Style.RESET_ALL)
  
  choose = input("> ")
  
  # actions
  if choose == "1": 
    searchAmazon()
    return "Amazon"
    
  else: 
    return "Opção inválida!"


if __name__ == "__main__":
  main()
