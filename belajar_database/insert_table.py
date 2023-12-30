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

query = "INSERT INTO pruduct (nama, harga, lokasi, rating) VALUES(%s, %s, %s, %s)"
data = ('asus rog', 7000000, 'Malang', 4.8)

cursor.execute(query, data)

db.commit()

print("sudah termasukkan")
