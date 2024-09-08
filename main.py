from tkinter import *
from tkinter import messagebox
root = Tk()
root.resizable(0,0)
root.configure(bg="#000000")
root.title("awesome button")
root.geometry("300x300")

def the_func():
    m = messagebox.askokcancel("EXIT","Do you want to exit?")
    if m == True:
        exit()

b = Button(root,text="Exit",bg = "#FFFFFF",command=the_func).pack()
root.mainloop()