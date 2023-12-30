import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='basic_pybase'
)

# membuat database 
# cursor = db.cursor()
# cursor.execute('CREATE DATABASE basic_pybase')
# print('sudah terbuat')

if db.is_connected():
    print('berhasil terconnect')
