from tkinter import *
import funciones
from functools import partial
from tkvideo import tkvideo

palabra2 = "hoola"
lista = []

root = Tk()
root.title("¿?")


def valorar(lista):
    nombre = ""
    for i in lista:
        letra = i.get()
        nombre += letra
    if nombre.upper() == palabra2.upper():
        print("Ganaste")
    else:
        print("Perdiste")

def limitador(*entry_text):
    pos = int(entry_text[1][6:])
    if(lista[pos].get()):
        if pos < len(lista)-1:
            lista[pos+1].focus_set()
        if len(entry_text[0].get()) > 0:
            entry_text[0].set(entry_text[0].get()[:1].upper())
    else:
        lista[pos-1].focus_set()
        if len(entry_text[0].get()) > 0:
            entry_text[0].set(entry_text[0].get()[:1].upper())

for i in range(len(palabra2)):
    entry_text = StringVar()  
    respuesta = Entry(root, width=2, textvariable = entry_text,justify=CENTER)
    entry_text.trace("w", partial(limitador, entry_text))
    lista.append(respuesta)
    respuesta.grid(column=i,row=0)

b_guardar = Button(root, text="ok", command=partial(valorar, lista))
b_guardar.grid(column=10, row=0)
lista[0].focus_set()

root.mainloop()




'''
#def construir_pantalla():
root = tk.Tk()
root.title("Banderas")
f1 = tk.Frame(root)
f1.grid(column=0, row=0)
f2 = tk.Frame(root)
f2.grid(column=0, row=1)
f3 = tk.Frame(root)
f3.grid(column=0, row=2)
label = tk.Label(f1)
label.grid(column=0, row=0)
    #return (f1,f2,f3, label, root)
root.mainloop()

lista = []

palabra2 = "hoola"

for i in range(len(hola)):
    entry_text = tk.StringVar()  
    i_nombre = tk.Entry(f2, width=2, textvariable = entry_text,  justify=tk.CENTER)
    entry_text.trace("w", partial(limitador,   entry_text))
    lista.append(i_nombre)
    i_nombre.grid(column=i,row=0)
    
def valorar(lista):
    nombre = ""
    for i in lista:
        letra = i.get()
        nombre += letra
    if nombre.upper() == nombre_pais.upper():
        print("Ganaste, sumaste un punto")
    else:
        print("Perdiste")
        
b_guardar = tk.Button(f3, text="ok", command=partial(valorar, lista))



#partes = construir_pantalla()
f1 = partes[0]
f2 = partes[1]
f3 = partes[2]
label = partes[3]
root = partes[4]



def valorar(lista):
    nombre = ""
    for i in lista:
        letra = i.get()
        nombre += letra
    if nombre.upper() == nombre_pais.upper():
        print("Ganaste, sumaste un punto")
    else:
        print("Perdiste")


def limitador(*entry_text):
    print(entry_text)
    pos = int(entry_text[1][6:])
    if(lista[pos].get()):
        if pos < len(lista)-1:
            lista[pos+1].focus_set()
        if len(entry_text[0].get()) > 0:
            entry_text[0].set(entry_text[0].get()[:1].upper())
    else:
        lista[pos-1].focus_set()
        if len(entry_text[0].get()) > 0:
            entry_text[0].set(entry_text[0].get()[:1].upper())



lista = []

for i in range(len(nombre_pais)):
    entry_text = tk.StringVar()  
    i_nombre = tk.Entry(f2, width=2, textvariable = entry_text,  justify=tk.CENTER)
    entry_text.trace("w", partial(limitador,   entry_text))
    lista.append(i_nombre)
    i_nombre.grid(column=i,row=0)
    
b_guardar = tk.Button(f3, text="ok", command=partial(valorar, lista))

b_guardar.grid(column=0, row=0)
lista[0].focus_set()
root.mainloop()

'''