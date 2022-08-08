from pytube import YouTube
import vlc

class R:
    def __init__(self):
        self.url= "https://www.youtube.com/watch?v=6Vn8BgjdhuI"
        
    def descargar_peli(self):
        yt = YouTube(self.url)
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

R= R()
R.descargar_peli()
R.reproducir()
