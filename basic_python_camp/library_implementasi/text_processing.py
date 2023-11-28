"""
library text processing adalah sekumpulan library yang bertujuan untuk melakukan pemrosesan teks dan 
menyederhanakan serta mempercepat tugas-tugas pemrosesan teks.
"""

"""
String
String adalah salah satu modul bawaan Python yang tidak perlu dideklarasikan. Pada modul string ada 
    fungsi-fungsi yang dapat dioperasikan pada variabel bertipe string seperti di bawah.
- upper(): Ubah setiap huruf dalam string menjadi huruf kapital. 
- lower(): Ubah setiap huruf dalam string menjadi huruf kecil.
- split(): Pisahkan teks berdasarkan delimiter (karakter pemisah).
- title(): Jadikan setiap awal kata kapital.
- zfill(): Tambahkan nol di awal string sebanyak nilai yang ada pada parameter.
"""

"""Regex"""

"""
Regex atau regular expression adalah sebuah cara untuk mencari teks berdasarkan pola tertentu. Umpamanya, 
ketika ingin mencari sebuah kata dalam kamus, misalnya arti dari kata parsing, kita akan mencari kata tersebut 
di halaman yang memiliki kata dengan awalan p, lalu pa. Regex bekerja dengan konsep yang sama.
Contoh umum regex adalah pada email. Kita dapat menggunakan regex untuk mengecek bahwa karakter @ ada 
pada email atau tidak.
"""

import re     # Import modul regex
 
pola= '^a...s$'
string_tes= 'abyss'
hasil= re.match(pola, string_tes)
 
if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.") 


"""
Contoh di atas menunjukkan penggunaan regex. Pada variabel pattern di bawah, ^a berarti kita ingin mencari 
teks dengan awalan 'a', dan s$ berarti kita ingin mencari string berakhiran 's'.
"""



