# GUI (grafical user interface)
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

window = tk.Tk() #to set the window app
window.configure(bg = "gray") #set to color
window.geometry("800x600") # setting of width and height app
window.resizable(False, False) #can't be resize
window.title("Hello There") 

def Warning():
    the_message = "Your account has been hacked!!!\nplease do something!!!"
    showinfo(title = "Warning!!!", message = "Your passsword is incorrect, please input correct password")
    showwarning(title = "Warning!!!", message = the_message)
    window.quit()

#input
input_frame = ttk.Frame(window)
# parameternya (grid, pack, place)
input_frame.pack(padx = 40, pady = 40, fill = "x", expand = True)

#to create variabel string
USERNAME = tk.StringVar() 
PASSWORD = tk.StringVar()

#the componen
#for label
username_label = ttk.Label(input_frame, text = "Username")
username_label.pack(padx = 40, pady = 10,  fill = "x", expand = True)

#for entry or spot for input
USERNAME = tk.StringVar() #to create variabel string
username_entry = ttk.Entry(input_frame, textvariable = USERNAME) # textvariable is parameter must be in
username_entry.pack(padx = 40, pady = 20, fill = "x", expand = True)

password_label = ttk.Label(input_frame, text = "Password")
password_label.pack(padx = 40,pady = 10,  fill = "x", expand = True)

#for entry or spot for input
password_entry = ttk.Entry(input_frame, textvariable = PASSWORD) # textvariable is parameter must be in
password_entry.pack(padx = 40, pady = 20, fill = "x", expand = True)

hasil_button = ttk.Button(input_frame, text = "Login", command = Warning)
hasil_button.pack(padx = 40, pady = 20, expand = True)

window.mainloop()