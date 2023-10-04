import numpy as np

x1 = np.array([2, 4, 5, 3])
x2 = np.array([1, 3, 5, 2])


"""
jika kalau x1 + x2 menggunakan list biasa maka akan terjadi concate
contohnya x1 + x2 jika menggunakan list hasilnya => [2, 4, 5, 3, 1, 3, 5, 2]
tetapi kalau menggunakan numpy.array akan menghitung seperti vector matematika
misal a = np.array([1, 2, 3, 4]), b = np.array([6, 7, 8, 9])
a + b ==>(output) [7, 9, 11, 13]

begitu juga dengan operasi yang lain jika list saja tidak bisa menghitung 
"""
print(x1, "+", x2, "=", end=" ") # penambahan
print(x1 + x2) # hasil



"""
numpy array juga dapat digunakan untuk menghitung operasi vector matematika seperti -, *, /, sin(), cos(), 
dan lain lain. variabel  np.array dianggap sebagai vector / matriks matematika.
jikalau list dalam python tidak dapat menghitung -, *, /, dll. maka np.array bisa 
"""
print(x1, "x", x2, "=", end=" ") # perkalian
print(x1 * x2) # perkalian

print(x1, "-", x2, "=", end=" ") # pengurangan
print(x1 - x2) # pengurangan

print(x1, "^ 2", "=", end=" ") # pangkat
print(x1 ** 2) # pangkat

print("sin(", x1, ")", "=", end=" ") # sin
print(np.sin(x1)) # sin

print("tan(", x1, ")", "=", end=" ") # tan
print(np.tan(x1)) # sin

print(x1, "x ", 3, "=", end=" ") # bisa dikali dengan skalar
print(x1 * 3) # perkalian

print(x1, "- ", 5, "=", end=" ") # bisa ditambah dengan skalar
print(x1 - 5) # perkalian


"""
multidimensi numpy atau biasa disebut dengan matriks. Untuk perhitungannya hampir sama dengan vector
tetapi memiliki multi dimensi. 
Contoh : A = | 2 0 |        atau       B = | 5 2 4 |
             | 3 1 |                       | 3 6 0 |
matriks bisa dihitung seperti vector jika dioperasikan pada skalar (satuan angka) 
tetapi kalau bertemu sesama matriks / vector jika operasinya '+' dan '-' maka akan melakukan operasi sesuai dengan index / urutan
jika bertemu sesama matriks dan perkalian maka akan melakukan perhitungan secara advance (sran lihat youtube)
"""

m1 = np.array(([2, 0], [3, 1]))

m2 = np.array(([4, 2], 
               [7, 3]))

print("\n", m1, "+", m2, "=", sep="\n") # perkalian
print(m1 + m2) # perkalian

print("\n", m1, "-", m2, "=", sep="\n") # perkalian
print(m1 - m2) # perkalian

"""
perhitungan perkalian 
misal 
A = | a11 a12 |     B = | b11 b12 |     
    | a21 a22 |         | b21 b22 |     

    jika C = A * B 
    
C = | ( a11 * b11 + a12 * b21 )     ( a11 * b12 + a12 * b22 ) |
    | ( a21 * b11 + a22 * b21 )     ( a21 * b12 + a22 * b22 ) |

dan untuk menghitung di numpy ada 2 cara (jika a dan b adalah matriks):
1. np.dot(a, b) // artinya a * b
2. a.dot(b) // artinya a * b

"""

print("\n", m1, "x", m2, "=", sep="\n") # perkalian
# print(np.dot(m1, m2)) # bisa menggunakan seperti ini
print(m1.dot(m2)) # atau seperti ini
