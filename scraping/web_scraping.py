"""Library web scraping adalah jenis library untuk membantu pengguna mengumpulkan data dari halaman web."""

"""---------------------------------beautifulsoup4---------------------------------------------"""
"""
pip install beautifulsoup4
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)

"""
Pada contoh di atas, kita melakukan web scraping untuk mengambil judul dari laman web 
“http://python.org/”. Hal pertama yang dilakukan adalah mengimpor Beautifulsoup sebagai library yang 
akan kita gunakan. Selanjutnya kita mengambil konten dari url dengan menggunakan fungsi dari modul 
“urlopen”. Setelah konten diambil, kita membuat objek BeautifulSoup dan dari objek ini kita bisa 
memunculkan beberapa konten berdasarkan tag html. Pada contoh di atas, kita mengambil judul halaman 
dengan menggunakan method “title”.
"""

"""---------------------------------urllib---------------------------------------------"""
from urllib.request import urlopen
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
 
# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)

"""
caranya hampir sama dengan beutifulsoup4 tetapi pada tahapan pengambilannya sedikit rumit
Tahapan ketiga adalah kita mencari indeks awal dan akhir. Tujuan kita adalah mengambil title 
sehingga indeksnya ditentukan dari tag “<title>” dan “</title>”. Terakhir, kita mengekstrak dan 
mencetak judul halaman tersebut.
"""