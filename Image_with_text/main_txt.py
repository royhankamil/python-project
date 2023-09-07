from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


window = tk.Tk() #to set the window app
window.configure(bg = "gray") #set to color
window.geometry("800x600") # setting of width and height app
window.resizable(False, False) #can't be resize
window.title("Text On Image") 

def Choose():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    draw = ImageDraw.Draw(image)
    text = USERNAME.get()
    font = ImageFont.truetype("arial.ttf", (int)(image.size[0]/4 - text.__len__()), encoding="unic")
    koordinat = ((int)(image.size[0] / font.size),100)
    draw.text(koordinat, text, font=font, fill=(255,0,0), align="center")

    image.show()

#input
input_frame = ttk.Frame(window)
# parameternya (grid, pack, place)
input_frame.pack(padx = 40, pady = 40, fill = "x", expand = True)

#the componen
#for label
username_label = ttk.Label(input_frame, text = "Isi Text")
username_label.pack(padx = 40, pady = 8,  fill = "x", expand = True)

#for entry or spot for input
USERNAME = tk.StringVar() #to create variabel string
username_entry = ttk.Entry(input_frame, textvariable = USERNAME) # textvariable is parameter must be in
username_entry.pack(padx = 40, pady = 2, fill = "x", expand = True)

textPosX_label = ttk.Label(input_frame, text = "Text Position X")
textPosX_label.pack(padx = 40,pady = 8,  fill = "x", expand = True)

#for entry or spot for input
TEXTPOSX = tk.IntVar() #to create variabel string
textPosX_entry = ttk.Entry(input_frame, textvariable = TEXTPOSX) # textvariable is parameter must be in
textPosX_entry.pack(padx = 40, pady = 2, fill = "x", expand = True)

textPosY_label = ttk.Label(input_frame, text = "Text Position X")
textPosY_label.pack(padx = 40,pady = 8,  fill = "x", expand = True)

#for entry or spot for input
TEXTPOSY = tk.IntVar() #to create variabel string
textPosY_entry = ttk.Entry(input_frame, textvariable = TEXTPOSY) # textvariable is parameter must be in
textPosY_entry.pack(padx = 40, pady = 2, fill = "x", expand = True)


hasil_button = ttk.Button(input_frame, text = "Tambahkan Gambar", command = Choose)
hasil_button.pack(padx = 40, pady = 20, expand = True)

window.mainloop()


