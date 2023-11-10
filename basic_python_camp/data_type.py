
# int
x = 6
print(x) 
print(type(x))

# float
y = 6.0
print(y) 
print(type(y))

# complex
z = 1 + 2j
print(z) 
print(type(z))


"""
Perlu diperhatikan bahwa tipe data numbers 
bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah. Mari lihat contoh di bawah ini.
"""

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
Output:
10
140371142789712
11
140371142789744

Pada contoh di atas, kita berusaha 
untuk melakukan perubahan tipe data 
numbers dengan melakukan inisialisasi 
ulang variabel. Namun, ternyata hal tersebut 
bukan merupakan proses mengubah nilai 
variabel. Proses tersebut lebih bisa disebut 
sebagai membuat objek baru dengan nilai baru. 
"""

# tipe data boolean
rain = True
sunny = False

print(type(rain))
print(type(sunny))



# tipe data string 
nama = "Royhan"
print(type(nama))
kota = 'Malang'
print(type(kota))

# string yang dapat menyimpan multiple line
text = """"hallo semuanya
text ini outputnya sesuai dengan newline pada text ini
fe
"""

# dapat mengambil substring pada python

huruf_awal_nama = nama[0]
awal_sampai_3 = nama[:3]
dua_sampai_akhir = nama[:3]
duplikat_nama = nama[:]
print(huruf_awal_nama)
print(awal_sampai_3)
print(dua_sampai_akhir)
print(duplikat_nama)

# tetapi perlu diingat bahwa pergantian substring pada python itu tidak bisa
# nama[1] = "e" #-> hasilnya akan error



# penggunaan formatted string / string yang dapat memasukkan variable juga 
nama = "Farhan"
print(f"Halo semua, nama saya {nama}") # hasilnya akan "Halo semua, nama saya Farhan"

# % format
nama = "zaky"
print("Halo semua, nama saya %s" % (nama)) # hasilnya akan "Halo semua, nama saya zaky"

# str format
nama = "zidane"
print("Halo semua, nama saya {}".format(nama)) # hasilnya akan "Halo semua, nama saya zaky"