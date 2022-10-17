from tkinter import *
import bd_utils
import requests
import json
import random
from tkvideo import tkvideo
from functools import partial
from pytube import YouTube
from tkvideo import tkvideo

class ScreenLogin:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Login Usuario")
        mainFrame = Frame(self.ventana)
        mainFrame.pack()
        titulo = Label(mainFrame, text="Login de Usuario", font=("Arial 24"))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        iniciarSesion = Button(mainFrame, command=self.verificar_uc, text="Iniciar sesión")
        iniciarSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        registroUsuario = Button(mainFrame, command=self.registrar_usuario, text="Registrar")
        registroUsuario.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        nombreLabel = Label(mainFrame, text="Nombre: ")
        nombreLabel.grid(column=0, row=1)
        contrasenaLabel = Label(mainFrame, text="Contraseña: ")
        contrasenaLabel.grid(column=0, row=2)
        self.nombreUsuario= StringVar()
        nombreEntry = Entry(mainFrame, textvariable=self.nombreUsuario)
        nombreEntry.grid(column=1, row=1)
        self.contrasenaUsuario= StringVar()
        contrasenaEntry = Entry(mainFrame, textvariable=self.contrasenaUsuario, show="*")
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
            sig= ScreenChoice()
        else:
            print("Faltan datos")

class ScreenChoice:
    
    def __init__(self):
        self.url_peli = ""
        self.url_serie = ""
        self.base = bd_utils.Base()
        self.ventana2 = Tk()
        self.ventana2.withdraw()
        self.ventana = Tk()
        self.ventana.title("")
        self.lista= []
        self.palabra2= ""
        self.mainFrame = Frame(self.ventana)
        self.mainFrame.pack()
        self.titulo = Label(self.mainFrame, text="Elección de juego", font=("Arial 24"))
        self.titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        self.mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        self.serieBoton = Button(self.mainFrame, text="Serie")
        self.serieBoton.grid(column=1, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        self.peliBoton = Button(self.mainFrame, command= self.sortear_pelicula, text="Pelicula")
        self.peliBoton.grid(column=0, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        print(self.ventana.deiconify())
    
    def sortear(self):
        url= "https://imdb-api.com/en/API/YouTubeTrailer/k_b4axdozw/{}"
        self.url_final= "https://imdb-api.com/en/API/MostPopularMovies/k_b4axdozw"
        azar = random.randint(0,99)
        response = requests.request("GET", self.url_final)
        dic = json.loads(response.text)
        id = dic['items'][azar]['id']
        response2= requests.request("GET", url.format(id))
        dic2 = json.loads(response2.text)
        self.palabra2 = dic2['title']
        print(self.palabra2)
        id_imdb = dic2['imDbId']
        self.url_sorteada = dic2['videoUrl']
        self.base.guardar_ps(id_imdb, self.palabra2, False, "", self.tipo, self.url_sorteada)
        url = self.url_sorteada
        print(url)
        video = YouTube(url)
        video_streams = video.streams.filter(file_extension ='mp4').get_by_itag(22)
        print("Descargando video")
        self.titulo = video_streams.download(filename = "1.mp4")
        video.streams[0].default_filename
        print("Video descargado")
                
    def reproductor(self):
        self.ventana.withdraw()
        self.ventana2.deiconify()
        self.frameRespuesta = Frame(self.ventana2)
        self.frameVideo = Frame(self.ventana2)
        self.frameRespuesta.pack()
        self.frameVideo.pack()
        self.labelVideo = Label(self.frameVideo)
        self.labelVideo.pack()
        nombre= self.titulo
        self.reproductor = tkvideo("{}".format(nombre), self.labelVideo, loop = 1, size = (640,480))
        self.reproductor.play()
        
        for i in range(len(self.palabra2)):
            self.entry_text = StringVar() 
            self.respuesta = Entry(self.frameRespuesta, width=2, textvariable = self.entry_text, justify=CENTER)
            self.entry_text.trace("w", partial(self.limitador, self.entry_text))
            self.lista.append(self.respuesta)
            self.respuesta.grid(column=i,row=0)
            self.verificarBoton = Button(self.frameRespuesta, text="ok", command=partial(self.valorar))
            self.verificarBoton.grid(column=0,row=1)
        
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
    
    def valorar(self):
        self.nombre = ""
        for i in self.lista:
            self.letra = i.get()
            self.nombre += self.letra
        if self.nombre.upper() == self.palabra2.upper():
            print("Ganaste")
        else:
            print("Perdiste")
        
        #self.ventana2.mainloop()
    
    def sortear_pelicula(self):
        self.tipo = "PELICULA"
        self.url_final= "https://imdb-api.com/en/API/MostPopularMovies/k_b4axdozw"
        self.sortear()
        self.reproductor()
        
    def sortear_serie(self):
        self.tipo = "SERIE"
        self.url_final = "https://imdb-api.com/en/API/MostPopularTVs/k_b4axdozw"
        self.sortear()
        self.reproductor()
        
    
inicio = ScreenChoice()