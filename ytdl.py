from pytube import YouTube
import requests
import json
import random
from tkinter import *
import vlc
import pafy
import time
from bd_utils import Base

base = Base()

class Video:
    def __init__(self):
        self.url= "https://imdb-api.com/en/API/YouTubeTrailer/k_b4axdozw/{}"
        self.url_seriespopulares = "https://imdb-api.com/en/API/MostPopularTVs/k_b4axdozw"
        self.url_peliculaspopulares= "https://imdb-api.com/en/API/MostPopularMovies/k_b4axdozw"
        self.url_peli= ""
        self.url_serie= ""
        self.titulo= ""
    
    def sortear_pelicula(self):
        peliazar=random.randint(0,99)
        response= requests.request("GET", self.url_peliculaspopulares)
        dicpelicula = json.loads(response.text)
        id_peliculas= dicpelicula['items'][peliazar]['id']
        response2= requests.request("GET", self.url.format(id_peliculas))
        dicpelicula2= json.loads(response2.text) 
        nombre_peli = dicpelicula2['title']
        id_imdb_peli = dicpelicula2['imDbId']
        self.url_peli = dicpelicula2['videoUrl']
        base.guardar_ps(id_imdb_peli, nombre_peli, False, "", "PELICULA", url_peli)
        print("Tráiler de las películas: {}".format(dicpelicula2['videoUrl']))
        return self.url_peli

    def sortear_serie(self):
        serieazar=random.randint(0,99)
        response3= requests.request("GET", self.url_seriespopulares)
        dicseries= json.loads(response3.text)
        if dicseries['items']:         
            id_series= dicseries['items'][serieazar]['id']
            response4= requests.request("GET", self.url.format(id_series))
            dicseries2 = json.loads(response4.text)
            nombre_serie = dicseries2['title']
            id_imdb_serie = dicseries2['imDbId']
            url_serie = dicseries2['videoUrl']
            base.guardar_ps(id_imdb_serie, nombre_serie, False, "", "SERIE", url_serie)
            print ("Tráiler de las series: {}".format(dicseries2['videoUrl']))
        else:
            print("consultas agotadas, buscando en BD")
        return self.url_serie

    def descargar_peli(self, url):
        yt = YouTube(self.url_peli)
        yt.streams
        resp = yt.streams.filter(file_extension='mp4')
        len(resp)
        resp[0].download()
        self.titulo=resp[0].title
        print("Video descargado")
        return self.titulo

    def reproducir(self):
        media = vlc.MediaPlayer("{}.mp4".format(self.titulo))
        media.play()

v = Video()

#url= ["https://www.youtube.com/watch?v=Y-sv2E_MJ-g","https://www.youtube.com/watch?v=7GffFIMy91Q",
      #"https://www.youtube.com/watch?v=iewyrckGA7o", "https://www.youtube.com/watch?v=oZ1FN6VKUU8",
      #"https://www.youtube.com/watch?v=3FxlAwzRJw8"]

#v.reproducir("Bad Bunny - Me Porto Bonito (LetraLyrics)")

ventana = Frame(height=500, width=500)
ventana.pack()

    #etiqueta= Label(text= "Juego").place(x=0, y=10)

boton1 = Button(ventana, command= v.reproducir, text= "Película").place(x= 250, y=200)
#boton2= Button(ventana, command= v., text= "Serie").place(x= 50, y=200)

ventana.mainloop()


