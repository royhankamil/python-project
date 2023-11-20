"""
1. Matriks adalah kumpulan data yang diatur dalam 
bentuk tabel dua dimensi dengan setiap elemennya 
terdefinisi berdasarkan baris dan kolom.

2. Setiap elemen matriks dapat diakses melalui metode 
indexing jika kedua indeks telah diketahui.

3. Elemen matriks dideklarasikan memiliki tipe homogen 
yang artinya elemen tersebut harus mempunyai tipe data yang sama. 
Jika elemen tersebut adalah bilangan real, seluruh elemen lainnya 
pun adalah bilangan real. Walaupun dalam list Python Anda dapat 
membuat matriks dengan tipe data berbeda, alangkah lebih baik 
jika tetap mengikuti aturan ini.

"""

matriks = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
            
print(matriks)


"""
kita mendeklarasikan variabel "matriks" dan menginisialisasikan dengan nested list.
"""



"""
membuat matriks dengan nested list akan lebih boros memori solusinya 
adalah dengan membuat matriks dengan array (karena setiap variable nya
akan disimpan di memory yang sama)
contohnya array dengan menggunakan numpy array
"""

import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)


"""perbandingan memori matriks list dengan matriks numpy"""
import numpy 
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)


"""Mendeklarasi matriks"""
matriks = [[1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1]]
     
print(matriks)

"""deklarasi matriks dengan nilai default"""
matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)
# ukuran baris = 3 dan ukuran kolom = 4.


"""akses elemen matriks"""
var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1]) # mengambil nilai dari 12
# nama_var[index_baris][index_kolom]


"""operasi matriks"""

# perkalian matriks dengan konstanta    
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)


# melakukan operasi matriks dengan menggunakan library numpy
import numpy as np

var_mat = np.array([[5, 0],
                    [1, -2]])

result = var_mat * 2

print(result)

"""
fungsinya antara operasi dg library dan tanpa library memiliki tujuan sama yakni
mengkalikan matriks dengan konstanta. Hanya saja dengan menggunakan library numpy
akan menjadi jauh lebih simple dan mudah dibaca
"""

