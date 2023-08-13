"""percobaan pembuatan diplay image dengan filter contour"""

from PIL import Image
import pylab

#membuka image lalu dimasukkan ke array lalu konversi ke grayscale
im =  pylab.array(Image.open(r'C:\Users\Rizal\Documents\Rekayasa Perangkat Lunak\projek diluar DDK\python\display untuk image\great.jpg') .convert('L'))
#buat gambar baru 
pylab.figure()
#mengubah ke gray
pylab.gray()
#tampilan contour
pylab.contour(im, origin = 'image')
pylab.axis('equal')
pylab.axis('off')
pylab.figure()
pylab.hist(im.flatten(), 128)
pylab.show()
