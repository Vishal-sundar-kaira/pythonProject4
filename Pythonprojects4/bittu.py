import tkinter
from tkinter import messagebox
top=tkinter.Tk()
def hellocallBack():
    messagebox.showinfo("hello python")
B=tkinter.Button(top,text="hello",command=hellocallBack)
B.pack()
top.mainloop()