"""
jika bertanya bagaimana melakukan concate / penambahan jumlah anggota, bukan setiap elemen
cara concate biasa dilakukan pada list python dan untuk array numpy tetap bisa membuat concate 
tetapi penggunaan namanya berbeda, nama pada numpy yakni stacking matrix (menumpuk matriks)
"""
import numpy as np

x = np.array([3, 8, 2])
y = np.array([1, 6, 9])

xStackHor = np.hstack((x, y)) # melakukan penumpukan / penambahan di belakang secara horizontal
xStackVer = np.vstack((x, y)) # melakukan penumpukan / penambahan di belakang secara vertikal

print("x :")
print(x)

print("\ny :")
print(y)

print("\nx + y (horizontal) :")
print(xStackHor)

print("\nx + y (vertikal) :")
print(xStackVer)

"""
bisa juga berupa matriks tetapi dengan syarat
- jikalau ingin stacking horiontal, length/panjang/size baris harus sama
- jikalau ingin stacking vertikal, length/panjang/size kolom harus sama
"""

matX = np.ones((3, 4)) # matrix 3x4 valuenya 1
matY = np.zeros((3, 4)) # matrix 3x4 valuenya 0

print()
print(np.vstack((matX, matY)))

print()
print(np.hstack((matX, matY)))
