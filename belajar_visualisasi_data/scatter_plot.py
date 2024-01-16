import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


print(os.getcwd())

data = pd.read_csv(os.getcwd()+"\\belajar_pandas\insurance.csv")

x = np.array([i for i in range(len(data.charges))])
y = data.charges.array

print(x)
print(y)

plt.scatter(x, y)
# plt.axis("equal")

plt.show()

# isi parameter c = color char misal "r", 'g, 'b 
# s = size (independent)
# cmap => perubahan warna
plt.scatter(x, y, c=x*2, s=x*2, cmap='seismic')
plt.axis("equal")

plt.show()

plt.scatter(x, y, c=x*2, s=x*2, cmap='seismic')

plt.show()

print()

