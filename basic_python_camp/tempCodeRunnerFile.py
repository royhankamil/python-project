
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