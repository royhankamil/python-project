import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
 
data = []
index = 0

def CheckItem(item, tag, class_):
    try:
        return item.find(tag, class_=class_).text
    except:
        return ''
    
# Mencetak judul halaman
# Pengambilan konten
url = "https://www.tokopedia.com/search?st=&q=TLWR840N&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
# page = urlopen(url)
driver = webdriver.Chrome()
driver.get(url)

for k in range(15 ):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
    time.sleep(2)


    # Membuat objek BeautifulSoup
    for i in range(21):
        driver.execute_script('window.scrollBy(0, 250)')
        time.sleep(1)


    soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup)
    for item in soup.find_all('div', class_='pcv3__container css-1izdl9e'):
        product = {
            'id': '',
            'nama': '',
            'harga': '',
            'lokasi': '',
            'perusahaan': '',
            'rating': '',
            'terjual': ''
        }

        nama_produk = CheckItem(item,'div', class_='prd_link-product-name css-3um8ox')
        harga = CheckItem(item,'div', class_='prd_link-product-price css-h66vau')
        lokasi = CheckItem(item,'span', class_='prd_link-shop-loc css-1kdc32b flip')
        perusahaan = CheckItem(item,'span', class_='prd_link-shop-name css-1kdc32b flip')
        rating = CheckItem(item,'span', class_='prd_rating-average-text css-t70v7i')
        terjual = CheckItem(item, 'span', class_='prd_label-integrity css-1sgek4h')
        terjual = terjual[:-7]

        print('='*50)
        print('number:', index)
        print('nama produk:', nama_produk)
        print('harga:', harga)
        print('lokasi:', lokasi)
        print('perusahaan:', perusahaan)
        print('rating:', rating)
        print('terjual:', terjual)
        print('='*50)
        print()

        product['id'] = index
        product['nama'] = nama_produk
        product['harga'] = harga
        product['lokasi'] = lokasi
        product['perusahaan'] = perusahaan
        product['rating'] = rating
        product['terjual'] = terjual

        data.append(product)

        index += 1

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'button[aria-label^="Laman berikutnya"]').click()
    time.sleep(3)

# aria-label="Laman berikutnya"
    

driver.close()
df = pd.DataFrame(data, columns=['id', 'nama', 'harga', 'lokasi', 'perusahaan', 'rating', 'terjual'])
df = df.drop(columns='id')

print(df.head())

df.to_csv('d:/Rekayasa_Perangkat_Lunak/new_python/python-project/basic_python_camp/library_implementasi/crawling')

