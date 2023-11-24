"""berikut merupakan cara basic untuk penggunaan oop dalam pemrograman python"""

"""initialize class"""
class Mobil:
    # Atribut
    warna = "Merah"



"""creating object"""
mobil_1 = Mobil()


"""call the attribut of object"""
print(mobil_1.warna)
# print(nama_object.nama_atribut)


"""change the attribut"""
mobil_1.warna = "Hijau"
print(mobil_1.warna)

"""change the attribut class"""
# kekurangan dari atribut kelas yakni ini dapat mengubah semua object atribut jika atribut kelas diubah

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)

