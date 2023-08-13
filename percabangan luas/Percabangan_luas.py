print("hallo, anda masuk perhitungan luas")
pilih = input("pilih luas apa ")
if pilih =="persegi":
    sisi = float(input("masukkan sisi: "))
    luas = sisi * sisi
elif pilih =="persegi panjang":
    panjang = float(input("masukkan panjang: "))
    lebar = float(input("masukkan lebar: "))
    luas = panjang * lebar
print("luasnya adalah", str(luas))