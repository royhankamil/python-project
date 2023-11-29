"""
Library parser pada Python menyediakan fasilitas untuk menguraikan kode Python menjadi struktur 
data yang dapat diproses dan dianalisis.
"""

"""
Argument parser bermanfaat jika kita ingin membuat program atau skrip kecil yang langsung menerima 
parameter pada saat pemanggilan program.Hal ini biasa digunakan dalam pemanggilan aplikasi atau skrip di 
CLI/terminal *nix-based, misalnya Linux dan MacOS. Contoh perintah dimaksud adalah berikut.
"""

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
   print("Halo, ini merupakan sebuah output dari panggildicoding.py")

"""
- Berkas panggildicoding.py dapat menerima parameter -o atau --output.
- Jika kita memanggil berkas tanpa parameter -o, berkas tidak akan menampilkan apa pun.
- Jika kita memanggil dengan -o atau --output, berkas akan menampilkan Halo, ini merupakan sebuah output 
    dari panggildicoding.py.
- Jika kita memanggil --help, tampil help dengan penjelasan "tampilkan output"
"""


""" penggunaan variabel """

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
args = parser.parse_args()
 
print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama)


"""
:- Berkas panggildicoding.py harus dipanggil dengan parameter -n atau --nama.
:- Jika kita memanggil berkas tanpa parameter -n, berkas akan meminta parameter n atau nama.
:- Jika kita memanggil dengan -n NAMAKITA atau --nama NAMAKITA, berkas akan menampilkan Terima kasih 
    telah menggunakan panggildicoding.py NAMAKITA.
:- Jika kita memanggil --help, tampil help dengan penjelasan "Masukkan Nama Anda".
"""


# Anda dapat menyuplai lebih dari satu argumen dengan menambahkan parser.add_argument sejumlah yang Anda inginkan. 

"""menambahkan statement pada parse"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="masukkan nama anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="masukkan tanggal lahir anda (DD-MM-YY)")
args = parser.parse_args()

# print(datetime.time.)
yearIs = args.tanggallahir.split("-")[2]

if (2020 - int(yearIs) < 30):
    print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2020, kakak "+args.nama)

else:
    print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2020, bapak "+args.nama)
