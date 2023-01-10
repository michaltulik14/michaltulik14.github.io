from tkinter import * 
from bs4 import BeautifulSoup
import math


root = Tk()
root.geometry("600x600")            #window dimensions
root.configure(bg="#cccccc")        #configure window
root.title("Michał Tulik")          #window title
root.resizable(False,False)         #don't allow window resizing
root.iconbitmap("media/icon.ico")   #add icon

#test

def button_comand():
    x=int(entry1.get())
    y=int(entry2.get())
    z=int(entry3.get())

    delta = y**2 - (4*(x*z))
    print(delta)
    if delta<0:
        print("mniejsza od zera")
    elif delta==0:
        print("rowna zero")
        result = - (y/(2*x))
        result2 = "Miejsce x0 to ",result
        siema.config(text=result2) 
    else:
        x0 = (-y - math.sqrt(delta))/(2*x)
        x1 = (-y + math.sqrt(delta))/(2*x)
        print(x0," ",x1)

        result = "Miejsce x0 wynosi ",x0," a miejsca x1 to",x1

        siema.config(text=result)     

        a= 1231231

entry1 = Entry(root, width=20)
entry1.pack()

entry2 = Entry(root, width=20)
entry2.pack()

entry3 = Entry(root, width=20)
entry3.pack()


Button(root, text="Policz miejsca zerowe", command=button_comand).pack()

siema = Label(root, text="wynik")
siema.pack()


root.mainloop()                     #generate window
