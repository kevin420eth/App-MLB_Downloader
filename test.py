from tkinter import *
from tkinter import colorchooser
from tkinter import ttk


root = Tk()

root.title("This is the title")

root.geometry("400x200")

root.minsize(width=400,height=200)
root.maxsize(width=800,height=400)

btn =Button(text="Fuck me baby",background="skyblue")
btn.grid(column=1,row=1)

root.mainloop()