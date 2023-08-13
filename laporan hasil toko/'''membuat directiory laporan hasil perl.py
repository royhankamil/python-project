'''membuat dictionary laporan hasil perlengkapan toko
    -nama toko
    -terdapat bahan bahan rumah tangga 
        seperti sabun, odol, sampo, dll.
    -terdapat tempat isi pulsa
    -milik negri, pribadi, atau koperasi
    -perlengkapan konsumsi
        +makanan ringan
        +minuman
        +roti atau mie instan
        +konsumsi bayi
    -jumlah merek produk
    -nilai desain dan daya tarik
    -persentase kelengkapan toko
'''
import os
import string
import random

#template to use dictionary
laporan_toko_template = {
    'Nama' : 'nama',
    'Jenis' : 'peralatan',
    'Isi_pulsa' : False,
    'Konsumsi' : 0,
    'Jumlah_merek' : 0,
    'Desain' : 0,
    'Persentase' : '0%'
}

os.system('cls') #clear screen
data_toko = {} 
print('='*52)
print(10*" "+ " SELAMAT DATANG DI LAPORAN TOKO " + " "*10)
print('='*52)
while True:
    toko = dict.fromkeys(laporan_toko_template)
    toko['Nama'] = input('Masukkan nama toko: ')
    toko['Jenis'] = input('Masukkan jenis toko: ')
    toko['Isi_pulsa'] = bool(input('Tempat isi pulsa: '))
    toko['Konsumsi'] = int(input('\nKelengkapan konsumsi dari \nmakanan ringan, minuman, \nice cream, makanan pokok, \nmakanan bayi(angka 1-5): '))
    toko['Jumlah_merek'] = int(input('\nMasukkan berapa banyak \njumlah merek yang terdapat di toko itu: '))
    toko['Desain'] = int(input('Masukkan nilai desain (1-100): '))
    #penilaian perhitungan persentase kedatangan dengan data yang diambil
    nilai = 0
    if toko['Isi_pulsa'] == True:
        nilai += 30
    nilai += toko['Konsumsi'] * 10
    if toko['Jumlah_merek'] >= 300:
        nilai += 10
    elif toko['Jumlah_merek'] >= 500:
        nilai += 20
    elif toko['Jumlah_merek'] >= 800:
        nilai += 30
    elif toko['Jumlah_merek'] >= 1000:
        nilai += 40
    nilai += toko['Desain']
    nilai = nilai / 220 * 100 + 14
    toko['Persentase'] = str(int(nilai) )+ '%'

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(4)))
    data_toko.update({KEY:toko})
    os.system('cls')

    print(f"{'KEY':<8} {'NAMA':<12} {'JENIS':<14} {'COUNTER':<10} {'KONSUMSI':<10} {'MEREK':<8} {'DESAIN':<8} {'PERSENTASE':<6}")

    for data in data_toko:
        KEY = data

        NAMA = data_toko[KEY]['Nama']
        JENIS = data_toko[KEY]['Jenis']
        PULSA = data_toko[KEY]['Isi_pulsa']
        KONSUMSI = data_toko[KEY]['Konsumsi']
        MEREK = data_toko[KEY]['Jumlah_merek']
        DESAIN = data_toko[KEY]['Desain']
        PERSENTASE = data_toko[KEY]['Persentase']

        print(f"{KEY:<8} {NAMA:<12} {JENIS:<14} {PULSA:^10} {KONSUMSI:^10} {MEREK:^8} {DESAIN:^8} {PERSENTASE:^6}")
    print('\n')
    lagi = input('Apakah ingin lagi(y/t): ')
    if lagi == 't':
        break

print("Itu hasilnya terima kasih")

