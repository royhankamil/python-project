"""

Program Pembuatan Perender an nama secara random

"""
import random




hurufVokal = ["a","i", "u", "e", "o"] # huruf vokal

#huruf non-vokal
hurufBiasa = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]




def AmbilKata():
    jumlahHuruf = int(3 + random.random() * 7) # untuk merandom jumlah huruf
    hasilKata = "" # declarasi variable
    randomVokal = int(1 + random.random() * 10)
    apakahVokal = False
    if randomVokal % 2 == 0:  
        apakahVokal = False

    # jika genap akan huruf vokal
    elif randomVokal % 2 == 1:
        apakahVokal = True

    berapaVokal = int(1 + random.random() * 2)
    for i in range(jumlahHuruf): # melooping berapa huruf setiap kata
        urutan = i + 1
        # jika ganjil akan huruf biasa
        if apakahVokal == False:  
            hasilKata += random.choice(hurufBiasa)
            if urutan >= berapaVokal:
                berapaVokal = int(1 + random.random() * 2)
                apakahVokal = True # mengubah kembali ke huruf vokal

        # jika genap akan huruf vokal
        elif apakahVokal == True:
            hasilKata += random.choice(hurufVokal)
            apakahVokal = False # mengubah kembali ke huruf biasa

    return hasilKata



while True:  # melakukan hal itu sampai bilang tidak
    jumlahKata = int(1 + random.random() * 10)
    # print(jumlahKata)
    hasilNama = ""
    for i in range(jumlahKata):
        kata = AmbilKata()
        hasilNama += kata + " "
    print(hasilNama)

    inginLagi = input("\t\t\t\t\t\tapakah anda ingin lagi (y/t): ")
    if inginLagi == 't':
        break




# nama = ["N", "H", "O", "Y", "R", "A"]

# hitungan = 0

# sudah = []

# while True:
#     hitungan += 1

#     hasil = ""

#     for i in range(6):
#         for f in range(6):
#             randomize = int(random.random() * 6)
#             for r in sudah:
#                 if randomize == r:
#                     randomize = int(random.random() * 6)
#             sudah.append(randomize)

#         hasil += nama[randomize]
#     print(hasil)

#     if hasil == "ROYHAN":
#         break

# print(hitungan)

