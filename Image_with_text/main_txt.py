from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


window = tk.Tk() #to set the window app
window.configure(bg = "gray") #set to color
window.geometry("800x600+600+300") # setting of widthxheight+x+y => string x->x_window, y->y_window
window.resizable(False, False) #can't be resize
window.title("Text On Image") 

# isi parameter dengan menggunakan pack
"""
side : TOP (default), BOTTOM, LEFT, or RIGHT 
fill : NONE (default), X (fill horizontally), Y (fill vertically), BOTH
expand : YES, NO   => membuatnya di tengah ?
padx -> mengatur margin x, pady -> mengatur margin y, 
ipadx -> mengatur padding x, ipady -> mengatur padding y
"""

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

def remove():
    global hasil_button
    hasil_button.destroy()

button2 = ttk.Button(input_frame, text = "hapus", command = remove)
button2.pack(padx = 40, pady = 20, expand = True)

# isi parameter dengan grid
"""
Opsion(parameter): sticky -> membuat elemennya menempel di sisi grid, columns -> menentukan pada kolom berapa elemen tersebut
        row -> menentukan pada baris berapa elemen tersebut, columnspan(opsional) -> menentukan dalam satu element tersebut ingin
        mengisi berapa column, rowspan -> menentukan dalam satu element tersebut ingin mengisi berapa row, 
        padx ->margin x, pady ->margin y, ipadx -> padding x, ipady -> padding y
sticky (value) : Atas : n, Bawah : s, Kiri : w, Kanan : e
"""

# # kita membuat ada 5 kolom yang kita sediakan di dalam grid window
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)
# window.columnconfigure(3, weight=1)
# window.columnconfigure(4, weight=1)

# # kita membuat ada 2 baris yang kita sediakan di dalam grid window
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# button1 = tk.Button(text= "tes1")
# button2 = tk.Button(text= "tes2")
# button3 = tk.Button(text= "tes3")
# button4 = tk.Button(text= "tes4")

# button1.grid(column=0, row=0, sticky="we")
# button2.grid(column=1, row=0, columnspan=2)
# button3.grid(column=2, row=0, sticky="es")
# button4.grid(column=1, row=1, columnspan=5)



# isi parameter dengan place
"""
Optional : x ->menempatkan posisi x element(koordinat pixel), y ->menempatkan posisi y element(koordinat pixel), height ->mengatur tinggi elemen(px),
                width ->mengatur lebar elemmen(px), relwidth ->menagtur lebar dengan persentase layar(0-1), 
                relheight ->menagtur tinggi dengan persentase layar, relx ->memposisikan x sesuai dengan persentase layar,
                rely ->memposisikan y sesuai dengan persentase layar, anchor ->membuat pusat 0 berada di (kanan/kiri/...),
                bordermode ->mengatur apakah border diluar atau di dalam
anchor : N (atas), E (kanan), S (bawah), W (kiri), NE, NW, SE, or SW
bordermode : INSIDE, OUTSIDE
"""
window.mainloop()


