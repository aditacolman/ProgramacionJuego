import vlc
from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.widget import Widget
 
class VideoWindow(App):
    def build(self):
        video = Video(source='QUEVEDO.mp4')
        video.state = 'play'
        video.options = {'eos': 'loop'}
        video.allow_stretch = True
        video.duration(10)
        return video
 
if __name__ == "__main__":
    window = VideoWindow()
    window.run()

'''
#vlc
video= "1.mp4"
media = vlc.MediaPlayer(video)
media.play()
'''
