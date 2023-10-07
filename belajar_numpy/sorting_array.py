import numpy as np

"""
np.floor() = untuk membulatkan ke bawah (jika ada 1.9 dibulatkan ke bawah jadi 1)
np.random.randn() = untuk membuat random dari angka 0 sampai 1 ; parameter => (baris, kolom)
dikali 20 fungsinya untuk menjadikan hasil random 0 sampai 20 
(20 dari hasil random 1 yang akhirnya dikali dengan 20)
"""
x = np.floor(np.random.randn(2, 3) * 20)

print(x)
"""
numpy array juga bisa mencari nilai maksimal dan minimal
misalnya untuk mencari nilai yang paling besar itu apa dan pada posisi / index di mana
"""
print("nilai maksimal dari array x :", x.max())
print("posisi / index nilai maksimal dari array x :", x.argmax())
print("nilai minimal dari array x :", x.min())
print("posisi / index nilai mimimal dari array x :", x.argmin())

"""
numpy array juga bisa mengurutkan data yang tidak terurut bisa berupa nilai atau posisi/index
jika data bentuknya 2 dimensi maka data yang diurutkan pada setiap baris saja 
misal ([6, 3, 2], [1, 5, 0]) =(sort)> ([2, 3, 6], [0, 1, 5])
"""
print("\nmengurutkan array x:")
print(np.sort(x)) # harus menggunakan np.sort() dan tidak bisa menggunakan x.sort()
print("\nmengurutkan array x dari posisi / index:")
print(np.argsort(x)) 

"""sorting untuk multitype array"""

"""
multytype array yakni terdapat dua type data misal string dan int
membuat list yang berisi couple ("key", typeData) S255 artinya string dengan max length 255
"""
dataType = [('nama', 'S8'), ('nilai', int)]
data =[
    ('Nicolas', 86),
    ('Bagus', 80),
    ('Dina', 92),
    ('Dimas', 88)
]

dataArr = np.array(data, dtype=dataType)
print("\ndari array: ")
print(dataArr)

"""dalam kasus ini sort terdapat 2 opsi yakni sort untuk nama atau nilai (value dari key 0 / 1)"""

print("\nurutan berdasarkan nilai: ")
print(np.sort(dataArr, order='nilai')) # mengurutkan berdasarkan nilai
print("\nurutan berdasarkan nama: ")
print(np.sort(dataArr, order='nama')) # mengurutkan berdasarkan nama

