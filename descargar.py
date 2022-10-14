from pytube import YouTube
from tkinter import *
from tkvideo import tkvideo
'''
url = "https://www.youtube.com/watch?v=juRFjpB5Ppg"
video = YouTube(url)
video_streams = video.streams.filter(file_extension ='mp4').get_by_itag(22)
print("Descargando video")
titulo = video_streams.download(filename = "1.mp4")
video.streams[0].default_filename
print(titulo)

root = Tk()
root.resizable(width=False, height=False)
frameRespuesta = Frame(root)
frameVideo = Frame(root)
frameRespuesta.pack()
frameVideo.pack()
labelVideo = Label(frameVideo)
labelVideo.pack()
reproductor = tkvideo("{}".format(titulo), labelVideo, loop = 1, size = (640,480))
reproductor.play()
'''
class video:
    
    def __init__(self):
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
    
    def dr_pelicula(self):
        
        self.url= "https://www.youtube.com/watch?v=4I25nV9hXGA"
        video = YouTube(self.url)
        video_streams = video.streams.filter(file_extension ='mp4').get_by_itag(22)
        print("Descargando video")
        self.titulo = video_streams.download(filename = "1.mp4")
        video.streams[0].default_filename
        print(self.titulo)
        print("Video descargado")
            
        self.frameRespuesta = Frame(self.ventana)
        self.frameVideo = Frame(self.ventana)
        self.frameRespuesta.pack()
        self.frameVideo.pack()
        self.labelVideo = Label(self.frameVideo)
        self.labelVideo.pack()
        self.reproductor = tkvideo("{}".format(self.titulo), self.labelVideo, loop = 1, size = (640,480))
        self.reproductor.play()
        self.ventana.mainloop()

inicio= video()
inicio.dr_pelicula()



