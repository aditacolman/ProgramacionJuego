from tkinter import *
import bd_utils
import requests
import json
import random
import time
from tkvideo import tkvideo
from functools import partial
from pytube import YouTube

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
        self.mainFrame = Frame(self.ventana)
        self.mainFrame.pack()
        self.titulo = Label(self.mainFrame, text="Elección de juego", font=("Arial 24"))
        self.titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        self.mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        self.serieBoton = Button(self.mainFrame, text="Serie")
        self.serieBoton.grid(column=1, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        self.peliBoton = Button(self.mainFrame, command= self.dr_pelicula, text="Pelicula")
        self.peliBoton.grid(column=0, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        print(self.ventana.deiconify())
    
    def sortear_pelicula(self):
        url= "https://imdb-api.com/en/API/YouTubeTrailer/k_b4axdozw/{}"
        url_peliculaspopulares= "https://imdb-api.com/en/API/MostPopularMovies/k_b4axdozw"
        peliazar=random.randint(0,99)
        response= requests.request("GET", url_peliculaspopulares)
        dicpelicula = json.loads(response.text)
        id_peliculas= dicpelicula['items'][peliazar]['id']
        response2= requests.request("GET", url.format(id_peliculas))
        dicpelicula2= json.loads(response2.text)
        nombre_peli = dicpelicula2['title']
        print(nombre_peli)
        id_imdb_peli = dicpelicula2['imDbId']
        self.url_peli = dicpelicula2['videoUrl']
        self.base.guardar_ps(id_imdb_peli, nombre_peli, False, "", "PELICULA", self.url_peli)
        print("Tráiler de las películas: {}".format(dicpelicula2['videoUrl']))

    def sortear_serie(self):
        url= "https://imdb-api.com/en/API/YouTubeTrailer/k_b4axdozw/{}"
        url_seriespopulares = "https://imdb-api.com/en/API/MostPopularTVs/k_b4axdozw"
        serieazar=random.randint(0,99)
        response3= requests.request("GET", url_seriespopulares)
        dicseries= json.loads(response3.text)
        id_series= dicseries['items'][serieazar]['id']
        response4= requests.request("GET", url.format(id_series))
        dicseries2 = json.loads(response4.text)
        nombre_serie = dicseries2['title']
        id_imdb_serie = dicseries2['imDbId']
        self.url_serie = dicseries2['videoUrl']
        self.base.guardar_ps(id_imdb_serie, nombre_serie, False, "", "SERIE", url_serie)
        print ("Tráiler de las series: {}".format(dicseries2['videoUrl']))
    
    def dr_pelicula(self):
        self.sortear_pelicula()
        url= self.url_peli
        self.video = YouTube(url)
        video_streams = self.video.streams.filter(file_extension ='mp4').get_by_itag(22)
        print("Descargando video")
        self.titulo = video_streams.download()
        self.video.streams[0].default_filename
        print(self.titulo)
        print("Video descargado")
            
        self.frameRespuesta = Frame(self.ventana2)
        self.frameVideo = Frame(self.ventana2)
        self.frameRespuesta.pack()
        self.frameVideo.pack()
        self.labelVideo = Label(self.frameVideo)
        self.labelVideo.pack()
        self.reproductor = tkvideo("rauw.mp4", self.labelVideo, loop = 1, size = (640,480))
        self.reproductor.play()
        self.ventana.mainloop()
        
    

class ScreenGame:  
            
    def __init__(self):
        self.palabra2 = "hola"
        self.lista = []
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.frameRespuesta = Frame(self.root)
        self.frameVideo = Frame(self.root)
        self.frameRespuesta.grid(column=0, row=1)
        self.frameVideo.grid(column=0, row=0)
        self.labelVideo = Label(self.frameVideo)
        self.labelVideo.pack()
        self.reproductor = tkvideo("ok.mp4", self.labelVideo, loop = 1, size = (640,480))
        self.reproductor.play()
    
        for i in range(len(self.palabra2)):
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
    
    def valorar(self):
        self.nombre = ""
        for i in self.lista:
            self.letra = i.get()
            self.nombre += self.letra
        if self.nombre.upper() == self.palabra2.upper():
            print("Ganaste")
        else:
            print("Perdiste")
            
