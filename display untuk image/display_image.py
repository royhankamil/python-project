#sebuah program untuk display image (copy paste dari buku)
#by Mr. widodo
from PIL import Image
import pylab

#baca image ke array (harus ada r'tempat file')
im = pylab.array(Image.open(r'C:\Users\Rizal\Documents\Rekayasa Perangkat Lunak\projek diluar DDK\python\display untuk image\picture.jpg'))
#untuk plot image
pylab.imshow(im)

#untuk titik titik nya
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

#plot untuk penanda garis merah
pylab.plot(x, y, 'r*')
#line plot
pylab.plot(x[:2], y[:2])

#untuk menambahkan title
pylab.title('plot : for trying matplotlib')
pylab.show()
 
 
