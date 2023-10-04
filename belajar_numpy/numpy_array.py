import numpy as np

# membuat vector menggunakan numpy
a = np.array([1, 3, 5, 7, 9])        #menambahkan sebuah vector jenis bilangan ganjil
b = np.array([0.5, 3.5, 5, 7.7, 9.3]) # dapat berupa bilangan float juga

# membuat vector dengan dengan range (loop)
# parameter => (start, end, step)
x = np.arange(1, 10, 2)
y = np.arange(1, 13, 0.5) # bisa juga untuk stepnya menjadi angka desimal

# membuat linspace (pembagi)
# parameter => (start, end, divideToLength) divideToLength = pembagian menjadi berapa angka
c1 = np.linspace(1, 10, 4)  # hasilnya akan [1. 4. 7. 10.]

# membuat multi dimentional / matrix
mat = np.array([(1, 2, 3), 
                (4, 5, 6)])

# membuat vector dan matriks dengan nilai nol
v = np.zeros(3) # akan menghasilkan vector yang isi valuenya 0 dan length nya itu 3 [0,0,0]
m = np.zeros((3, 4)) # akan menghasilkan matriks 3x4 yang isi valuenya itu 0


# matriks dengan isi valuenya satu parameter => (length/size) hampir sama dengan np.zeros
vOnes = np.ones((3, 3))

# membuat matriks identitas ada dua cara
# matriks identitas = matriks nol dan matriks diagonal satu
"""
[
   [1 0 0]
   [0 1 0]
   [0 0 1]
]
ada dua cara membuat matriks identitas (menggunkan np.identify, menggunakan np.eye)
"""
hik = np.identity(4) # menggunakan np.identify
kih = np.eye(3) # menggunakn np.eye

# print
print(a, b, x, y, c1, mat, v, m, hik, kih, sep="\n\n")
