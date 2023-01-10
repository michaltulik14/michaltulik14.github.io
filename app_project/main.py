from tkinter import * 
from fractions import Fraction
import math


root = Tk()
root.geometry("600x600")            #window dimensions
root.configure(bg="#cccccc")        #configure window
root.title("Michał Tulik")          #window title
root.resizable(False,False)         #don't allow window resizing
root.iconbitmap("media/icon.ico")   #add icon

frametop = Frame(root)
frametop.config(bg="#cccccc")
frametop.pack()



#test

def button_comand():
    output_result.config(text="")    #clearing previous results, in case they exist
    output_result2.config(text="")
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
        out_str = str(result)
        output_result.config(text="Istnieje 1 miesjce zerowe :  "+out_str)
    else:
        
        x0 = (-y - math.sqrt(delta))/(2*x)
        x1 = (-y + math.sqrt(delta))/(2*x)
        print(x0," ",x1)
        out_str1 = str(Fraction(x0).limit_denominator())            #converting a decimal number into fraction,
        out_str2 = str(Fraction(x1).limit_denominator())            #and converting to string
        result = "1 miejsce zerowe : "+out_str1
        result2= "2 miejsce zerowe : "+out_str2
        output_result.config(text=result)     
        output_result2.config(text=result2)  




entry1 = Entry(frametop, width=3, )
entry1.config(font=('Helvetica bold',20))
entry1.pack(ipadx=5,ipady=5,side=LEFT)

label1 = Label(frametop,text="x^2",width=2)
label1.config(font=('Helvetica bold',20),bg="#cccccc")
label1.pack(ipadx=5,ipady=5,side=LEFT)



entry2 = Entry(frametop, width=3,bg="white")
entry2.config(font=('Helvetica bold',20))
entry2.pack(ipadx=5,ipady=5,padx=5,pady=5,side=LEFT)

label2 = Label(frametop,text="x",width=2)
label2.config(font=('Helvetica bold',20),bg="#cccccc")
label2.pack(ipadx=5,ipady=5,side=LEFT)


entry3 = Entry(frametop, width=3)
entry3.config(font=('Helvetica bold',20))
entry3.pack(ipadx=5,ipady=5,side=LEFT)


submit = Button(frametop, text="Policz miejsca zerowe", command=button_comand)

submit.pack(ipadx=5,ipady=5,padx=50,pady=5,side=LEFT)

output_result = Label(root, text="")
output_result.config(font=('Helvetica bold',20),bg="#cccccc")
output_result.pack(side=TOP)

output_result2 = Label(root, text="")
output_result2.config(font=('Helvetica bold',20),bg="#cccccc")
output_result2.pack(side=TOP)




root.mainloop()                     #generate window
