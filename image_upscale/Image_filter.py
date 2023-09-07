from PIL import Image, ImageFilter, ImageDraw
from tkinter import filedialog

file_path = filedialog.askopenfilename()
# image = Image.open(os.path.dirname(__file__)+'\\great.jpg').filter(ImageFilter.SMOOTH_MORE)
image = Image.open(file_path).filter(ImageFilter.SMOOTH_MORE)
image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image = image.filter(ImageFilter.SHARPEN)
image = image.filter(ImageFilter.SMOOTH_MORE)

phistogram = image.histogram()
image.show()