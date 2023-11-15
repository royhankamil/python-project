

# fungsi len() -> fungsinya untuk meghitung berapa jumlah elemen yang ada di list
data = [8, 2, 3, 1, 3, 4, 9, 10]

print(data)
print(len(data))

text = "Kali ini saya akan belajar"
print(len(text)) # akan mengeluarkan berapa banyak elemen string (hitungan setiap char)


# mencari nilai terendah{min()} dan nilai tertinggi{max()}
angka = [2, 4, 14, 14, 67, 34, 56, 64]
print(min(angka))
print(max(angka))


# fungsi untuk mengetahui berapa kali object yang sama muncul -> count()
data = [4, 5, 23, 5, 3, 21, 7, 4, 5, 21, 8]

print(data.count(4))

kata = "hello coy bahagia loh"
print(kata.count("l"))
print(kata.count("ll"))

# in dan in not fungsinya untuk mengetahui apakah ada nilai object ada dalam list / string atau tidak
print(21 in data) # true karna ada(in) di list data
print(0 not in data) # true karna tidak ada(not in) di list data
print("cuy" in kata)
print("cuy" not in kata)

# menyimpan data list ke dalam satuan variable
warga = ["Mawar", "Laki", 3]
nama, j_kelamin, anak =  warga # nama = "Mawar", j_kelamin = "Laki", anak = 3
# jumlah variable harus sama dengan length dari list

print(nama)
print(j_kelamin)
print(anak)


# melakukan pengurutan angka dan huruf 
siswa = ["Kim", "Roxanne", "Kamil", "Zidane","Ahmad", "Bagas", "Adi"]
siswa.sort() # melakukan urutan a-z
data.sort(reverse=True) # melakukan urutan terbesar - terkecil
# tidak bisa melakukan sort pada list berisi angka dan string sekaligus

print(siswa)
# Metode sort menggunakan urutan ASCII 
# sehingga nilai huruf kapital (uppercase) akan lebih 
# dahulu dibandingkan huruf kecil (lowercase).
print(data)


# ekspresi Operan dapat berupa nilai, variabel, konstanta, atau ekspresi lain.
# Operator merupakan suatu fungsi standar yang disediakan dalam bahasa pemrograman untuk melakukan 
# beberapa hal dasar, seperti perhitungan aritmetika, logika, dan relasional. Contohnya adalah penjumlahan
#  (+), pengurangan (-), perkalian (*), modulus (%), dan sebagainya.
a, b = 3, 4
result = b - a # pengurangan pada operasi angka biasa

mixed = siswa + warga # penjumlahan concate pada list

"""
Ekspresi pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan 
fungsi yang bermakna untuk menghasilkan suatu nilai dalam tipe tertentu.

Ekspresi Menurut Arity dari Operator
    jenis jenis ekspresi 
    Biner : (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).
    Uner : (x += 1), (x-=1), (not x).

Ekspresi Menurut Tipe Data yang Dihasilkan
    Ekspresi aritmetika: 2 + 2 = 4, 2 - 2 = 0
    Ekspresi relasional: 3 < 10 = True, 1 > 10 = False
    Ekspresi logika: True or False = True
"""

x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = "Dicoding"
y = "Indonesia"

print(x == y)
print(x != y)

# Menghasilkan True, jika huruf pertama pada string pertama lebih 
# BESAR dari huruf pertama pada string kedua dalam urutan alfabet. 
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)


# melakukan penukaran value variable menggunakan one liner
x = 10
y = 5
x, y = y, x

print(x, "\n", y)