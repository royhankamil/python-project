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
# DELETE FROM nama_tabel WHERE var_primary_key=%s
delete = 'DELETE FROM pruduct WHERE id=%s'
val = (1, )
cursor.execute(delete, val)

db.commit()
print("data berhasil dihapus")

