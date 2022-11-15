import tkinter
from tkvideonew import tkvideo
from functools import partial
from pytube import YouTube
import random
import json
import requests
import bd_utils
from PIL import ImageTk, Image

class VentanaLogin:

    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Login Usuario")
        mainFrame = tkinter.Frame(self.ventana)
        mainFrame.pack()
        titulo = tkinter.Label(mainFrame, text="Login de Usuario", font=("Arial 24"))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        iniciarSesion = tkinter.Button(mainFrame, command=self.verificar_uc, text="Iniciar sesión")
        iniciarSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        registroUsuario = tkinter.Button(mainFrame, command=self.registrar_usuario, text="Registrar")
        registroUsuario.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        nombreLabel = tkinter.Label(mainFrame, text="Nombre: ")
        nombreLabel.grid(column=0, row=1)
        contrasenaLabel = tkinter.Label(mainFrame, text="Contraseña: ")
        contrasenaLabel.grid(column=0, row=2)
        self.nombreUsuario= tkinter.StringVar()
        nombreEntry = tkinter.Entry(mainFrame, textvariable=self.nombreUsuario)
        nombreEntry.grid(column=1, row=1)
        self.contrasenaUsuario= tkinter.StringVar()
        contrasenaEntry = tkinter.Entry(mainFrame, textvariable=self.contrasenaUsuario, show="*")
        contrasenaEntry.grid(column=1, row=2)
        self.base = bd_utils.Base()
    
    def registrar_usuario(self):
        nombre= self.nombreUsuario.get()
        contrasena= self.contrasenaUsuario.get()
        if nombre and contrasena:
            resp = self.base.registro_usuario(nombre, contrasena)
            print(self.base.respuestas_registrousuario[resp])
        else:
            print("Faltan datos")
    
    def verificar_uc(self):
        nombre= self.nombreUsuario.get()
        contrasena= self.contrasenaUsuario.get()
        if nombre and contrasena:
            resp = self.base.iniciar_sesion(nombre, contrasena)
            print(self.base.respuestas_login[resp])
            self.ventana.state(newstate='withdraw')
            sig= VentanaJuego()
        else:
            print("Faltan datos")

class VentanaJuego:
    
    def __init__(self):
        self.ventanaPrincipal = tkinter.Tk()
        self.seccionFotoVid = tkinter.Frame(self.ventanaPrincipal)
        self.seccionBotones = tkinter.Frame(self.ventanaPrincipal)
        self.seccionFotoVid.grid(column=0, row=1)
        self.seccionBotones.grid(column=0, row=2)
        self.serieBoton = tkinter.Button(self.seccionBotones, command=self.sortear_serie, text="Serie")
        self.serieBoton.grid(column=1, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        self.peliBoton = tkinter.Button(self.seccionBotones, command=self.sortear_pelicula, text="Pelicula")
        self.peliBoton.grid(column=0, row=3, ipadx=2, ipady=2, padx=5, pady=5)        
        self.listaLetras = []
        self.url = ""
        self.nombre = ""
        self.nombreJuego = ""
        self.eleccion= {"PELICULA": self.sortear_pelicula, "SERIE": self.sortear_serie}
        self.ponerFoto()
        self.ventanaPrincipal.mainloop()
        
    def ponerFoto(self):
        self.portada = ImageTk.PhotoImage(file="fotoSP.jpg")
        self.portadaLabel = tkinter.Label(self.seccionFotoVid, image=self.portada)
        self.portadaLabel.pack()

    def ponerVideo(self):
        self.seccionLetras = tkinter.Frame(self.ventanaPrincipal)
        self.verificarBoton = tkinter.Button(self.seccionLetras, text="ok", command=partial(self.valorar))
        self.portadaLabel.destroy()
        self.labelVideo = tkinter.Label(self.seccionFotoVid)
        self.labelVideo.pack()
        self.reproductor = tkvideo(self.nombre, self.labelVideo, loop = 1, size = (640,480))
        self.ponerLetras()
        self.reproductor.play(100)
        #ocultar botones cuando se reproduce el video
        
    def ponerLetras(self):
        self.seccionLetras.grid(column=0, row=0)
        for i in range(len(self.nombreJuego)):
            self.entry_text = tkinter.StringVar() 
            self.respuesta = tkinter.Entry(self.seccionLetras, width=2, textvariable = self.entry_text, justify=tkinter.CENTER)
            self.entry_text.trace("w", partial(self.limitador, self.entry_text))
            self.listaLetras.append(self.respuesta)
            self.respuesta.grid(column=i,row=0)
            self.verificarBoton.grid(column=len(self.nombreJuego),row=0)
        #vaciar la lista para que se pueda volver a usar el limitador
    
    def limitador(self, *entry_text):
        pos = int(entry_text[1][6:])
        if(self.listaLetras[pos].get()):
            if pos < len(self.listaLetras)-1:
                self.listaLetras[pos+1].focus_set()
            if len(entry_text[0].get()) > 0:
                entry_text[0].set(entry_text[0].get()[:1].upper())
        else:
            self.listaLetras[pos-1].focus_set()
            if len(entry_text[0].get()) > 0:
                entry_text[0].set(entry_text[0].get()[:1].upper())
        #self.listaLetras = []
        
    def valorar(self):
        nombre = ""
        for i in self.listaLetras:
            letra = i.get()
            nombre += letra
        res = nombre.upper() == self.nombreJuego.upper()
        self.reproductor.destroy()
        self.seccionLetras.destroy()
        if res:
            print("Ganaste")
            self.eleccion[self.tipo]()
        else:
            print("Perdiste")
            self.ponerFoto()
        self.listaLetras = []
        
    def descargarVideo(self):
        url = self.url
        self.video = YouTube(url)
        video_streams = self.video.streams.filter(file_extension ='mp4').get_by_itag(22)
        self.nombre = video_streams.download()
        self.video.streams[0].default_filename
        self.ponerVideo()
        print(self.nombre)
    
    def sortear_pelicula(self):
        self.tipo = "PELICULA"
        self.url_final= "https://imdb-api.com/en/API/MostPopularMovies/k_b4axdozw"
        self.sortear()
        
    def sortear_serie(self):
        self.tipo = "SERIE"
        self.url_final = "https://imdb-api.com/en/API/MostPopularTVs/k_b4axdozw"
        self.sortear()
        
    def sortear(self):
        try:
            url= "https://imdb-api.com/en/API/YouTubeTrailer/k_b4axdozw/{}"
            azar = random.randint(0,99)
            response = requests.request("GET", self.url_final)
            dic = json.loads(response.text)
            id = dic['items'][azar]['id']
            response2= requests.request("GET", url.format(id))
            dic2 = json.loads(response2.text)
            self.nombreJuego = dic2['title']
            self.nombreJuego = self.nombreJuego.replace(" ","").lower()
            print(self.nombreJuego)
            id_imdb = dic2['imDbId']
            self.url = dic2['videoUrl']
            print(self.url)
            self.descargarVideo()
        except Exception as error_s:
            print(error_s)
            self.sortear_pelicula()

if  __name__ == "__main__":
    v = VentanaJuego()