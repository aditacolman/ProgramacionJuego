from tkinter import *
from tkvideo import tkvideo
from functools import partial

root = Tk()
root.geometry('700x600')
root.resizable(width=False, height=False)
frameRespuesta = Frame(root)
frameRespuesta.pack()
labelVideo = Label(root)
labelVideo.pack()
reproductor = tkvideo("QUEVEDO.mp4", labelVideo, loop = 1, size = (700,720))
reproductor.play()


palabra2 = "hoola"
lista = []

root.title("¿?")

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
    respuesta = Entry(frameRespuesta, width=2, textvariable = entry_text,justify=CENTER)
    entry_text.trace("w", partial(limitador, entry_text))
    lista.append(respuesta)
    respuesta.grid(column=i,row=2)
    
lista[0].focus_set()

root.mainloop()