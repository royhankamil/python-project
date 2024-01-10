"""-----------------------------Library Pandas-------------------------"""



import pandas as pd

# membuat data frame dari dictionary
data = {
    'Nama': ['John', 'Jane', 'Bob', 'Alice'],
    'Usia': [25, 30, 22, 28],
    'Pekerjaan': ['Engineer', 'Teacher', 'Designer', 'Doctor']
}

# untuk membaca dataframe melalui csv
# df = pd.read_csv("csv_dir.csv")

df = pd.DataFrame(data)

# menampilkan data frame
print(df) # menampilkan seluruh data 

print(df.head()) # menampilkan 5 baris data dari atas (argumen bisa diisi ingin ditampilkan berapa baris data)

print(df.tail()) # menampilkan 5 baris data dari bawah

print(df.columns) # menampilkan nama kolomnya

print(df.Nama) # menampilkan data dengan spesifik kolom (pada kolom nama)

print(df['Usia']) # menampilkan data dengan spesifik kolom (pada kolom usia)

print(df[['Nama', 'Pekerjaan']]) # menampilkan data dengan spesifik beberapa kolom (pada kolom nama dan pekerjaan)

"""
df.shape => untuk mengetahui ukuran data
df.index => untuk mengetahui indexnya
"""


# slicing dengan iloc dan loc
# menslicing menggunakan nama data [baris_awal : sampai_baris, kolom_awal : sampai_kolom]
print(df.loc[1:2, "Nama":"Usia"]) 
# menslicing menggunakan nama data [baris_awal : sampai_baris, list_kolom]
print(df.loc[1:2, ["Nama","Pekerjaan"]]) 

# menslicing menggunakan index
# menslicing menggunakan index data [baris_awal : sampai_baris, index_colomns_awal, sampai_index_columns]
print(df.iloc[1:2, 1:2]) 
# menslicing menggunakan nama data [baris_awal : sampai_baris, list_index_kolom]
print(df.iloc[1:2, [0, 2]]) 



# pandas memiliki table kolerasi
print(df.corr())

# informasi statistic seperti rata rata, mean, median, dll
print(df.describe())

# untuk memberikan informasi data kolom dll
print(df.info())

# menghitung informasi data kategori
# df.columns.value_counts() 


# menghitung rata rata kolom 
print(df.Usia.mean())

# menghitung median kolom 
print(df.Usia.median())

# menghitung jumlah total
print(df.Usia.count())


# menghitung missing value
print(df.isna().sum())


## preprocessing melakukan penanganan data kosong
# menghilangkan data yang kosong (drop missing value)
print(df.dropna())


# mengisi data kosong dengan "kosong" untuk string
print(df.filna("kosong"))

# bisa diisi untuk argumennya dictionary berdasarkan kolomnya (jika yang kosong di kolom...) 

# mengisi data yang kosong dengan rata2 / mean / dll (impute missing value)
df = df.filna(df.mean())
df.filna(df.median(), inplace=True)


# save to csv
df.to_csv("data/keluarga.csv", index_label="Nama") # index label untuk menyimpan seperti primary key
# jika tidak memiliki index label maka diisi argumen index=None



