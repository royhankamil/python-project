"""---------------------------Libary OS--------------------------------"""
import os
print(os.getcwd())



"""---------------------------Libary JSON--------------------------------"""

"""
1. JSON adalah format text-serialization dan umumnya menggunakan Unicode atau UTF-8. Sementara pickle
bersifat binary serialization.
2. JSON dapat dibaca dengan mudah oleh manusia, sementara pickle tidak.
3. JSON dapat dioperasikan dan digunakan di luar ekosistem Python. Pickle adalah Python-specific.
4. JSON secara default hanya dapat merepresentasikan subset dari built-in type pada Python.
5. Pickle dapat merepresentasikan hampir (jika tidak seluruh) tipe Python dan secara default melakukan kompresi data.
"""

import json
 
# contoh JSON:
x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
 
# parse  x:
y = json.loads(x)
 
print(y["umur"])


"""---------------------------Libary JSON--------------------------------"""
import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

""" Kode berikut adalah contoh untuk mengekstraksi berkas pickle dan menaruhnya pada sebuah variabel. """
import pickle
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
 
print(contohDictionary)

