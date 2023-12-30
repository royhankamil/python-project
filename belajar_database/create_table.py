import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='basic_pybase'
)

if db.is_connected():
    print('sudah terconnect')

cursor = db.cursor()

cursor.execute("""
               CREATE TABLE pruduct_test_2 (
               id INT AUTO_INCREMENT PRIMARY KEY,
               nama VARCHAR(100) NOT NULL,
               harga INT(20) NOT NULL,
               lokasi VARCHAR(40),
               rating FLOAT(5)
               )
               """)

print("tabel telah dibuat")


"""
penjelasan parameter 
(untuk setiap kolom setelahnya harus ada koma kecuali yg terakhir dan untuk menentukan kolom harus ada
    tanda kurung)
- command(CREATE TABLE) name-table(product)
- name-columns(id) type-data(INT) AUTO_INCREMENT(artinya akan dilakukan perhitungan / penambahan secara otomatis)
        primary-key(key yang unik dan setiap data itu berbeda dan harus ada di setiap tabel)
- name-columns(nama) type-data(VARCHAR(length-data)) -> parameter type-data adalah length dan yang non primary key
        wajib mengisi parameternya NOT NULL(opsional) -> untuk mewajibkan untuk diisi pada setiap data / baris
- untuk seterusnya hampir sama dengan point 3 dan ada yang tak ada NOT NULL karena itu opsional

untuk lebih lanjut kunjungi dokumentasi / melihat langung parameter yang ada di localhost
"""



