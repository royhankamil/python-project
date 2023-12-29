import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import os
 
data = [] # untuk seluruh data akan disimpan di sini
index = 0 # untuk urutan produk

def CheckItem(item, tag, class_):
    try:
        return item.find(tag, class_=class_).text
    except:
        return ''


url = "https://www.tokopedia.com/search?st=&q=TLWR840N&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
# untuk driver atau penyamaran untuk application yang digunakan untuk scraping
driver = webdriver.Chrome()
driver.get(url) # membuka url dengan driver (chrome)

# diulang sampai 15 page 
for k in range(15):
    # menunggu samapai css selector #zeus-root(body>zeus>all-element) muncul maksimal menunggu sampai 5 detik
    # menunggu sampai websitenya terender
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
    time.sleep(2) # tunggu sampai 2 detik


    # membuat driver menscroll website sehingga dapat membuka semua pilihan produk
    for i in range(21):
        driver.execute_script('window.scrollBy(0, 250)')
        time.sleep(1)

    # memuat halaman beutiful soup page_source -> url tadi
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # mengecek untuk setiap dari class pcv3__container css-1izdl9e
    for item in soup.find_all('div', class_='pcv3__container css-1izdl9e'):

        # membuat dictionary untuk menyimpan data
        product = {
            'id': '',
            'nama': '',
            'harga': '',
            'lokasi': '',
            'perusahaan': '',
            'rating': '',
            'terjual': ''
        }
        
        # mencari isi dari masing masing item yang dicari melalui class tertentu
        nama_produk = CheckItem(item,'div', class_='prd_link-product-name css-3um8ox')
        harga = CheckItem(item,'div', class_='prd_link-product-price css-h66vau')
        lokasi = CheckItem(item,'span', class_='prd_link-shop-loc css-1kdc32b flip')
        perusahaan = CheckItem(item,'span', class_='prd_link-shop-name css-1kdc32b flip')
        rating = CheckItem(item,'span', class_='prd_rating-average-text css-t70v7i')
        terjual = CheckItem(item, 'span', class_='prd_label-integrity css-1sgek4h')
        terjual = terjual[:-7] # menghilangkan kata 'terjual'

        # memunculkan di console data setiap produk
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

        # menyimpan data produk ke dalam dictionary
        product['id'] = index
        product['nama'] = nama_produk
        product['harga'] = harga
        product['lokasi'] = lokasi
        product['perusahaan'] = perusahaan
        product['rating'] = rating
        product['terjual'] = terjual

        # menambahkan data dictionary ke dalam list seluruh data dictionary
        data.append(product)

        index += 1

    # mencoba jika tidak dapat menemukan / tidak dapat menekan tombol next
    try:
        time.sleep(2) # menunggu 2 detik
        # mencari element dengan driver (agar dapat berinteraksi) pada button next lalu mengkliknya
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label^="Laman berikutnya"]').click()
        time.sleep(3) # menunggu 3 detik
    except:
        pass

# aria-label="Laman berikutnya"
    
# menutup driver
driver.close()

# membuat data frame (yang terdapat pada seluruh data) dengan kolom sesuai dengan urutan dict 
df = pd.DataFrame(data, columns=['id', 'nama', 'harga', 'lokasi', 'perusahaan', 'rating', 'terjual'])
df = df.drop(columns='id') # menghapus kolom id

# memunculkan data frame
print(df)

# menghapus csv yang sebelumnya
try:
    os.rmdir(os.path.dirname(os.path.realpath(__file__)) + '/data/tokped_TLWR840N.csv')
except:
    pass

# save data frame ke csv
df.to_csv(os.path.dirname(os.path.realpath(__file__)) +'/data/tokped_TLWR840N.csv')

