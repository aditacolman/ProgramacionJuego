from tkinter import *
import vlc
import pafy
import time
from random import randint


def iniciarpeli():
        url = "https://www.youtube.com/watch?v=_-HvOvavLrk"
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        time.sleep()
'''   
     except:
        url = "https://www.youtube.com/watch?v=Iizsdx_Y_BI"
        video = pafy.new(url)
        best = video.getbest()
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc.MediaPlayer(best.url)
        player.set_media(media)
        media.play()
        time.sleep(0.5)
        duration = player.get_length()
'''

def iniciarserie():
        url = "https://www.youtube.com/watch?v=jm1jT41L8fw"
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.set_fullscreen(True) 
        media.play()
        time.sleep()

'''
     except:
        url = "https://www.youtube.com/watch?v=Iizsdx_Y_BI"
        video = pafy.new(url)
        best = video.getbest()
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc.MediaPlayer(best.url)
        player.set_media(media)
        media.play()
        time.sleep(0.5)
        duration = player.get_length()
'''


ventana = Tk()
ventana.resizable(width=0, height=0)
f1 = Frame(ventana, height=100, width=200)
f2 = Frame(ventana, height=500, width=200)

f1.grid(row=0, column=0)
f2.grid(row=1, column=0)

etiqueta= Label(f1, text= "Juego").place(x=80, y=50)

boton1= Button(f2, command= iniciarpeli, text= "Película",width = 5, height = 2).grid(row = 1, column = 0)
boton2= Button(f2, command= iniciarserie, text= "Serie",width = 5, height = 2).grid(row = 1, column = 1)

palabra = input("Ingrese palabra: ").upper()
resultado = list(len(palabra) * "-")

ventana2= Tk()
ventana2.resizable(width=0, height=0)
Frame= Frame(ventana2)
Frame.pack()
Frame.config(width=10, height=10)
cuadrado= Entry(Frame).grid(column= 0, row=0)

#for i in range()


ventana.mainloop()
