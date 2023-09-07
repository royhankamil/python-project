from PIL import Image, ImageDraw, ImageOps
from tkinter import filedialog

file_path = filedialog.askopenfilename()
image = Image.open(file_path).convert("L")
colorized_image = ImageOps.colorize(image, black = "green", white = "black")

image = image.convert("RGB")  # paramater can L, 1, P, RGB, LAB
# for i in range(image.size[1]):
#     for j in range((int)(image.size[0] * 1/4)):
#         x, y = j, i
#         pixel_color = (255, 0, 0)
#         image.putpixel((j, y), pixel_color)


# for drawing something
x1,x2,y1,y2 = 250, 100, 260, 200
draw = ImageDraw.Draw(image)
draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=50)

x1,x2,y1,y2 = 340, 560, 230, 130
draw2 = ImageDraw.Draw(image)
draw2.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=50)
phistogram = image.histogram()
image.show()
colorized_image.show()