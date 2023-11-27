import unittest
 
class TestStringMethods(unittest.TestCase):
    # Ini adalah test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')
    
    # Test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())
    
    # Test case ketiga (3)
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')
    
if __name__ == '__main__':
    # Test Runner
    unittest.main()


"""
hasil outputnya = Ran 3 tests in 0.002s

OK
"""


"""
1. Kelas TestStringMethods adalah sebuah kelas yang merupakan turunan (subclass) dari class unittest.
TestCase sehingga proses tes dapat dilangsungkan tanpa banyak implementasi lain.
2. Ada tiga metode pada class tersebut yang semua namanya diawali dengan kata test. Hal ini merupakan 
konvensi (aturan) yang wajib diikuti untuk menginformasikan ke test runner bahwa sejumlah metode tersebut 
merepresentasikan tes yang akan dioperasikan.
3. Pada setiap metode, pengujian dilakukan dengan pemanggilan assert. Pada metode test_strip pengecekan 
kesamaan menggunakan assertEqual dilakukan untuk memastikan bahwa 'www.dicoding.com'.strip('c.mow') sama 
dengan ‘dicoding’.
4. Pada metode test_isalnum pengecekan bahwa fungsi bernilai benar (True) dilakukan dengan assertTrue untuk 
memastikan jika 'c0d1ng'.isalnum() bernilai benar, yakni ‘cOd1ng’ adalah betul bertipe alfanumerik. Kemudian 
juga ada pengecekan bahwa fungsi bernilai salah (False) dengan assertFalse untuk memastikan jika 
'c0d!ng'.isalnum() betul bernilai salah karena ada karakter yang bukan alfanumerik yaitu ‘!’.
5. Pada metode test_index pengecekan kesamaan dilakukan seperti sebelumnya dengan menggunakan assertEqual 
bahwa pencarian substring coding menempati index sama dengan 2. Kemudian juga ada pengecekan bahwa ValueError 
akan dibangkitkan dengan menggunakan assertRaises(ValueError), jika pencarian index tidak berhasil ditemukan 
pada string yang sudah ditentukan.
6. Pada bagian terakhir kode, ada pemanggilan unittest.main() untuk mulai menjalankan test.
"""