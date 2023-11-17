
# ingin menampilkan angka 1 - 10 dengan efektif tanpa harus print satu persatu

var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

# range akan mengembalikan list dengan format berikut
# -> (stop) => akan mengembalikan list 0 - <stop - 1>
# -> (start, stop) => akan mengembalikan list <start> - <stop - 1>
# -> (start, stop, step) => akan mengembalikan list <start> - <stop - 1> dengan kelipatan <step>
for i in range(1, 11):
    print(i)

"""
-"Start" merupakan nilai awal dari urutan bilangan yang bersifat opsional, jika Anda tidak memasukkannya, nilai awal akan dianggap 0. 
-"Stop" merupakan nilai batas yang wajib dimasukkan. Urutan akan berhenti sebelum mencapai nilai "stop" (eksklusif). 
-"Step" merupakan nilai penambahan antara setiap dua bilangan dalam urutan yang bersifat opsional. Jika nilai tersebut tidak diberikan, secara de
"""

for i in range(1,10,2):
    print(i)


counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment


# berhati hati dengan infinite loop
# counter = 1
# while counter <= 5:
#     print(counter)


for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

"""
Break statement adalah pernyataan 
untuk menghentikan perulangan dan
kemudian program akan otomatis keluar
dari perulangan tersebut, lalu 
dilanjutkan dengan mengeksekusi blok 
perulangan selanjutnya.
"""

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1


for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

"""
Continue statement adalah pernyataan untuk 
membuat iterasi berhenti, kemudian melanjutkan 
ke iterasi berikutnya.
"""

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))


"""
Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.
"""

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")


"""
Perlu diperhatikan oleh Anda, if dan else pada contoh tersebut berkaitan walaupun berbeda blok. 
Pada else setelah for, statement else tidak akan dieksekusi saat if pernah sekali saja benar. 
Dengan kata lain, break dalam if harus tidak terjadi untuk memicu else setelah for.
"""

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

"""
Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan 
atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
"""

x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

"""
List Comprehension
Masih terkait perulangan, terkadang ada kalanya Anda perlu membuat sebuah list baru berdasarkan list yang sudah ada.
"""
# contoh kode yang kurang baik
# angka = [1, 2, 3, 4]
# pangkat = []
# for n in angka:
#   pangkat.append(n**2)

# print(pangkat)

# bisa menjadi solusi lebih singkat dan jelas menjadi seperti dibawah
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

# new_list = [expression for_loop_one_or_more_condition]
kubik = [i ** 3 for i in range(1,11)]
print(kubik)
