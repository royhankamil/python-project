import mysql.connector 

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database=''
)

if db.is_connected():
    print('gasin berhasil')
