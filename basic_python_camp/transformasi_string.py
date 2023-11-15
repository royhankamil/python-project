
"""transformasi string pada python"""
kata = "halo semua"

# mengubahnya menjadi huruf besar semua
print(kata.upper())

# mengubahnya menjadi huruf kecil semua
print(kata.lower())



# mengubah awalan atau akhiran yang kosong

# menghapus kosong yang kanan
print("python coy                   ".rstrip())

# menghapus kosong yang kiri
print("                    python coy".lstrip())

# menghapus kosong yang di kiri dan kanan
print("                    python coy                    ".strip())
print("                    python coy".strip())

# menghilangkan selain whitespace
print("cakcakcakcakhelo semuanya".strip("cak"))


# komparasi string jika awalannya ...
print("Coding, ngoding, ngoding".startswith("Coding")) # akan mereturn true karna benar teks tsb dimulai dg Coding

# komparasi string jika akhirannya ...
print("kerja, ngoding, kaya".endswith("kaya")) # akan mereturn true karna benar teks tsb diakhiri dg kaya

# menggabungkan list string
print(' '.join(["aku", 'kaya', 'coy']))
print('-'.join(["aku", 'kaya', 'coy']))

# memisahkan string menjadi sekumpulan list
print("aku kaya coy ;)".split())
print('-'.join(["aku", 'kaya', 'coy']))


# melakukan replace atau pregantian string satu menjadi lainnya
kata = "ayo coding biar kaya"
print(kata.replace("kaya", "cerdas"))
 

 # melakukan pengecekan yang ada di string 

# mengecek apakah huruf kapital semua
nama = "ROYHAN" # true karna semuanya kapital
print(nama.isupper())

# mengecek apakah huruf kecil semua
nama = "ROYHAN" # false karna semuanya kapital
print(nama.isupper())

# mengecek apakah huruf alphabet semua
nama = "ROYHAN" # true karna semuanya alphabet
kelas = "10 RPL C" # false karna ada angkanya
print(nama.isupper())
print(kelas.isupper())

# mengecek apakah angka / alphabet / keduanya
nama = "Kamil" # true karna semuanya alphabet
print(nama.isupper())

# mengecek apakah isi string semuanya adalah angka
print("1524".isdecimal()) # hasilnya akan true karna semuanya angka

# mengecek apakah string berisi spasi / whitespace semua
print("                 ".isspace()) # hasilnya true karna spasi semua


# mengecek apakah huruf pertama setiap kata kapital dan setelahnya huruf kecil (title)
print("Halo Semuanya Saya Royhan".istitle()) # true karna title


# formatting pada python

# zfill (menambahkan angka 0 untuk memastikan subuah angka atau nilai memiliki panjang tetap)

teks = 'Code'
tambah_number = teks.zfill(7)
print(tambah_number)


"""
Variabel teks menyimpan nilai string berupa "Code". Perlu dipahami bahwa kata "Code" hanya memiliki 4 huruf atau sederhananya panjang kata "Code" adalah 4.
Variabel tambah_number menyimpan nilai variabel teks dengan memanggil metode zfill(5).  Angka 5 tersebut merupakan parameter untuk menentukan panjang yang diinginkan oleh string. Sederhananya, Anda memastikan bahwa panjang kata "Code" haruslah 5 dan bukan 4. Jadi, program akan menambahkan angka 0 di depan kata "Code" untuk memastikan bahwa panjangnya adalah 5.
"""


# membuat string menjadi rata kanan dengan parameter berapa spasinya
print("aroyka".rjust(27))
print("aroyka".rjust(27, "-"))

# membuat string menjadi rata kiri dengan parameter berapa spasinya
print("aroyka".ljust(20))
print("aroyka".ljust(20, "+"))

# membuat string menjadi rata tengah dengan parameter berapa spasinya
print("aroyka".center(30))
print("aroyka".center(30, "+"))

# string literal (untuk masalah string 'jum'at')
hari = 'jum\'at'
print("halo\tapakabar semua\n baik baik saja kan?")

# raw string untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan.
print(r'helo semua\tjangan lupa ibadah') # \t akan dianggap sebagai string

