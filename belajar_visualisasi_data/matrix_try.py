import matplotlib.pyplot as plt
import numpy as np
from math import *

#               
# a1 = np.array([0])
# a2 = np.array([10, 4, 4, 4])


# a3 = a1 * a2
# a4 = a1 ** a2

# plt.plot(a1, marker="o")

# plt.plot(a2, marker="*")

# plt.plot(a3, marker="*")
# plt.plot(a4, marker="^")

a1 = []
for i in range(100):
    a1.append(i**2)

a2 = np.array(a1)

plt.plot(a1)

plt.show()
