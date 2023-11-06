import matplotlib.pyplot as plt
import numpy as np

"""create a single vector"""
# A = np.array([1, 1])

"""create a plot"""
# fig, ax = plt.subplots()

"""add the A to the plot"""
# #  (fromX, fromY, toX, toY, angles, scale_units, scale(vectorA * 1/scale), color)
# ax.quiver( 0, 0, A[0], A[1],  angles="xy", scale_units="xy", scale=1, color='r' )

"""set the x and y limits of the plot"""
# # poin view camera (must be on)
# ax.set_xlim([-2, 2])
# ax.set_ylim([-2, 2])

"""show the plot along with the grid"""
# plt.grid() # make some grid (optional)
# plt.show()


def Determinant(a1, a2, b1, b2):
    return Extensive(b1[0], b1[1], b2[0], b2[1]) / Extensive(a1[0], a1[1], a2[0], a2[1])
  

def Extensive(x1, y1, x2, y2)->float:
    # print(x1, y1, x2, y2)
    wide = abs(x1) + abs(x2)
    longe = abs(y1) + abs(y2)

    if (x1 != 0 and x2 != 0):
        if (x1 * (1/abs(x1)) + x2 * (1/abs(x2)) != 0):
            wide = max(x1, x2)

    if (y1 != 0 and y2 != 0):
        if (y1 * (1/abs(y1)) + y2 * (1/abs(y2)) != 0):
            longe = max(y1, y2)

    # print(wide, longe)
    return wide * longe

a1 = np.array([1, 0])
a2 = np.array([0, 1])

fig, ax = plt.subplots()

# plt.figure("vector awal")
# membuat sebuah vector yang ditampilkan dalam bentuk vector (arah)
ax.quiver( 0, 0, a1[0], a1[1], angles="xy", scale_units="xy", scale=1, color='r')
ax.quiver( 0, 0, a2[0], a2[1], angles="xy", scale_units="xy", scale=1, color='b')

# mengatur limit pada view grafik
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

plt.grid() # menambahkan grid

# plot 2

# plt.figure("vector sudah transformasi")
fig, ax = plt.subplots()

transform = np.array([[-1, 2],
                    [1, 1]])

b1 = transform * a1
b2 = transform * a2

b1 = np.array([b1[0][0], b1[1][0]])
b2 = np.array([b2[0][1], b2[1][1]])

ax.quiver( 0, 0, b1[0], b1[1], angles="xy", scale_units="xy", scale=1, color='r')
ax.quiver( 0, 0, b2[0], b2[1], angles="xy", scale_units="xy", scale=1, color='b')

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

plt.grid()
plt.show()
print()
print()




# print(a1 > a2, b1 > b2)

print("Determinant = ", Determinant(a1, a2, b1, b2))