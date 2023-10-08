import numpy as np

"""
inverse adalah x^-1 atau kebalikan 
misal x = 5; x^-1 = 1/5 ; x.x^-1 = 1 => 5.5^-1 = 1
untuk matriks ketika A.A^-1 maka akan menghasilkan matriks identitas
A.A^-1 = |1 0|
         |0 1|
tetapi tidak semua angka mempunyai invers dan tidak semua matriks pula mempunyai invers
"""
#membuat 2 vector 2 dimensi 
a = np.array([(1, -1), (1, 1)])

print("a:")
print(a)

# inverse matriks
inversA = np.linalg.inv(a)  # a^-1
print("\ninvers a (a^-1):")
print(inversA)

print("\na . (a^-1):")
print(np.dot(a, inversA)) # a . a^-1 => akan menghasilkan matriks identitas (terbukti)


"""
determinan adalah luas antara vector a dengan vector b
jika ada vector b diduplikat lalu dipindah di atas vector a dan juga sebaliknya maka akan membentuk
jajargenjang atau persegi. Determinan adalah luas dari persegi tersebut
"""

detA = np.linalg.det(a)
detInversA = np.linalg.det(inversA)

print("\ndet(a):")
print(detA)
print("\ndet(a^-1):")
print(detInversA)
print("\ndet(a^-1).det(a):")
print(detInversA*detA)

