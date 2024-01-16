import matplotlib.pyplot as plt
import numpy as np
from math import *

              
# a1 = np.array([0])
a1 = []
# a2 = np.array([10, 4, 4, 4])
for i in range(100):
    a1.append(i**2)

a2 = np.array(a1)

# a3 = a1 * a2
# a4 = a1 ** a2

# plt.plot(a1, marker="o")

plt.plot(a2)

# plt.plot(a3, marker="*")
# plt.plot(a4, marker="^")

plt.show()

a3 = a2 * -1


plt.plot(a3)

# plt.plot(a3, marker="*")
# plt.plot(a4, marker="^")

# akan mengubah scalanya dengan scala asli
plt.axis('equal')

plt.show()

# a4 = np.array([sin(i) for i in range(100)])


# plt.plot(a4)
# plt.show()
