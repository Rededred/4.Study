# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("400x300+300+250")

btn = Button(root,
             text="Hello",
             background="#555",
             foreground="red",
             padx="20",
             pady="8",
             font="16")
btn.pack()

root.mainloop()
