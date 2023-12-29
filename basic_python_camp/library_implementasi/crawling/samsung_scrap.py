import time
import pandas as pd 
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

def search_element(item, tag, tClass):
    try:
        return item.find(tag, class_=tClass).text
    except:
        return ''
    

data = []
index = 0
    
url = 'https://www.tokopedia.com/search?st=&q=samsung%20a8&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='
driver = webdriver.Chrome()
driver.get(url)

for i in range(3):
    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
    time.sleep(2)


    for j in range(21):
        driver.execute_script('window.scrollBy(0, 250)')
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for item in soup.find_all('div', class_='css-kkkpmy'):

        product = {
            'id': '',
            'nama': '',
            'harga': '',
            'lokasi': '',
            'perusahaan': '',
            'rating': '',
            'terjual': '' 
        }

        nama = search_element(item, 'div', 'prd_link-product-name css-3um8ox')
        harga = search_element(item, 'div', 'prd_link-product-price css-h66vau')
        lokasi = search_element(item, 'span', 'prd_link-shop-loc css-1kdc32b flip')
        perusahaan = search_element(item, 'span', 'prd_link-shop-name css-1kdc32b flip')
        rating = search_element(item, 'span', 'prd_rating-average-text css-t70v7i')
        terjual = search_element(item, 'span', 'prd_label-integrity css-1sgek4h')
        terjual = terjual[:-7]

        print("="*70)
        print("nama: ", nama)
        print("harga: ", harga)
        print("lokasi: ", lokasi)
        print("perusahaan: ", perusahaan)
        print("rating: ", rating)
        print("terjual: ", terjual)
        print("="*70 + "\n")

        product['id'] = index
        product['nama'] = nama
        product['harga'] = harga
        product['lokasi'] = lokasi
        product['perusahaan'] = perusahaan
        product['rating'] = rating
        product['terjual'] = terjual

        data.append(product)

        index += 1
    
    try:
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label^="Laman Berikutnya"]').click()
        time.sleep(3)
    except:
        pass


driver.close()


df = pd.DataFrame(data, columns=['id', 'nama', 'harga', 'lokasi', 'perusahaan', 'rating', 'terjual']).drop(columns='id')

print(df)

if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/data/tokped_samsung.csv'):
  os.remove(os.path.dirname(os.path.realpath(__file__)) + '/data/tokped_samsung.csv')
else:
  print("The file does not exist")

df.to_csv(os.path.dirname(os.path.realpath(__file__)) + '/data/tokped_samsung.csv')
print('tersimpan')

