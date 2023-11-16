"""
"Setiap hari, Ibu selalu pergi ke pasar untuk membeli bahan makanan. Ibu selalu 
mengutamakan untuk membeli daging ayam di pasar. Jika daging ayam tidak tersedia, 
maka Ibu akan membeli tempe sebagai pengganti, lalu memasaknya."
"""


ketersediaan = "Daging ayam"

if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")


score = 100

if score == 100: # jika kondisi ini benar maka akan dieksekusi dibawahnya jika tidak maka akan diabaikan atau melewati statemnet selanjutnya
    print("Nilai Anda sempurna!")

if score != 100: print("Nilai Anda tidak sempurna!")


"""
Beberapa nilai yang dianggap sebagai false oleh Python sebagai berikut.
- 0-Nilai yang sudah didefinisikan bernilai salah: None dan False.
- Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
- Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).
Selain nilai di atas, Python akan menganggap semua nilai sebagai true.
"""

tinggi_badan = 120

if tinggi_badan >=160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster") # pasti terpenuhi jika statement di atas tidak terpenuhi

"""
elif statement menghasilkan true, blok kode di dalamnya akan dieksekusi. 
Kondisi else statement akan dijalankan dan kode di dalamnya akan dieksekusi 
jika semua kondisi sebelumnya salah atau menghasilkan false.
"""

nilai = 65

if nilai>=80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai>=70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai>=60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")

nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")


"""
Ternary operators dibangun dengan menempatkan "blok kode jika benar" pada 
posisi awal, lalu diikuti oleh "if statement" serta "kondisi"-nya. Kemudian 
"else statement" ditempatkan di akhir beserta dengan "blok kode jika salah".
"""

lulus = True
print("selamat") if lulus else print("perbaiki")


"""
Perhatikan bahwa pada ternary tuples kita menggunakan indeks ke-0 tuples sebagai 
kode jika kondisi salah, sedangkan indeks ke-1 sebagai kode jika kondisi benar. 
"""
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)
