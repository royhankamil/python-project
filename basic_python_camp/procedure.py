"""
procedure merupakan sebuah fungsi yang tak mengembalikan / mereturn value apapun
jadi procedure hanya akan melakukan perintah yang ada di dalam fungsi
"""


"""contoh prosedur"""
def greetings(name):
    print("Halo " + name + ", Selamat Datang!")

"""mendefinisikan prosedure"""

# yang sebenarnya terjadi
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
    return

"""memanggil procedure"""
greeting("Dicoding Indonesia")


def sapa():
    print("Halo Selamat Datang!")

sapa()


