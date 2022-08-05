from pytube import YouTube
import vlc

yt = YouTube("https://www.youtube.com/watch?v=A_g3lMcWVy0")
yt.streams
resp = yt.streams.filter(file_extension='mp4')
len(resp)
resp[0].download()

