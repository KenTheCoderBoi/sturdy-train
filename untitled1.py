from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry=("1000x600")
root.title=("sus among us")

class CreateObject:
    def create(self):
        if select.get()=="Button":
            btn=Button(root,text="Donalds",command=self.eat)
            btn.pack()
        elif select.get()=="Label":
            label=Label(root,text="rick ashley")
            label.pack()
        elif select.get()=="Entry":
            entry=Entry(root,text="rick ashley")
            entry.pack()
    def eat(self):
        messagebox.showinfo("Hello sir mcdonalds is here","Hello sir you have ordered hamborgor")
order=CreateObject()
elements=["Label","Button","Entry"]
select=ttk.Combobox(root,values=elements)
select.pack()

btn=Button(root,text="create",command=order.create)
btn.pack()
root.mainloop()