from sys import path
path.append(r"C:\Users\Rizal\Documents\Rekayasa Perangkat Lunak\projek diluar DDK\python\course lms\module_practice")

import modules.module as module

print("hello world")

isi = [i*i for i in range(1, 6)]
isi_dua = [i + (1+i) for i in range(5)]

print(isi)
print(isi_dua)


print(module.suml(isi))
print(module.prodl(isi_dua))

# print(module.counter)
