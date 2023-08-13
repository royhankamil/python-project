import os

print(10*'=' + ' data keluarga ' + 10*'=')
data_anak = [ ]
data_semua =[ ]

print('masukkan data keluarga pertama dahulu')
bapak = input('tuliskan nama bapak: ')
ibuk = input('tuliskan nama ibuk: ')
jumlah_anak =int(input('masukkan jumlah anak : '))
for anak in range(jumlah_anak):
    data_anak.append ( input('tuliskan nama anak ke-'+str(anak+1)+': '))
data_keluarga = [bapak, ibuk ]+data_anak
data_semua.append(data_keluarga)
#print(data_keluarga)
while True:
    os.system('clear')
    print('\nketik 1 untuk menambah data, \nketik 2 untuk menghapus semua data, \nketik 3 untuk melihat data, \nketik 4 untuk keluar')
    pilih = int(input('silahkan masukkan: '))
    data_keluarga =[0]
    if pilih == 1:
        data_keluarga_x = data_keluarga.copy()
        data_anak_x =[ ]
        bapak = input('tuliskan nama bapak: ')
        ibuk = input('tuliskan nama ibuk: ')
        jumlah_anak =int(input('masukkan jumlah anak : '))
        for anak in range(jumlah_anak):
            data_anak_x.append ( input('tuliskan nama anak ke-'+str(anak+1)+': '))
        data_keluarga_x= [bapak, ibuk ]+data_anak_x
        data_semua.append(data_keluarga_x)
    elif pilih == 2:
            print(10*'=' +'penghapusan data'+10*'=')
            print(data_semua)
            hapus = input('data akan dihapus semua (y/n): ')
            if hapus =='y':
                data_semua.clear()
                print('data terhapus...')
                input('\nketik untuk lanjut       ')
    elif pilih ==3:
          # print(f"{bapak:^10} {ibuk:^10} anak")
           for data in data_semua:
               print(data) 
           input('\nketik untuk lanjut   ')
            #for data in data_semua:
#                        print('\nkeluarga' +str((data+1)))
#                        print(f'nama ayah : {data_semua[data][0]}')
#                        print(f'nama ibu : {data_semua[data][1]}')
#                        for r in range(2, len(data_semua[data])+1):
#                                   print(f'anak ke-{r-1} : {data_semua[data][r]}')
    elif pilih ==4:
            break 
    else:
            print('masukkan angka 1-4')
print('Terima kasih')
            
        