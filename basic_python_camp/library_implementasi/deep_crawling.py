from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
 
# Pengambilan konten
url = "https://www.tokopedia.com/search?st=&q=TLWR840N&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
# page = urlopen(url)
driver = webdriver.Chrome()
driver.get(url)
# Membuat objek BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
 
def CheckItem(item, tag, class_):
    try:
        return item.find(tag, class_=class_).text
    except:
        return ''
    
# Mencetak judul halaman
# print(soup)

for item in soup.find_all('div', class_='pcv3__container css-1izdl9e'):
    nama_produk = CheckItem(item,'div', class_='prd_link-product-name css-3um8ox')
    harga = CheckItem(item,'div', class_='prd_link-product-price css-h66vau')
    harga = CheckItem(item,'div', class_='prd_link-product-price css-h66vau')
    lokasi = CheckItem(item,'span', class_='prd_link-shop-loc css-1kdc32b flip')
    perusahaan = CheckItem(item,'span', class_='prd_link-shop-name css-1kdc32b flip')
    rating = CheckItem(item,'span', class_='prd_rating-average-text css-t70v7i')
    terjual = CheckItem(item, 'span', class_='prd_label-integrity css-1sgek4h')

    print('='*50)
    print('nama produk:', nama_produk)
    print('harga:', harga)
    print('lokasi:', lokasi)
    print('perusahaan:', perusahaan)
    print('rating:', rating)
    print('terjual:', terjual)
    print('='*50)
    print()



driver.close()

