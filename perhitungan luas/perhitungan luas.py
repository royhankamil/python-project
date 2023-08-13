import datetime as dt

nama = input("Perkenalkan namamu ")

print("Hello", nama)
tanggalLahir = int(input("Masukkan tanggal lahir anda: "))
bulanLahir = int(input("Masukkan bulan lahir anda: "))
tahunLahir = int(input("Masukkan tahun lahir anda: "))
tahunIni = dt.date.today().year
bulanIni = dt.date.today().month
hariIni = dt.date.today().day
tanggalLahir = tahunIni - tahunLahir - 1

if bulanIni > bulanLahir:
    tanggalLahir += 1
elif bulanIni == bulanLahir:
    if hariIni > tanggalLahir:
        tanggalLahir += 1
    elif hariIni == tanggalLahir:
        print("Selamat ulang tahun " + nama)
        tanggalLahir += 1
print("anda hari ini berusia " + str(tanggalLahir) + " tahun")
print("Hello "+ nama +" selamat datang di perhitungan luas")

pilih = input("Pilih perhitungan luas bangun datar : ")
if pilih == "persegi":
    print("Anda memilih perhitungan luas persegi")
    sisi = int(input("masukkan panjang sisi: "))
    luas = sisi * sisi
elif pilih == "persegi panjang":
    print("Anda memilih perhitungan luas persegi panjang")
    panjang = float(input("masukkan panjang: "))
    lebar = float(input("masukkan lebar: "))
    luas = panjang * lebar
elif pilih == "lingkaran":
    print("Anda memilih perhitungan luas lingkaran")
    jariJari = float(input("masukkan jari-jari"))
    luas = 3.14 * jariJari * jariJari
else :
    print("Anda mungkin memasukkan kata yang salah\n dan perhatikan bahwa semua hurufnya harus kecil")
    luas = 0
print("luas bangun datar yakni " + str(luas))