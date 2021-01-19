from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter import scrolledtext
from food import *
from menu import *
import pickle
import datetime
import time

'''DECLARATIONS'''
win=Tk()
win.title("MESS : FOOD MANAGEMENT SYSTEM ")
win.geometry('2000x1000')

f1=Frame(win,width=600,height=200,relief=SUNKEN)
f2=Frame(win,width=800,height=600,relief=SUNKEN)
f3=Frame(win,width=400,height=150)
f4=Frame(win,width=200,height=50)
f1.pack()
f2.pack()
f3.pack()
f4.pack()

############################################################################################################################################################################################

localtime=time.asctime(time.localtime(time.time()))

Label(f1,font=('helvetica',50,'bold'),text="HOSTEL MESS FOOD MANAGEMENT ",fg="Black",bd=10,anchor='w').grid(row=0,column=0)

Label(f1,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w').grid(row=1,column=0)

############################################################################################################################################################################################

input_ing_cost=StringVar()
input_ing=StringVar()
output_ing=StringVar()
output_ing_cost=StringVar()

input_food_ing=StringVar()
input_food_name=StringVar()
output_food_cost=StringVar()
output_food_name=StringVar()


menu_food=StringVar()
menu_cost=StringVar()
menu_name=StringVar()

ingridients={}      #DICTIONARY STORING INGRIDIENTS AND THERE COST

###########################################################################################################################################################################################
'''FUNCTIONS'''
###########################################################################################################################################################################################
'''THIS FUNCTION TAKES INGRIDIENT INPUT AND APPENDS THEM INTO FILE'''
def input_ingridients():
    ingridients={}
    try:
        file=open("ingridients.txt","r")
        s=file.read()
        ingridients=eval(s)
        file.close()
    except Exception as e:
        print(e)
    else:
        pass
    ingridients[input_ing.get()]=eval(input_ing_cost.get())
    file1=open("ingridients.txt","w")
    file1.write(str(ingridients))
    file1.close()

def get_ingridient_food():
    l=[]
    item=input_food_ing.get()
    l.append(item)

def Convert(string):
    li = list(string.split(" ")) 
    return li 

def output_ingridients():
    abc=open("ingridients.txt","r").read()
    top=Toplevel()
    top.title("INGRIDIENTS AND COST ")
    T=Text(top,height=20,width=100)
    T.pack()
    T.insert(END,abc)

def input_food():
    x=input_food_name.get()
    ct=0
    p=0
    l=[]
    s=open("ingridients.txt","r").read()
    d=eval(s)
    item=input_food_ing.get()
    l=Convert(item)
    Ff=Food(x,l,d)
    i=0
    for i in l: 
        ct=ct+d[i]
    output_food_cost.set(ct)
    try:
        pout=open("Foods.pickle","ab")
        pickle.dump(Ff,pout)
        pout.close()
    except Exception as e:
        message = e
        print(message)
    else:
        pout=open("Foods.pickle","wb")
        pickle.dump(Ff,pout)
        pout.close()

def show_food_name_cost():
    f1=open("Foods.pickle","rb")
    l=[]
    ct=[]
    x=""
    while 1:
        try:
            f2=pickle.load(f1)
            x=x+f2.name
            ct.append(f2.get_cost())
            x=x+" "
        except(EOFError):
            break
    l=Convert(x)
    l.pop()
    d={}
    i=0

    try:
        file=open("foods_costs.txt","r")
        s=file.read()
        d=eval(s)
        file.close()
    except Exception as e:
        message = e
        print(message)
    else:
        pass  
    while i<len(ct):
        d[l[i]]=eval(str(ct[i]))
        i=i+1
    #print(d)
    file1=open("foods_costs.txt","w")
    file1.write(str(d))    
    file1.close()
    top=Toplevel()
    top.title("FOODS AND COST ")
    abc=open("foods_costs.txt","r").read()
    T=Text(top,height=20,width=100)
    T.pack()
    T.insert(END,abc)


def add_menu():
    x=menu_name.get()
    ct=0
    p=0
    l=[]
    s=open("foods_costs.txt","r").read()
    d=eval(s)
    item=menu_food.get()
    l=Convert(item)
    Mm=Menu(x,l,d)
    i=0
    for i in l: 
        ct=ct+d[i]
    ct=Mm.get_mcost()
    menu_cost.set(ct)
    try:
        pout=open("Menus.pickle","ab")
        pickle.dump(Mm,pout)
        pout.close()
    except Exception as e:
        message = e
        print(message)
    else:
        pout=open("Menus.pickle","wb")
        pickle.dump(Mm,pout)
        pout.close()



def show_menu():
    f1=open("Menus.pickle","rb")
    l=[]
    ct=[]
    x=""
    while 1:
        try:
            f2=pickle.load(f1)
            x=x+f2.name
            ct.append(f2.get_mcost())
            x=x+" "
        except(EOFError):
            break
    l=Convert(x)
    l.pop()
    d={}
    i=0

    try:
        file=open("menus_costs.txt","r")
        s=file.read()
        d=eval(s)
        file.close()
    except Exception as e:
        message = e
        print(message)
    else:
        pass  
    while i<len(ct):
        d[l[i]]=eval(str(ct[i]))
        i=i+1
    #print(d)
    file1=open("menus_costs.txt","w")
    file1.write(str(d))    
    file1.close()
    top=Toplevel()
    top.title("MENUS AND COST ")
    abc=open("menus_costs.txt","r").read()
    T=Text(top,height=20,width=100)
    T.pack()
    T.insert(END,abc)





############################################################################################################################################################################################
'''WIDGETS'''
############################################################################################################################################################################################

'''INGRIDIENT I/O WIDGETS   : ROW:0'''
Label(f2,font=('arial', 16, 'bold'),text="INGRIDIENT NAME",bd=16,anchor="w").grid(column=0,row=0)  
Entry(f2,width=30,textvariable=input_ing,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=1,row=0)

Label(f2,font=('arial', 16, 'bold'),text="COST INGD",bd=16,anchor="w").grid(column=2,row=0)
Entry(f2,width=30,textvariable=input_ing_cost,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=3,row=0)

Button(f3,text="ADD INGRIDIENT",command=input_ingridients,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,bg="powder blue").grid(column=0,row=0)
Button(f3,text="PRINT INGRIDIENT",command=output_ingridients,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,bg="powder blue").grid(column=1,row=0)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''FOOD I/O WIDGETS   : ROW:1'''
Label(f2,font=('arial', 16, 'bold'),text="FOOD NAME",bd=16,anchor="w").grid(column=0,row=1)
Entry(f2,width=30,textvariable=input_food_name,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=1,row=1)

Label(f2,font=('arial', 16, 'bold'),text="FOOD INGD",bd=16,anchor="w").grid(column=2,row=1)
Entry(f2,width=30,textvariable=input_food_ing,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=3,row=1)

Label(f2,font=('arial', 16, 'bold'),text="MAKING COSTF",bd=16,anchor="w").grid(column=0,row=2)
Entry(f2,width=30,textvariable=output_food_cost,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=1,row=2)
    
Button(f3,text="ADD FOOD",command=input_food,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,bg="powder blue").grid(column=2,row=0)
Button(f3,text="SHOW FOODS",command=show_food_name_cost,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,bg="powder blue").grid(column=3,row=0)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''MENU I/O WIDGETS : ROW:2'''
Label(f2,font=('arial', 16, 'bold'),text="MENU NAME",bd=16,anchor="w").grid(column=0,row=3)
Entry(f2,width=30,textvariable=menu_name,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=1,row=3)

Label(f2,font=('arial', 16, 'bold'),text="MENU FOOD",bd=16,anchor="w").grid(column=2,row=3)
Entry(f2,width=30,textvariable=menu_food,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=3,row=3)

Label(f2,font=('arial', 16, 'bold'),text="MAKING COSTM",bd=16,anchor="w").grid(column=0,row=4)
Entry(f2,width=30,textvariable=menu_cost,bg="powder blue",font=('arial',16,'bold'),insertwidth=4).grid(column=1,row=4)

Button(f3,text="ADD MENU",command=add_menu,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,bg="powder blue").grid(column=4,row=0)
Button(f3,text="SHOW MENU",command=show_menu,padx=16,pady=8,bd=16,fg="black",font=('arial',10,'bold'),width=10,bg="powder blue").grid(column=5,row=0)

Button(f3,text="EXIT",command=quit,padx=16,pady=8,bd=16,fg="black",font=('arial',8,'bold'),width=10,bg="powder blue").grid(column=7,row=1,sticky=E)


###########################################################################################################################################################################################
'''END'''
###########################################################################################################################################################################################



win.mainloop()








