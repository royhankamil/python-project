"""
Untuk melakukan pewarisan, anggap kita memiliki "kelas A" sebagai induk atau kelas dasar.
Dari kelas A tersebut kita membuat kelas baru bernama "kelas B" sebagai kelas turunan dari 
kelas yang didapatkan (kelas A). Ketika kelas B mewarisi kelas A, secara otomatis kelas 
ini memiliki fitur-fitur yang dimiliki oleh kelas A tersebut, dalam hal ini atribut-atribut 
dan metode-metode. 
"""

"""initialize parent"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)


"""implementasi inheritance"""
class MobilP:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(MobilP):
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Dasar
mobil_1 = MobilP("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)  



