# Digital Clock Project - Python Tkinter

import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

def currentTime():
    string = time.strftime('%H: %M: %S %p \n %D')
    label.config(text=string)
    label.after(1000, currentTime)

label = tk.Label(
    root,
    font = ('calibri',50,'bold'),
    background='yellow',
    foreground='black'
)

label.pack(anchor='center')

currentTime()
root.mainloop()