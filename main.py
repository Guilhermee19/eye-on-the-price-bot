import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import truncate_product_name, saveJson

array_product = []

def searchAmazon():
  os.system('cls')
  
  try:
    driver = webdriver.Edge()
    driver.get('https://www.amazon.com.br/')
    
    btn_oferta = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[3]')
    btn_oferta.click()

    # Encontrar todos os produtos
    products = driver.find_elements(By.XPATH, '//*[@id="DealsGridScrollAnchor"]/div[3]/div/div/div[2]/div[1]/div/div/div')
    
    # Contar quantos produtos existem
    num_products = len(products)
    print(f"Number of products: {num_products}")
    
    # Extrair os links
    links = [product.find_element(By.XPATH, './/div/a').get_attribute('href') for product in products]
    os.system('cls' if os.name=='nt' else 'clear')
    # print(links)
    
    # Abre cada link em uma nova janela do navegador
    for link in links:
      print("----------------\n")
      try:        
        driver.get(link)
        
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
    
      saveJson(array_product)
      
    time.sleep(60*60)
      
  except Exception as e:
    print(f"Erro: {e}")
  finally:
    driver.quit()
    searchAmazon()
      
      
# Tenta extrair as informações
def getInfo(driver, search, return_element=False):
    try:
        element = driver.find_element(By.XPATH, search)
        if return_element:
            return element
        return element.text
    except:
        return '--' if not return_element else None

      
searchAmazon()
