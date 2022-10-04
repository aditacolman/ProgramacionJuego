from pytube import YouTube
from tkinter import *
from tkvideo import tkvideo

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
frameRespuesta.grid(column=0, row=1)
frameVideo.grid(column=0, row=0)
labelVideo = Label(frameVideo)
labelVideo.pack()
reproductor = tkvideo("{}".format(titulo), labelVideo, loop = 1, size = (640,480))
reproductor.play()


root.mainloop()



