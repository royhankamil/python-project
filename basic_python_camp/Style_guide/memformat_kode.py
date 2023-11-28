"""format kode hampir mirip dengan PEP tetapi terdapat auto solve disini"""


class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i):
        return self.i + _i

    def kurang(self, _i):
        return self.i - _i


# menjalankan black (salah satu aplikasi memformat kode)
# black kalkulator.py
