"""permasalahan kode yang berulang ulang dilakukan"""

# Luas pertama
panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

"""
Kode di atas merupakan program untuk mencari luas persegi panjang. 
Perhatikan bahwa kita perlu menuliskan dua rumus kode yang sama untuk 
mencari luas persegi panjang dengan nilai panjang dan lebar berbeda.
"""


"""solusi untuk penggunaan kode yang dipakai berulang kali"""
# dengan membuat fungsi
def mencari_luas_persegi_panjang(panjang,lebar):    # function header
    luas_persegi_panjang = panjang*lebar            # function body
    return luas_persegi_panjang                     # function return

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)



"""docstring"""

"""
Docstring adalah akronim dari documentation string, bertujuan untuk 
membuat dokumentasi terhadap fungsi yang dibuat
"""

def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)



"""keyword argument"""
persegi_panjang_keyword = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_keyword)

persegi_panjang_kedua = mencari_luas_persegi_panjang(lebar=15, panjang=8)

print(persegi_panjang_kedua)


"""positional argument"""
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print(persegi_panjang_pertama) # harus sesuai dengan urutannya


"""positional or keyword parameter"""
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))


"""positional only parameter (dengan menambah / pada parameter diakhir)"""
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))


"""keyword only parameter (dengan menambah * pada parameter diawal)"""
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))


"""var positional parameter (Variadic Positional Parameter)"""
def hitung_total(*args): # merubah argumen menjadi variable tuple
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))


"""Var-Keyword (Variadic Keyword Parameter)"""
def cetak_info(**kwargs): # merubah argumen menjadi variable dictionary
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))


"""Fungsi Anonim (Lambda Expression) => one liner function"""
# mempersingkat function menjadi satu baris 
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar

print(mencari_luas_persegi_panjang(5,10))


"""variable global"""
a = 10 # variable golbal yang dapat diakses semua blok

def add(b):
    result = a+b 
    return result

bilanganPertama = add(20)
print(bilanganPertama)


"""variable lokal"""
def add(a, b):
    lokal_var = 5 # variable lokal yang dapat diakses pada blok tertentu saja
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)


"""import function"""
import func_hello # func_hello merupakan nama file

persegi_panjang_pertama = func_hello.mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
print(func_hello.nama)



