'''Program sapa dengan function'''

import os
import datetime as dt

def halo_nama(name:str):
    '''fungsi untuk memanggil nama'''
    print(" "*45 +"Halooo Selamat datang " + name +'\n'+ " "*40 + "saya harap hari ini sangat bagus")

def kotak(besar:int):
    '''display persegi'''
    for o in range(besar):
        print(besar * '*' + '\n')

def persegi_panjang(panjang:int, lebar:int):
    '''display persegi panjang'''
    for g in range(panjang):
        print(lebar * '*' + '\n')

def segitiga(tinggi:int):
    '''display segitiga'''
    spasi = tinggi
    for i in range(tinggi * 2):    
        if i %2 ==1:
            continue
        print(spasi* ' ' +'*' * (i+1 ))
        spasi -=1
    a = tinggi * 2 - 3   

def belah_ketupat(panjang:int):
    '''display belah ketupat'''
    spasi = panjang
    for i in range(panjang * 2):    
            if i %2 ==1:
                continue
            print(spasi* ' ' +'*' * (i+1 ))
            spasi -=1
    a = panjang * 2 - 3    
    spasi = 2    
    while a > 0 :    
            print(spasi * ' ' +'*' * a)
            spasi +=1
            a-=2     

os.system('cls')
print("\n\n")
print(" "*40 + "hallo selamat datang di dalam program penyapa")
nama = input(" " * 50 + "perkenalkan nama anda\n\n\n")
while True:
    os.system('cls')
    today = dt.datetime.today()
    print(str(today) + "\t\t\t\t\t\t\t\t\t\t\t" + str(today.time()))
    print(" "*50 + "window 10 pro\n")
    halo_nama(nama)
    print(" "*45 + "Try the best as you can\n")
    print(" "*50 + "What do you think\n")
    print(" "*50 + "You can choose display\n")
    print(" "*30 + "Display is persegi,persegi panjang, segitiga, belah ketupat\n")

    pilih = input('\t\t\t\t\t\t\t\t')

    if pilih == 'persegi':
        sisi = int(input('masukkan sisi: '))
        kotak(sisi)

    elif pilih == 'persegi panjang':
        panjang = int(input('masukkan panjang: '))
        lebar = int(input('masukkan lebar: '))
        persegi_panjang(panjang, lebar)
    elif pilih == 'belah ketupat':
        besar = int(input('masukkan besar: '))
        belah_ketupat(besar)
    elif pilih == 'segitiga':
        besar = int(input('masukkan besar: '))
        segitiga(besar)
    else:
        continue

    input(" "*50 + "Press 'enter' to continue\n")




