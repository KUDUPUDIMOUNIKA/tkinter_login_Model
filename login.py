import tkinter as tk
from tkinter import *
from tkinter import messagebox
def login():
    username = entry1.get()
    password = entry2.get()
    
    if(username == "" and password == ""):
        messagebox.showinfo("","Blank Not Allowed")
        
    elif(username == "Mounika" and password == "mouni@123"):
        messagebox.showinfo("","Login Success")
        root.destroy()
        
    else:
        messagebox.showinfo("","Invalid UserName and Password")
        
root = tk.Tk()
root.title("Login")
root.geometry("800x800")
root['background'] = 'grey'

global entry1
global entry2

Label(root,text = "User Name",bg="white",fg="black").place(x=20,y=20)
Label(root,text = "Password",bg="white",fg="black").place(x=20,y=70)

entry1 = Entry(root,bd = 5)
entry1.place(x=140,y=20)

entry2 = Entry(root,bd = 5)
entry2.place(x=140,y=70)
entry2.config(show="*")

Button(root,text = 'Login',command = login ,height=3,width=13,bd=6).place(x=100,y=120)

root.mainloop()

    