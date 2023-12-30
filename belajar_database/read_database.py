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
show_data = 'SELECT * FROM pruduct'
cursor.execute(show_data)

# menampilkan dengan fetchall -> mengembalikan data bentuk list
data = cursor.fetchall()
print(data)


# menampilkan data dengan fetchone -> dengan satu per satu
data = cursor.fetchone()

while data is not None:
    print(data)
    data = cursor.fetchone()


