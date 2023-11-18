"""penggunaan list yang mirip dengan array"""

x = [1, 2, 3, 4, 5]
print(x)


"""penggunaan array dalam python yang perlu menggunakan library"""

import array

x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))


"""
Pada contoh di atas, kita membuat array bertipe integer dengan menyatakan "i" 
sebelum array. Sekarang, coba Anda ubah nilai array "[1, 2, 3, 4, 5]" menjadi 
"[1, 2, 3, 4, 5, 'Dicoding']". Apa yang terjadi? Jika yang terjadi adalah error, 
hal ini disebabkan karena nilai atau elemen dalam array harus bertipe sama atau identik.
"""


"""studi kasus semisal ingin menyimpan nilai siswa """

# jangan lakukan ini
nama_siswa1 = 90
nama_siswa2 = 100
nama_siswa3 = 50
nama_siswa4 = 80
nama_siswa5 = 85
nama_siswa6 = 45
nama_siswa7 = 80
nama_siswa8 = 75
nama_siswa9 = 50
nama_siswa10 = 60

"""peran penggunaan list yang dapat menggantikan kode yang diatas dan menjadikan lebih efisien"""
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0]) 

"""
Perlu Anda ingat, setiap elemen yang ada pada list sebetulnya disimpan pada satu memori. 
Jika list adalah "[1, 2, 3]", sebetulnya Anda memerintahkan memori komputer untuk menyimpan 
integer "1" ke dalam satu tempat memori, begitu pun integer "2" akan disimpan dalam satu tempat 
memori, dan seterusnya.
"""

var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)


"""mendefinisikan list dengan nilai default"""
var_arr = [0 for i in range(10)]
print(var_arr)

var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)

"""
Pada contoh di atas, kita membuat program untuk mengubah nilai default pada variabel array "var_arr" dengan 
nilai 0 hingga 9. Output dari program tersebut adalah mengubah nilai yang awalnya adalah 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] menjadi [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

"""

"""pengaksesan array / list"""
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])


"""Pemrosesan Sekuensial"""

# pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai 
# dari elemen pada indeks terkecil hingga terbesar.

var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i] # metode indexing
    next_index = i+1 # suksesor indeks
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")



"""implementasi sekuensial processing untuk mencari nilai terbesar dalam list"""
# left_pointer = founded_highest_value
# right_pointer = compare_next_index_value # if left_pointer < right_pointer : left_pointer = right_pointer

var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

