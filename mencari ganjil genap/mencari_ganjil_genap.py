#operasi pencari ganjil genap

while True:
    angka = int(input('masukkan angka untuk mencari genap atau ganjil: '))
    if angka % 2 == 0:
        print('angka genap')
    else :
        print('angka ganjil')
    lagi = input('apakah anda ingin lagi(y/t): ')
    if lagi == 't':
          break
    elif lagi == 'y':
        continue
    else:
        print('anda tidak memasukkab y atau t')