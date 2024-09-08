from tkinter import *
from tkinter import messagebox
root = Tk()
root.resizable(0,0)
root.configure(bg="#000000")

root.title("awesome button")
root.geometry("300x300")
b = Button(root,text="click me",bg = "#FFFFFF").pack()
root.mainloop()