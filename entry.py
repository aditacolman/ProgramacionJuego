from tkinter import *
from random import randint
import random
from tkinter.messagebox import *
from tkinter import ttk

gui = Tk()
gui.geometry("200x200+50+50") 

zona_c = Canvas(gui, width = 200, height = 200) 
zona_c.pack()

entry_text = StringVar() 
entry_widget = Entry(zona_c, width = 20, textvariable = entry_text,justify=CENTER) 
zona_c.create_window(100, 100, window = entry_widget)

def limitador(entry_text):
    if len(entry_text.get()) > 0:
        #donde esta el :5 limitas la cantidad d caracteres
        entry_text.set(entry_text.get()[:1])

entry_text.trace("w", lambda *args: limitador(entry_text))
gui.mainloop()
 
 
''' 
letrasUsadas=[]
 
vidas= 7
 
def probarLetraFuncion():
    global vidas
    letrasUsadas.append(letraObtenida.get())
    print(letrasUsadas)
    if letraObtenida.get() in palabra:
        if palabra.count(letraObtenida.get())>0:
          #  letrasAcertadas+=palabra.count(letraObtenida.get())  #
            for i in range(len(palabra)):
                if palabra[i]==letraObtenida.get():
                    guiones[i].config(text=""+letraObtenida.get())
            else:
                guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get())
    else:
        vidas-=1
        if vidas==0:
            showwarning(title="Derrota",message="Se te acabaron las vidas")
 
 
raiz = Tk()
 
archivo = open("palabras.txt","r")
conjuntoPalabras= list(archivo.read().split("\n"))
palabra = conjuntoPalabras[random.randint(0,len(conjuntoPalabras)-1)].lower()
letraObtenida=StringVar()
 
 
raiz.config(width=1000, height = 600, bg="blue",relief = "groove",bd=10)
juegoFrame = Frame(raiz)
juegoFrame.config (width=1000, height = 600,relief = "sunken",bd=15)
juegoFrame.grid_propagate(False)
 
juegoFrame.pack()
 
Label(juegoFrame,text= "Introduce una letra", font=("Verdana", 24), #Cartel en Pantalla.
    ).grid(row=0, column=0,padx=10,pady=10)
letra= Entry(juegoFrame,width=1,font=("Verdana", 24),textvariable=letraObtenida
             ). grid(row=0, column=1,padx=10,pady=10)
probarLetra = Button(juegoFrame,text="Probar",bg="yellow",command=probarLetraFuncion
                     ).grid(row=1,column=0,pady=10)
 
guiones = [Label(juegoFrame,text="_",font=("verdana",30)) for  _ in palabra ]
 
 
 
 
inicialX=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialX,y=400)
    inicialX+=50
 
 
 
 
Label(juegoFrame,text= " 7 vidas.", font=("Verdana", 24), #DUDA ACA
    ).grid(row=0, column=80,padx=10,pady=10)
 
 
 
 
 
raiz.mainloop()
'''