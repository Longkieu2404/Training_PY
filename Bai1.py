import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk

root =tkinter.Tk()
root.title("Wanted!")

line_text = tkinter.Label(root, text="WANTED")
line_text.pack()

image = Image.open("./image/pikachu.jpg")
image_tk = ImageTk.PhotoImage(image)

im = tkinter.Label(root,image=image_tk)
im.pack()

root.mainloop()