from tkinter import *
from tkvideo import tkvideo
from functools import partial

class Video:
    
    palabra2 = "hoola"
    lista = []
    def valorar(self):
        self.nombre = ""
        for i in self.lista:
            self.letra = i.get()
            self.nombre += self.letra
        if self.nombre.upper() == self.palabra2.upper():
            print("Ganaste")
        else:
            print("Perdiste")
    def videar(self):
        self.root = Tk()
        #root.geometry('700x600')
        self.root.resizable(width=False, height=False)
        self.frameRespuesta = Frame(self.root)
        self.frameRespuesta.pack()
        self.labelVideo = Label(self.root)
        self.labelVideo.pack()
        self.reproductor = tkvideo("QUEVEDO.mp4", self.labelVideo, loop = 1, size = (700,720))
        self.reproductor.play()
        self.root.mainloop()
    
    def entrear(self):
        self.root2= Tk()
        for i in range(len(self.palabra2)):
            self.entry_text = StringVar()  
            self.respuesta = Entry(self.root2, width=2, textvariable = self.entry_text, justify=CENTER)
            self.entry_text.trace("w", partial(self.limitador, self.entry_text))
            self.lista.append(self.respuesta)
            self.respuesta.grid(column=i,row=0)
            self.verificarBoton = Button(self.root2, text="ok", command=partial(self.valorar))
            self.verificarBoton.grid(column=10,row=2)
    
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


if __name__ == "__main__":
    rp= Video()
    #rp.videar()
    rp.entrear()
    