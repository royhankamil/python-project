import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='basic_pybase'
)

if db.is_connected():
    print('sudah terhubung ke server')

cursor = db.cursor()
#  "UPDATE table_name SET column = %s WHERE id = %s
column = 'lokasi'
delete = "UPDATE pruduct SET " + column + " = %s WHERE id = %s"
val = ( 'Denpasar', 3 )
cursor.execute(delete, val)

db.commit()
print("data berhasil diupdate")

