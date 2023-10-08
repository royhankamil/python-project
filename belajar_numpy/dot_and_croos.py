import numpy as np

"""
apa itu dot
dot adalah perkalian antara 2 vector yang akan menghasilkan skalar rumus dot = a.b yakni
dot = |a|.|b|.cos0
|a| = panjang dari vector a
|b| = panjang dari vector b
0 = besar sudut antara vector a dan vector b
misal ada 2 buah vector a[1 3] dan b[2 1] dan sudut antara a dan b = 60
dot = |a|.|b|.cos0
    = 2 . 3. cos60
    = 2. 3 . 1/2
    = 3
"""


a = np.array([1, 3])
b = np.array([3, 0])

# mencari hasil dari perkalian dot
dotAB = np.dot(a, b)
print("a=", a)
print("b=", b)
print("hasil cross a . b = ",dotAB)



"""perkalian dot pada vector 3 dimensi"""
a = np.array([1, 3, 2])
b = np.array([3, 0, 2])

# mencari hasil dari perkalian dot
dotAB = np.dot(a, b)

print()
print("a=", a)
print("b=", b)
print("hasil dot a . b = ",dotAB)


"""
apa itu cross yaitu perkalian 2 vector yang akan mengembalikan vector dan urutan / arah crossnya diperhatikan
urutannya apakah +Z atau -Z
cross = a x b
      = ||a|| . ||b||.sin0.c
|a| = panjang dari vector a
|b| = panjang dari vector b
0 = besar sudut antara vector a dan vector b
c = adalah arah antara urutan a dan b. Jika vector antara a ke b itu searah jarum jam maka akan ke bawah
maka a x b => c = -Z ; b x a => c = +Z
intinya a -> b (searah jarum jam) => a x b => c = -Z (ke bawah)
intinya a -> b (berlawanan jarum jam) => a x b => c = Z (ke atas)
misal ada 2 buah vector a[1 3] dan b[2 1] dan sudut antara a dan b = 30
dot = |a|.|b|.sin0.c
    = 2 . 3. sin0
    = 2. 3 . 1/2
    = 3 . (-Z) => karena antara a ke b searah jarum jam maka akan ke bawah
"""

a = np.array([1, 2])
b = np.array([2, 1])

# mencari hasil dari perkalian dot
crossAB = np.cross(a, b)
crossBA = np.cross(b, a)

print()
print("a=", a)
print("b=", b)
print("hasil cross a x b = ", crossAB)
print("hasil cross b x a = ", crossBA)


"""cross dalam vector 3 dimensi"""
a = np.array([3, 2, 0])
b = np.array([2, 1, 0])

# mencari hasil dari perkalian dot
crossAB = np.cross(a, b)
crossBA = np.cross(b, a)

print()
print("a=", a)
print("b=", b)
print("hasil cross a x b = ", crossAB)
print("hasil cross b x a = ", crossBA)

