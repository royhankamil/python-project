import numpy as np

mat = np.array(([2, 4],
              [6, 7],
              [3, 5]))

"""untuk mengetahui ukuran dari sebuah matriks bisa dengan mat.shape akan mereturn (baris, kolom)"""
print(mat)
print(mat.shape)


"""melakukan tranpose / pergantian antara index baris dengan index kolom"""
print("\ndari matriks")
print(mat)
print("\nmenjadi matriks yang sudah di tranpose")
# ada beberapa cara melakukan tranpose
print(mat.transpose())
# print(np.transpose(mat))
# print(mat.T)

"""flatten fungsinya agar merubah matriks menjadi vector sesuai urutan baris, kolom"""
print("\nmatriks yang sudah di flatten")
print(mat.ravel())
# print(np.ravel(mat))
# print(mat.flatten(mat))

"""
reshape matriks fungsinya adalah untuk melakukan perubahan ukuran baris dan kolom menjadi ukuran 
baris dan kolom yang baru. seperti diratakan / flatten terlebih dahulu lalu diatur ulang dalam bentuk
matriks dengan ukuran yan baru sesuai parameter. syaratnya ukuran baris x kolom nya sama
tetapi untuk reshape hanya sementara / bentuk return dan tidak mengubah nilai mat
"""
print("\nmatriks yang sudah di reshape")
print(mat.reshape(2, 3))

"""
fungsi resize hampir sama dengan reshape tetapi untuk resize akan mengubah nilai dari mat
dan bukan fungsi yang mengembalikan value tetapi fungsi yang mengubah parameter / object
"""

print("\nmatriks yang sudah di resize")
# print(mat.resize(2, 3)) # hasilnya akan menjadi none karna fungsi ini tidak mereturn nilai
mat.resize(2, 3) # akan melakukan pengubahan nilai mat lalu merubah ukuran baris kolom dan disimpan pada variabel mat
print(mat) # hasilnya akan berbeda dengan nilai awal
