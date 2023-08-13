"""mencoba latihan image filtering"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\Rizal\Documents\Rekayasa Perangkat Lunak\projek diluar DDK\python\display untuk image\picture.jpg')

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(dst), plt.title('averanging')
plt.xticks([]), plt.yticks([])

plt.show()
