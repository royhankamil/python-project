import numpy as np

x = np.arange(8) * 5

"""dapat mengambil satuan dari array numpy, caranya sama seperti mengambil di list. a[0] = mengambil i ke 0"""
print("arraynya", x)
print("mengambil index / urutan ke 0 : ", x[0])
print("mengambil index / urutan ke 4 : ", x[4])
print("mengambil index / urutan yang terakhir : ", x[-1])

"""
slicing atau memotong array dari indeks a sampai b
caranya sama sepeti menggunakan list python. 
a[start : end] //from startIndex to endIndex
a[: end] // from index 0 to endIndex
a[start :] // from startIndex to -1(end)

"""
print()
print("element x :", x[:])
print("element 2-5 :", x[2:5])
print("element awal - 6 :", x[:6])
print("element 3 - akhir :", x[3:])

"""melakukan looping sesuai list / array (iterasi)"""
print()
for i in x:
    print("value = ", i)
