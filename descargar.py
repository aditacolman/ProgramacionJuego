from pytube import YouTube

url = "https://www.youtube.com/watch?v=kLw1UrDqC9Q"
video = YouTube(url)
video_streams = video.streams.filter(file_extension ='mp4').get_by_itag(22)
video_streams.download(filename = "1")
print(video_streams)
'''
class R:
    def __init__(self):
        self.url= "https://www.youtube.com/watch?v=A_g3lMcWVy0"
        
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

    nombre= "/home/alcal/ProgramacionJuego{}"

#https://stackoverflow.com/questions/55348346/how-do-i-rename-the-downloaded-file-from-pytube-automatically
'''

