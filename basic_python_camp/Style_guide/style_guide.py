"""Statement Gabungan"""
"""
Saat Anda membuat program dengan banyak statement, usahakan untuk tidak menggabungkan >1 
statement pada baris yang sama.
"""
# disarankan seperti ini
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# tak disarankan seperti ini
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()


# tak disarankan pula seperti ini
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()


# dan sangat tidak disarankan juga seperti ini
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()
try: something()
finally: cleanup()
do_one(); do_two(); do_three(long, argument,
                             list, like, this)
if foo == 'blah': one(); two(); three()


"""trailing commas"""
# trailing commas yakni dengan menambahkan koma dibelakang, ini bersifat opsional

# disarankan seperti ini
FILES = ('setup.cfg',)

# dan tidak disarankan seperti ini
FILES = 'setup.cfg',


# disarankan 
FILES = [
    'setup.cfg',
    'tox.ini',
    ]

initialize(FILES,
           error=True,
           )


# tidak disarankan
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)



"""Anotasi Fungsi"""

"""
Anotasi fungsi adalah fitur yang memungkinkan kita untuk menambahkan informasi tambahan tentang 
parameter dan return value dari sebuah fungsi. 
"""

# Perhatikan penggunaan spasi dari kedua kode berikut.
 
# Yes:
def munge(input: str):  # Menambahkan informasi parameter bertipe string
    pass
def munge() -> str:   # Menambahkan informasi return value bertipe string
    pass
 
# No:
def munge(input:str):  # Menambahkan informasi parameter bertipe string
    pass
def munge()->str:   # Menambahkan informasi return value bertipe string
    pass


def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    luas = panjang*lebar
    return luas

luas_satu = LuasPersegiPanjang(lebar=2)
print(luas_satu)

# Yes:
def LuasPersegiPanjang(panjang:int = 2, lebar=None):
    pass
 
# No:
def LuasPersegiPanjang(panjang: int=2, lebar = None):
    pass


# Yes:
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas
 
# No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas


"""
Jika kita membuat fungsi yang menggabungkan anotasi dengan nilai parameter, sebaiknya tetap
menggunakan spasi sebelum dan sesudah tanda sama dengan (=). Namun, ketika membuat fungsi biasa
tanpa adanya anotasi, sebaiknya tidak menggunakan spasi sebelum dan sesudah tanda sama dengan (=).
"""

