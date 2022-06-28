import requests
import json
import random
from tkinter import *
import vlc
import pafy
import time
from pruebabd import guardar_ps, registrar_usuario

def sortear_pelicula():
    url= "https://imdb-api.com/en/API/YouTubeTrailer/k_b4axdozw/{}"
    url_peliculaspopulares= "https://imdb-api.com/en/API/MostPopularMovies/k_b4axdozw"
    peliazar=random.randint(0,99)
    response= requests.request("GET", url_peliculaspopulares)
    dicpelicula = json.loads(response.text)
    id_peliculas= dicpelicula['items'][peliazar]['id']
    response2= requests.request("GET", url.format(id_peliculas))
    dicpelicula2= json.loads(response2.text)
        
    nombre_peli = dicpelicula2['title']
    id_imdb_peli = dicpelicula2['imDbId']
    url_peli = dicpelicula2['videoUrl']
    guardar_ps(id_imdb_peli, nombre_peli, False, "", "PELICULA", url_peli)
    print("Tráiler de las películas: {}".format(dicpelicula2['videoUrl']))
    return url_peli

def sortear_serie():
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
    guardar_ps(id_imdb_serie, nombre_serie, False, "", "SERIE", url_serie)
    print ("Tráiler de las series: {}".format(dicseries2['videoUrl']))
    return url_serie

def iniciarpeli():
    try:
        url = sortear_pelicula()
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        
    except Exception as error_p:
        print(error_p)
        iniciarpeli()

def iniciarserie():
    try:
        url= sortear_serie()
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        
    except Exception as error_s:
        print(error_s)
        iniciarserie()

ventana = Frame(height=500, width=500)
ventana.pack()

#etiqueta= Label(text= "Juego").place(x=0, y=10)

boton1 = Button(ventana, command= iniciarpeli, text= "Película").place(x= 250, y=200)
boton2= Button(ventana, command= iniciarserie, text= "Serie").place(x= 50, y=200)

ventana.mainloop()
