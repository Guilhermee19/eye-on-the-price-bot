import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from utils import truncate_product_name, saveJson


array_product = []

def setup_driver(view_navegation):
    options = Options()
    
    # Configurar o navegador em modo headless
    if(view_navegation):
      options.add_argument('--headless')
      options.add_argument('--disable-gpu')
      options.add_argument('--no-sandbox')
      options.add_argument('--disable-dev-shm-usage')
    
    return webdriver.Edge(options=options)
    
    
def searchKabum():
  os.system('cls')
  
  try:
    # Inicializar o WebDriver do Edge com as opções configuradas
    driver = setup_driver(False)
    
    # Abrir o navegador em tela cheia
    driver.maximize_window()
    
    driver.get('https://www.kabum.com.br/')
    
    print("\n\n ------------ OPEN KABUM ------------ \n\n")
    btn_oferta = driver.find_element(By.XPATH, '//*[@id="ofertaDoDiaMenuSuperior"]')
    btn_oferta.click()


    # Encontrar todos os produtos
    products = driver.find_elements(By.XPATH, '//*[@id="blocoProdutosListagem"]/article')
    

    # Extrair os links
    links = [product.find_element(By.TAG_NAME, 'a').get_attribute('href') for product in products]
    os.system('cls' if os.name=='nt' else 'clear')
    print(links)
    
    
    # Contar quantos produtos existem
    num_products = len(products)
    print(f"Number of products: {num_products}")
    
    array_product = []

    # Abre cada link em uma nova janela do navegador
    for link in links:
      print("----------------\n")
      try:        
        driver.get(link)
        
        time.sleep(2)
        
        name = truncate_product_name(getInfo(driver,'//*[@id="container-purchase"]/div[1]/div/h1'))
        price = getInfo(driver,'//*[@id="blocoValores"]/div[2]/div[1]/div/h4')
        
        img_element = getInfo(driver, '//*[@id="carouselDetails"]/div[2]/div/figure', return_element=True)
        img_url = img_element.find_element(By.TAG_NAME, 'img').get_attribute('src') if img_element else '--'
        
        array_product.append({
            "name": name,
            "price": price,
            "image": img_url,
            "link": link
        })
        
        print("-> ", name, ' | ' , price)
        print(img_url)

        print('\n')
        
        time.sleep(1)
        
      except Exception as e:
        print(f"Erro ao processar o produto {link}: {str(e)}")
    
      saveJson("Kabum", array_product)
      
    time.sleep(5)
      
  except Exception as e:
    print(f"Erro: {e}")
    searchKabum()
  finally:
    driver.quit()
      
      
def searchAmazon():
  os.system('cls')
  
  try:
    # Inicializar o WebDriver do Edge com as opções configuradas
    driver = setup_driver(True)
    
    # Abrir o navegador em tela cheia
    driver.maximize_window()
    
    driver.get('https://www.amazon.com.br/')
    
    print("\n\n ------------ OPEN AMAZON ------------ \n\n")
    
    btn_oferta = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[3]')
    btn_oferta.click()

    # Encontrar todos os produtos
    products = driver.find_elements(By.XPATH, '//*[@id="DealsGridScrollAnchor"]/div[3]/div/div/div[2]/div[1]/div/div/div')
    

    # Extrair os links
    links = [product.find_element(By.XPATH, './/div/a').get_attribute('href') for product in products]
    os.system('cls' if os.name=='nt' else 'clear')
    # print(links)
    
    # Contar quantos produtos existem
    num_products = len(products)
    print(f"Number of products: {num_products}")
    
    array_product = []
    
    # Abre cada link em uma nova janela do navegador
    for link in links:
      print("----------------\n")
      try:        
        driver.get(link)
        
        time.sleep(2)
        
        name = truncate_product_name(getInfo(driver,'//*[@id="productTitle"]'))
        price_c = getInfo(driver,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
        price_d = getInfo(driver,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[3]')
        
        img_element = getInfo(driver, '//*[@id="imgTagWrapperId"]', return_element=True)
        img_url = img_element.find_element(By.TAG_NAME, 'img').get_attribute('src') if img_element else '--'
                
        price = f"R$ {price_c}.{price_d}"
        
        array_product.append({
            "name": name,
            "price": price,
            "image": img_url,
            "link": link
        })
        
        print("-> ", name, ' | ' , price)
        print(img_url)

        print('\n')
        
        time.sleep(1)
        
      except Exception as e:
        print(f"Erro ao processar o produto {link}: {str(e)}")
    
      saveJson('Amazon', array_product)
      
    # time.sleep(60*60)
    time.sleep(5)
      
  except Exception as e:
    print(f"Erro: {e}")
    searchAmazon()
  finally:
    driver.quit()
      
      
def searchMercadoLivre():
  os.system('cls')
  
  try:
    # Inicializar o WebDriver do Edge com as opções configuradas
    driver = setup_driver(False)
    
    # Abrir o navegador em tela cheia
    # driver.maximize_window()
    
    driver.get('https://www.mercadolivre.com.br/')
    
    print("\n\n ------------ OPEN MERCADO LIVRE ------------ \n\n")
    
    btn_oferta = driver.find_element(By.XPATH, '/html/body/header/div/div[5]/div/ul/li[2]/a')
    btn_oferta.click()

    # Encontrar todos os produtos
    products = driver.find_elements(By.XPATH, '//*[@id="root-app"]/div[2]/div[2]/div/ol/li')
    

    # # Extrair os links
    links = [product.find_element(By.XPATH, './/div/a').get_attribute('href') for product in products]
    os.system('cls' if os.name=='nt' else 'clear')
    print(links)
    
    # # Contar quantos produtos existem
    num_products = len(products)
    print(f"Number of products: {num_products}")
    
    array_product = []
    
    # Abre cada link em uma nova janela do navegador
    for link in links:
      print("----------------\n")
      try:        
        driver.get(link)
        
        time.sleep(2)
        
        name = truncate_product_name(getInfo(driver,'//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/h1'))
        price_c = getInfo(driver,'//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]')
        price_d = getInfo(driver,'//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[4]')
        
        img_element = getInfo(driver, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[1]/div/div/div/span[1]/figure', return_element=True)
        img_url = img_element.find_element(By.TAG_NAME, 'img').get_attribute('src') if img_element else '--'
                
        price = f"R$ {price_c}.{price_d}"
        
        array_product.append({
            "name": name,
            "price": price,
            "image": img_url,
            "link": link
        })
        
        print("-> ", name, ' | ' , price)
        print(img_url)

        print('\n')
        
        time.sleep(1)
        
      except Exception as e:
        print(f"Erro ao processar o produto {link}: {str(e)}")
    
      saveJson('MercadoLivre', array_product)
      
    time.sleep(60*60)
      
  except Exception as e:
    print(f"Erro: {e}")
    searchAmazon()
  finally:
    driver.quit()
      
      
      
# Tenta extrair as informações
def getInfo(driver, search, return_element=False):
    try:
        element = driver.find_element(By.XPATH, search)
        if return_element:
            return element
        return element.text
    except:
        return '--' if not return_element else None
