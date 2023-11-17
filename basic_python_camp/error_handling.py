"""
Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti perintah Anda. 
Ini mengakibatkan pesan kesalahan muncul sebelum program tersebut berjalan. 

Salah satu tipe kesalahan sintaks yang sering ditemui adalah kesalahan indentasi
"""

# if 9>10:
# print("Hello World!")      # akan terjadi error indentasi


"""
Pada tipe kesalahan sintaksis (syntax errors) program akan memunculkan pesan error "SyntaxError". Program pun memberi petunjuk 
bahwa terdapat sintaks yang tidak valid berada di posisi i<3. Dapatkah Anda menemukan kesalahannya? Ya, kesalahannya adalah 
tidak terdapat tanda titik dua ":" setelah while statement.
"""
# i = 1
# while i<3
#     print("Dicoding")
#     i+=1                  # akan terjadi syntax errors


"""
Pengecualian adalah kesalahan yang terjadi ketika Python mengerti perintah Anda, tetapi mendapatkan masalah saat mengikutinya. 
Umumnya, pengecualian bisa terjadi ketika aplikasi sudah mulai beroperasi.
"""
# print(angka) # akan error karena masih belum di deklarasi

# akan mengalami error seperti dibawah
# bukan_angka = '1'
# bukan_angka + 2
# ^ akan terjadi error

"""
Pada contoh di atas, program memunculkan kesalahan karena variabel "bukan_angka" termasuk tipe data string. Di sisi lain, program 
berusaha melakukan operasi aritmetika yang mengharuskan kedua variabel 
atau operan bertipe data integer. Pesan tipe kesalahan yang dimunculkan adalah TypeError dengan keterangan atau pesan detailnya 
adalah "can only concatenate str (not "int") to str".
"""


"""--------------------------exception handling----------------------------"""
# z = 0
# print(1/z)

# ^ akan terjadi error
"""
Anda bisa simpan kode yang dibuat di dalam "try" statement. Kode 
tersebut merupakan barisan kode yang mungkin terjadi pengecualian. 
Ada pun statement "except" adalah statement yang akan digunakan ketika 
pengecualian tersebut terjadi. 
"""

z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

    """
    Pada contoh di atas, program akan menjalankan try statement terlebih dahulu dengan mengeksekusi sintaks "print(1/z)". 
    Kita tahu bahwa program tersebut akan mengalami error "ZeroDivisionError". 
    Alih-alih program menampilkan pesan "ZeroDivisionError: division by zero", kita ingin program menampilkan 
    teks "Anda tidak bisa membagi angka dengan nilai nol.
    ”"""


"""
try:
    # lakukan percobaan kode
except:
    # lakukan jika terdapat kesalahan pengecualian
else:
    # lakukan jika tidak terjadi kesalahan pengecualian
finally:
    # lakukan jika semua pertanyataan telah selesai dilakukan

"""

"""
Pada try statement, program akan menjalankan blok kode yang mungkin terjadi pengecualian. Pada except statement, program 
akan mengeksekusi statement ini jika terjadi pengecualian. Pada else statement, 
program akan mengeksekusi statement ini jika tidak terjadi pengecualian. Pada finally statement, program akan mengeksekusi 
statement ini setelah semua pernyataan di atas terjadi.
"""

var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
    

"""
Mari lihat contoh penerapannya di bawah ini, contoh tersebut merupakan program untuk menampilkan key dalam tipe data dictionary. 
Jenis pengecualian yang akan dilakukan adalah KeyError dan TypeError. Kita akan coba untuk mengakses value dictionary dari key yang
tidak ada dan mencoba mengoperasikan value dictionary tersebut yang termasuk string dengan operasi aritmetika. Untuk pengingat, 
dictionary merupakan tipe data yang melibatkan key-value. 
"""

# ---------------------Raise Exception------------------------------------
#  raise merupakan jenis error yang disengaja
"""
Misalnya, Anda ingin membuat kode program untuk menampilkan angka dari 1 hingga 10 berdasarkan input atau masukan pengguna. Namun, 
dalam program tersebut kita ingin mengontrol dengan cara berikut: jika user memberikan input berupa bilangan negatif, program akan 
memunculkan pesan error dengan keterangan "Bilangan negatif tidak diperbolehkan".
"""

var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
