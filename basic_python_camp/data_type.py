
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


# contoh list
x = [1, 2.3, 'ngoding', False, 4, "kesalahan", 1.4, -2, 54.2, True]

print(x[2])
print(x[-1]) # index yang terakhir

x[2] = "baca buku"

print(x[:])
# array[0:-1]
print(x[:2])
# array[0:stop]
print(x[2:])
# array[start:-1]
print(x[1:3])
# array[start:stop]
print(x[1:6:2])
# array[start:stop:step]


# tuple
# tak dapat diubah tapi bisa di slicing seperti list
v = ("hello", 3, 0.4, False)

print(v[:2])


# set 
# sifatnya unik (tanpa duplikat) tanpa memiliki urutan
# dapat menggunakan ini untuk menghilangkan duplikat
set = {2, 4, 5, 1, 9}
set_data = {2, 4, 5, 1, 9, 2, 3, 5} # output {2, 4, 5, 1, 9, 3}

"""set adalah himpunan matematika jadi anda bisa meakukan operasi gabungan(union), intersection pada set"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)


# dictionary
data = {'name': 'roy', 'age':17, 'is_married': False}

print(data['name']) # pengaksesan menggunakan key
data['job'] = "game dev"

# menambahkan data
print(data['job']) # pengaksesan menggunakan key
print(data) 


# menghapus data
del data['is_married']
print(data)

# pengonversian tipe data

print(float(5)) # int to float
print(float("9")) # string to float

print(int(2.0)) # float to int
print(int(2.6)) # float to int
print(int("8")) # string to int

print(str(2)) # int to string
print(str(2.6)) # float to string

# konversi kumpulan data

print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
print(dict([[1,2],[3,4]]))
print(dict([(3,26),(4,44)]))

