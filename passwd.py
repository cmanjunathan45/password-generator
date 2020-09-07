import random
import string
from tkinter import *
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Password Generator | Manjunathan C")
root.geometry("400x450")
root.config(bg="#1B75BB")
ico=PhotoImage(file="icon.png")
root.iconphoto(False,ico)
def click():
	str1=string.ascii_uppercase
	str2=string.ascii_lowercase
	str3=string.digits
	str4=["!","@","#","$","%","^","&","*","~","?","_"]
	words=[]
	words.extend(str1)
	words.extend(str2)
	words.extend(str3)
	words.extend(str4)
	random.shuffle(words)
	try:
		if(text.get()>0):
			try:
				passwd=("".join(words[0:(int(text.get()))]))
				text4pass=Text(root,font=("fontawesome",15,"bold italic"),bg="#27AAE1",height=5,width=25,borderwidth=5)
				text4pass.place(x=20,y=240)
				text4pass.insert(tk.END,passwd)

			except:
				text.delete(0,END)
				messagebox.showwarning("Error","Use only Numbers")
		def clear1():
			text4pass.delete(1.0,END)
		clear=Button(root,text="Clear",command=clear1,bg="#1B75BB",fg="#FFFFFF",font=("fontawesome",10,"bold italic")).place(x=170,y=370)
	except:
		messagebox.showwarning("Error","Use only positive values")
		text.delete(0,END)

label=Label(root,text="Password Generator",width=45,padx=20,pady=20,bg="#1B75BB",fg="#FFFFFF",font=("fontawesome",15,"bold italic")).pack()

label2=Label(root,text="Enter The Length of the Password",bg="#1B75BB",fg="#FFFFFF",font=("fontawesome",10,"bold italic")).place(x=65,y=80)
text=Entry(root,font=("fontawesome",15,"bold italic"),bg="#27AAE1",width=10,borderwidth=5)
text.place(x=120,y=120)
def clear2():
	text.delete(0,END)
genbut=Button(root,text="Generate",command=click,bg="#1B75BB",fg="#FFFFFF",font=("fontawesome",10,"bold italic")).place(x=150,y=170)
clear=Button(root,text="Clear",command=clear2,bg="#1B75BB",fg="#FFFFFF",font=("fontawesome",10,"bold italic")).place(x=80,y=170)
quit=Button(root,text="EXIT",command=root.quit,bg="#1B75BB",fg="#FFFFFF",font=("fontawesome",10,"bold italic")).place(x=250,y=170)
root.mainloop()