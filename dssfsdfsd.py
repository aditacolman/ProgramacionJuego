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
        self.peliBoton = Button(self.mainFrame, command= self.dr_pelicula, text="Pelicula")
        self.peliBoton = Button(self.mainFrame, command= self.sortear_pelicula, text="Pelicula")
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
        return self.url_peli
        
    def sortear(self):
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
        self.base.guardar_ps(id_imdb_serie, nombre_serie, False, "", "SERIE", self.url_serie)
        print ("Tráiler: {}".format(dicseries2['videoUrl']))
        self.reproductor()

    def dr_pelicula(self):
        self.ventana.withdraw()
        self.sortear_pelicula()
        url = self.url_peli
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
        print(self.titulo)
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
        self.reproductor = tkvideo("{}".format(self.titulo), self.labelVideo, loop = 1, size = (640,480))
        self.reproductor.play()
        self.ventana2.mainloop()
        #self.ventana2.mainloop()

    def sortear_pelicula(self):
        self.tipo = "PELICULA"
        self.url_final= "https://imdb-api.com/en/API/MostPopularMovies/k_b4axdozw"
        self.sortear()

    def sortear_serie(self):
        self.tipo = "SERIE"
        self.url_final = "https://imdb-api.com/en/API/MostPopularTVs/k_b4axdozw"
        self.sortear()
        self.reproductor()


inicio = ScreenChoice()
inicio.dr_pelicula()

