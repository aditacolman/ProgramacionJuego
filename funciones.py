from tkinter import *
import bd_utils
import requests
import json
import random
import time
from tkvideo import tkvideo
from functools import partial

def funcion():
    ventana.state(newstate='withdraw')
    #ventana.state(newstate='normal')

class Interfaz:
    indice = 0
    
    def __init__(self):
        self.tipos = [self.crear_ventana_sesion, self.crear_ventana_eleccion, self.crear_ventana_juego]
        self.siguiente()
        
    def crear_ventana_sesion(self):
        ventanaSesion = ScreenLogin()
        ventanaSesion.ventana.deiconify()
        return ventanaSesion

    def crear_ventana_eleccion(self):
        ventanaEleccion= ScreenChoice()
        ventanaEleccion.ventana.deiconify()
        #ventanaEleccion.withdraw()
        return ventanaEleccion
    
    def crear_ventana_juego(self):
        ventanaJuego= ScreenGame()
        #poner deiconify()
        #ventanaJuego.withdraw()
        return ventanaJuego
    
    def siguiente(self):
        ventAct = self.tipos[self.indice]()
        ventAct.ventana.mainloop()
        self.indice += 1
        self.windows[self.indice].ventana.deiconify()

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
        self.base = bd_utils.Base()
        self.ventana = Tk()
        self.ventana.title("")
        self.mainFrame = Frame(self.ventana)
        self.mainFrame.pack()
        self.titulo = Label(self.mainFrame, text="Elección de juego", font=("Arial 24"))
        self.titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        self.mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        self.serieBoton = Button(self.mainFrame, command= self.iniciarserie, text="Serie")
        self.serieBoton.grid(column=1, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        self.peliBoton = Button(self.mainFrame, command= self.iniciarpeli, text="Pelicula")
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
        url_peli = dicpelicula2['videoUrl']
        self.base.guardar_ps(id_imdb_peli, nombre_peli, False, "", "PELICULA", url_peli)
        print("Tráiler de las películas: {}".format(dicpelicula2['videoUrl']))
        return url_peli

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
        url_serie = dicseries2['videoUrl']
        self.base.guardar_ps(id_imdb_serie, nombre_serie, False, "", "SERIE", url_serie)
        print ("Tráiler de las series: {}".format(dicseries2['videoUrl']))
        return url_serie
    
    def iniciarpeli(self):
        try:
            url = self.sortear_pelicula()
            video = pafy.new(url)
            best = video.getbest()
            media = vlc.MediaPlayer(best.url)
            media.play()
            
        except Exception as error_p:
            print(error_p)
            self.iniciarpeli()
        self.ventana.state(newstate='withdraw')
        sig= ScreenGame()

    def iniciarserie(self):
        try:
            url= self.sortear_serie()
            video = pafy.new(url)
            best = video.getbest()
            media = vlc.MediaPlayer(best.url)
            media.play()
            
        except Exception as error_s:
            print(error_s)
            self.iniciarserie()
        
    

class ScreenGame:

    def __init__(self, nombre):
        self.ventana = Tk()
        self.ventana.title("")
        #self.ruta= ruta
        self.lista = []
        self.palabra2= nombre
        self.ventana.geometry('700x600')
        self.ventana.resizable(width=False, height=False)
        self.frameRespuesta = Frame(self.ventana)
        self.frameRespuesta.pack()
        self.labelVideo = Label(self.ventana)
        self.labelVideo.pack()
        self.reproductor = tkvideo("QUEVEDO.mp4", self.labelVideo, loop = 1, size = (700,720))
        self.reproductor.play()
        self.verificarBoton = Button(self.ventana, text="ok", command=partial(self.valorar))
        self.verificarBoton.pack()
        for i in range(len(self.palabra2)):
            self.entry_text = StringVar()  
            respuesta = Entry(self.ventana, width=2, textvariable = self.entry_text, justify=CENTER)
            self.entry_text.trace("w", partial(self.limitador))
            self.lista.append(respuesta)
            respuesta.pack()
            self.lista[0].focus_set()
        
    def valorar(self):
        nombre = ""
        for i in self.lista:
            letra = i.get()
            nombre += letra
        if nombre.upper() == self.palabra2.upper():
            print("Ganaste")
        else:
            print("Perdiste")

    def limitador(self):
        pos = int(self.entry_text[1][6:])
        if(self.lista[pos].get()):
            if pos < len(lista)-1:
                self.lista[pos+1].focus_set()
            if len(self.entry_text[0].get()) > 0:
                self.entry_text[0].set(self.entry_text[0].get()[:1].upper())
        else:
            self.lista[pos-1].focus_set()
            if len(self.entry_text[0].get()) > 0:
                self.entry_text[0].set(self.entry_text[0].get()[:1].upper())
                
if __name__ == "__main__":
    sg= ScreenGame("holahola")
   