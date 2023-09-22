import matplotlib.pyplot as plt
import numpy as np

#               
a1 = np.array([3, 4])
a2 = np.array([0, 1])

""" akan menjadi grafik / marker yang mana nilai x-nya = index a1 dan nilai y-nya = value a1"""
plt.plot(a1)

"""akan membentuk dari a1 sebagai posisi x dan a2 sebagai posisi y yang akan membentuk garis dari titik 
index 0 a1 a2 ke titik indeks 1 a1 a2. 
artinya mulai dari titik posisi (a1[0], a2[0]) ke titik posisi (a1[1], a2[1])
maka hasilnya akan jadi garis dari titik (3, 0) ke titik (4, 1)

"""
plt.plot(a1, a2)
plt.show()
