"""membuat image menjadi gaussian filter"""
import pylab, os
from PIL import Image
from scipy.ndimage import filters

im = pylab.array(Image.open(os.path.dirname(__file__)+'\\picture.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
pylab.imshow(im2)
pylab.show()
