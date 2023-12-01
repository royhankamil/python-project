"""-----------------------------Library Pandas-------------------------"""



import pandas as pd

# membuat data frame dari dictionary
data = {
    'Nama': ['John', 'Jane', 'Bob', 'Alice'],
    'Usia': [25, 30, 22, 28],
    'Pekerjaan': ['Engineer', 'Teacher', 'Designer', 'Doctor']
}

df = pd.DataFrame(data)

# menampilkan data frame
print(df)

"""
Pada contoh di atas, kita membuat DataFrame dari dictionary dan menampilkannya ke layar. 
DataFrame merupakan struktur data utama dalam pandas yang mirip seperti tabel atau spreadsheet. 
DataFrame merupakan struktur dua dimensi yang menyimpan data dalam bentuk baris dan kolom.
"""

print()
print()
print()

"""-----------------------------Library Numpy-------------------------"""
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)

"""
Pada kode di atas, kita mengimpor library "numpy" terlebih dahulu untuk mengambil fungsi-fungsi 
atau kode yang berada pada library tersebut. Selanjutnya, mengubah nested list menjadi array dengan
menggunakan fungsi “.array()”.
"""

print()
print()
print()

"""-----------------------------Library Matplotlib-------------------------"""
import matplotlib.pyplot as plt
 
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
 
# Membuat plot garis
plt.plot(x, y)
 
# Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
 
# Menampilkan plot
plt.show()


"""
Pada kode di atas, kita akan membuat visualisasi berdasarkan data dari variabel x dan y. Hal pertama 
yang dilakukan adalah mengimpor library dengan menggunakan sintaks “import matplotlib.pyplot as plt".

Selanjutnya, ini adalah contoh sehingga kita perlu membuat variabel sebagai data yang akan digunakan. 
Di sini kita membuat variabel x dan y sebagai data yang akan divisualisasi.

Untuk membuat visualisasinya, kita menggunakan sintaks “plt.plot(x, y)” dengan argumennya adalah 
variabel x dan y. Lalu, kita menambahkan informasi tambahan seperti title, xlabel, dan ylabel. Terakhir, 
kita menampilkan visualisasi tersebut dengan sintaks “plt.show()”.
"""

"""-----------------------------Library Sea Born-------------------------"""
import seaborn as sns
import matplotlib.pyplot as plt
 
# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()


"""
Pada contoh di atas, kita menggunakan seaborn untuk melakukan visualisasi berdasarkan dataset tips. 
Dataset ini adalah bawaan dari library seaborn yang dapat Anda gunakan.

Hal pertama yang dilakukan adalah mengimpor modul seaborn. Selanjutnya, kita load dataset dan menyimpannya 
pada variabel tips.

Untuk membuat plot yang baik, di sini kita menggabungkan seaborn dan juga matplotlib. Library matplotlib 
digunakan untuk membuat title, xlabel, ylabel, dan menampilkannya ke layar.

Untuk membuat plot histogram pada seaborn, Anda dapat menggunakan sintaks “sns.histplot()” dengan sns 
adalah library seaborn dan histplot merupakan fungsinya. Jangan lupa untuk mengisikan value dalam fungsi 
tersebut. Pada contoh di atas kita menggunakan kolom total_bill yang ada dalam dataset tips.
"""

