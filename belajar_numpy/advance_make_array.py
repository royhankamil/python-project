import numpy as np

"""membuat matriks di numpy bisa dijelaskan secara explisit untuk tipe datanya"""
arrFloat = np.array(([4, 5, 7],
                     [2, 6, 9]), dtype=float) # bisa juga untuk int 
print(arrFloat)

"""
membuat array dengan menggunakan local function
syaratnya membuat 2 parameter sebagai baris dan kolom (baris, kolom) dan mengembalikan sebuah nilai
misalnya ingin menghasilkan sebuah array baris + kolom maka harus mereturn baris + kolom
"""

def tambah(baris, kolom):
    return (baris + kolom)

def kuadrat(b, k):
    return k**2

"""menggunakan np.fromfunction
 dengan parameter => (namaFunction, (jumBaris, jumKolom), dtype=tipedata) """

bTam = np.fromfunction(tambah, (4, 3), dtype=int)
bKuadrat = np.fromfunction(kuadrat, (1, 4), dtype=float)
print(bTam)
print(bKuadrat)

"""membuat array dengan menggunakan iterable"""
iterable = (x * 3 for x in range(4)) # shortcut membuat list yang berisi iterable / for
arrIterable = np.fromiter(iterable, dtype= int)


"""
multytype array yakni terdapat dua type data misal string dan int

membuat list yang berisi couple ("key", typeData) S255 artinya string dengan max length 255
"""
newType = [('nama', 'S255'), ('nilai', int)] # hampir mirip pada template data 

data = [
    ('Farhan', 88),
    ('Dimas', 80),
    ('Aldi', 92),
    ('Kipli', 78)
]


multi = np.array(data, dtype=newType)

print(multi)
print(multi[0]) # mengambil data urutan pertama 
print(multi[0][1]) # mengambil nilai dari data urutan pertama