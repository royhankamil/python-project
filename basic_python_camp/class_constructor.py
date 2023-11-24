"""class dengan constructor (inisialisasi variable)"""

class Mobil:
    def __init__(self):         # fungsi khusus untuk membuat constructor
        self.warna = 'Merah'    # self merujuk pada kata kunci pada refrensi object saat ini

"""
dengan menambahkan self maka ketika atribut kelas diubah maka objek objek 
yang ter-refrensi juga tidak terubah
"""

mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)


class MobilDgParam:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        
mobil_1 = MobilDgParam('Merah', 'DicodingCar', 160) # wajib memberikan argumen dengan lengkap

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)


"""method yang menempel dari object"""


def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

"""
1. Pertama, kita mendefinisikan sebuah fungsi bernama my_decorator. Dekorator ini menerima 
    sebuah fungsi func sebagai parameternya.
2. Dalam fungsi my_decorator, kita mendefinisikan fungsi wrapper(). Fungsi wrapper() bertindak 
    sebagai "pembungkus" yang menambahkan perilaku sebelum dan setelah eksekusi dari fungsi func.
3. Setelah itu, fungsi  my_decorator mengembalikan (return) fungsi wrapper sebagai hasilnya. 
    Return ini juga menyebabkan fungsi wrapper dijalankan.
4. Kemudian, kita mendefinisikan fungsi say_hello(). Fungsi ini akan menjadi target dekorasi.
5. Untuk mendekorasi say_hello(), kita menggunakan simbol "@" diikuti dengan nama dekorator, 
    yaitu @my_decorator sebelum mendefinisikan fungsi say_hello.
6. Jadi, secara alur, ketika fungsi say_hello() dipanggil, sebenarnya yang dieksekusi adalah 
    fungsi wrapper() yang menjadi hasil dari dekorasi. Oleh karena itu, pesan "Sebelum fungsi 
    dieksekusi." dicetak terlebih dahulu, kemudian fungsi say_hello() dieksekusi dan mencetak 
    "Hello, world!", lalu akhirnya, pesan "Setelah fungsi dieksekusi." dicetak.
"""


"""
Dekorator sangat berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi 
atau metode tanpa harus mengubah kode asli dari fungsi tersebut. Anda bisa membaca 
lebih dalam mengenai dekorator pada laman ini.
"""

"""method yang menempel dari class"""

class MobilDgMethod:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    # Namun, object method adalah metode yang 
    # melekat terhadap suatu objek dan menggunakan 
    # parameter self. Jadi, kita tidak bisa memanggil 
    # metode ini langsung melalui kelasnya.
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = MobilDgMethod("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.
# contoh diatas setara dengan code ini " Mobil.tambah_kecepatan(mobil_1) "

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)


"""method secara statis"""

class MobilDgStaticMet:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod #perlu keyword @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
MobilDgStaticMet.intro_mobil()
mobil_1 = MobilDgStaticMet("DicodingCar")
mobil_1.intro_mobil()

class MobilDgClassMet:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):   # parameter cls merupakan kesepakatan bersama
        print("Ini adalah metode dari kelas Mobil")
        
MobilDgClassMet.intro_mobil()
mobil_1 = MobilDgClassMet("DicodingCar")
mobil_1.intro_mobil()


