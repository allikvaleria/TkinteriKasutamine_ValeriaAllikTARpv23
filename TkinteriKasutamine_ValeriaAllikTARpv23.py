from cProfile import label
from msilib.schema import RadioButton
from tkinter import *
k=0
def vajuta():
    global k 
    k+=1 
    nupp.configure(text=k)
def vajuta_(event):
    global k
    k-=1
    nupp.configure(text=k)
def tst_psse(event):
    t=textbox.get()
    pealkiri.configure(text=t,width=len(t))
    textbox.delete(0,END)

def valik():
    arv=var.get()
    textbox.insert(END,arv) 

aken=Tk()         #root
aken.geometry("400x600")   #razmek okna
aken.iconbitmap('diamond.ico')
aken.title("Tkinteri kasutamine")
tekst="Pealkiri\n"
pealkiri=Label(aken,
               text=tekst,
               bg="#b9f2ff",
               fg="#000000",
               font="Algerian 20",
               height=3,width=len(tekst),
               cursor="watch")
textbox=Entry(aken,
              bg="#e0ffff",
              fg="#000000",
              font="Algerian 20",
              width=20,
              justify=CENTER) #show="*"
nupp=Button(aken,
            text="Vajuta mind!",
            font="Arial 20",
            height=3,width=10,
            relief=RAISED, #SUNKEN, GROOVE
            bg="darkred",
            command=vajuta)  
f=Frame(aken)
var=IntVar()   #StringVar(), BoolVar()
e=Radiobutton(f,text="Esimene",variable=var,value=1,font="Arial 20",command=valik)
t=Radiobutton(f,text="Teine",variable=var,value=2,font="Arial 20",command=valik)
ko=Radiobutton(f,text="Kolmas",variable=var,value=3,font="Arial 20",command=valik)
nupp.bind("<Button-3>",vajuta_)    #pkm
textbox.bind("<Return>",tst_psse)  #enter

obj=[pealkiri,textbox,nupp,f] 
for i in obj:
    i.pack() 
obj2=[e,t,ko]
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=i)


#pealkiri.pack()
#textbox.pack()
#nupp.pack()

aken.mainloop()