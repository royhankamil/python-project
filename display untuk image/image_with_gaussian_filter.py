"""membuat image menjadi gaussian filter"""
import pylab
from PIL import Image
from scipy.ndimage import filters

im = pylab.array(Image.open(r'C:\Users\Rizal\Documents\Rekayasa Perangkat Lunak\projek diluar DDK\python\display untuk image\picture.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
pylab.imshow(im2)
pylab.show()
