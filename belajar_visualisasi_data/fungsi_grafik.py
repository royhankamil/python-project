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
a2 = []
j = -50
for i in range(1000):
    j += 0.1
    a2.append(j) # value of x
    a1.append(j ** 2) # value of y

a1 = np.array(a1)
a2 = np.array(a2)

plt.figure("kuadrat")
plt.plot(a2, a1)

b1 = []
b2 = []
j = -50

for i in range(1000):
    j += 0.1
    b2.append(j) # value of x
    b1.append(j ** 2 * -1) # value of y

b1 = np.array(b1)
b2 = np.array(b2)

plt.figure("kuadrat negatif")
plt.plot(b2, b1)

plt.show()
