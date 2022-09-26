from tkinter import *
from tkvideo import tkvideo
from functools import partial

class Video:
    
    
    
    def valorar(self):
        self.nombre = ""
        for i in self.lista:
            self.letra = i.get()
            self.nombre += self.letra
        if self.nombre.upper() == self.palabra2.upper():
            print("Ganaste")
        else:
            print("Perdiste")
            
    def __init__(self):
        self.palabra2 = "hoola"
        self.lista = []
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.frameRespuesta = Frame(self.root)
        self.frameVideo = Frame(self.root)
        self.frameRespuesta.grid(column=0, row=1)
        self.frameVideo.grid(column=0, row=0)
        
        self.labelVideo = Label(self.frameVideo)
        self.labelVideo.pack()
        self.reproductor = tkvideo("QUEVEDO.mp4", self.labelVideo, loop = 1, size = (640,480))
        self.reproductor.play()
        
    
        for i in range(len(self.palabra2)):
            print(i)
            self.entry_text = StringVar() 
            self.respuesta = Entry(self.frameRespuesta, width=2, textvariable = self.entry_text, justify=CENTER)
            self.entry_text.trace("w", partial(self.limitador, self.entry_text))
            self.lista.append(self.respuesta)
            self.respuesta.grid(column=i,row=0)
            self.verificarBoton = Button(self.frameRespuesta, text="ok", command=partial(self.valorar))
            self.verificarBoton.grid(column=0,row=1)
        self.root.mainloop()
        
    def limitador(self, *entry_text):
        pos = int(entry_text[1][6:])
        print(pos)
        if(self.lista[pos].get()):
            if pos < len(self.lista)-1:
                self.lista[pos+1].focus_set()
            if len(entry_text[0].get()) > 0:
                entry_text[0].set(entry_text[0].get()[:1].upper())
        else:
            self.lista[pos-1].focus_set()
            if len(entry_text[0].get()) > 0:
                entry_text[0].set(entry_text[0].get()[:1].upper())


if __name__ == "__main__":
    rp= Video()
