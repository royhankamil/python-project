"""
PEP atau Python Enhancement Proposals merupakan panduan yang telah menjadi acuan untuk perkembangan Python.
Lint adalah proses pengecekan kode atas kemungkinan terjadi kesalahan (error), termasuk dalam proses
ini adalah mengecek kesesuaian terhadap arahan gaya penulisan kode (style guide) PEP8.
"""

# # coba untuk testing kode yang akan diuji
# class Kalkulator:
#     """kalkulator tambah kurang"""
#     def __init__(self, _i):
#         self.i = _i
#     def tambah(self, _i): return self.i + _i
#     def kurang(self, _i):
#     return self.i - _i


"""
penginstalan linter / aplikasi lint
pip install pycodestyle


pengujian dengan pycodestyle
pycodestyle file.py
"""

# setelah diperbaiki akan seperti ini
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
 
    def tambah(self, _i): return self.i + _i
 
    def kurang(self, _i):
        return self.i - _i

"""
Jika diproses menggunakan pycodestyle dan flake8, itu tidak akan memunculkan pesan seperti hasil
di bawah ini. Hal ini berarti menjelaskan kodenya sudah lebih baik.
"""

