import matplotlib.pyplot as plt
import numpy as np

#               
# a1 = np.array([3, 4])
# a2 = np.array([0, 1])


a1 = np.array([3, 4])
a2 = np.array([0, 1])

""" akan menjadi grafik / marker yang mana nilai x-nya = index a1 dan nilai y-nya = value a1"""
plt.plot(a1, label="grafik 1")

"""akan membentuk dari a1 sebagai posisi x dan a2 sebagai posisi y yang akan membentuk garis dari titik 
index 0 a1 a2 ke titik indeks 1 a1 a2. 
artinya mulai dari titik posisi (a1[0], a2[0]) ke titik posisi (a1[1], a2[1])
maka hasilnya akan jadi garis dari titik (3, 0) ke titik (4, 1)

"""
plt.plot(a1, a2, label="grafik 2")


"""parameter => color ='r', 'b' marker = 'b--', 'b-o' """
plt.plot(a2, a1, color="g", label="grafik 3")
plt.plot(a2 + a1, "b--" , label="grafik 4") # untuk marker tidak usah ditambah color = atau marker = 
a1a2 = plt.plot(a1 * a2, label="grafik 5")

"""set the properties manual"""
plt.setp(a1a2, color="r", linestyle= "-", linewidth=0.5)

"""plt.axis([xmin, xmax, ymin, ymax])
    to set display max min koordinat"""
plt.axis([0, 7, 0, 7])

"""menambahkan judul"""
judul = "mengetes basic matplotlib\n"
fungsi = r"$ \mathcal{Y} = A.\omega - \theta $"
plt.title(judul + fungsi)

"""menambahkan label(penanda) untuk value x or y"""
plt.xlabel("something random")
plt.ylabel("value random")


"""membuat legend / penanda garis termasuk pada jenis apa"""
# plt.legend()
plt.legend(loc="upper right")


"""menambahkan text dalam grafik 
    parameter => (x, y, stringText) ; optional parameter => size, color, ..."""
plt.text(2, 3, "hanya text random", size=13)
plt.text(2, 2, "menambahkan text", color="red")

"""tick berfungsi untuk membatasi angka koordinat yang keluar
    misal ingin menampilkan pada angka y hanya bilangannya genap maka yang keluar [0, 2, 4, 6, 8, ...]"""
plt.yticks([0, 2, 4, 6, 8])

"""bisa juga mengubahnya / me replace menjadi string
    maka parameternya => (value asli, replace)"""
plt.xticks(
    [1, 3, 5, 7, 9],
    ["satu", "tiga", "lima", "tujuh", "sembilan"]
    ) #bisa juga memanfaatkan replacement untuk mengubahnya menjadi derajat


"""menggeser axis atau garis pinggir (border)"""
ax = plt.gca()
ax.spines['left'].set_position(('data', -3)) # mengubah posisi border di kiri (y value) pada koordinat -3
ax.spines['bottom'].set_position(('data', 6)) # mengubah posisi border di bawah (x value) pada koordinat 6
ax.spines['top'].set_color("none") # menghilangkan border yang ada di atas
ax.spines['right'].set_color("none") # menghilangkan border yang ada di kanan

plt.show()
