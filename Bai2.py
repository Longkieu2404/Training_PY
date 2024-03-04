import tkinter as tk
from tkinter import Button, Label, StringVar
from random import choice

def Noi_ten():
    Ho = ["Phan", "Kiều", "Trần"]
    Ten = ["Thịnh", "Long", "Tùng", "My", "Linh"]
    HoVaTen = choice(Ho) + " " + choice(Ten)
    result.set(HoVaTen)

root= tk.Tk()
root.title("Bài 2")

title = Label(root, text="Nhấn nút đỏ")
title.pack()

button = Button(root, text="Tell me!", bg="red", command=Noi_ten)
button.pack()

result = StringVar()
result_label = Label(root, textvariable=result)
result_label.pack()

root.mainloop()