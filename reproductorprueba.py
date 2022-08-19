import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer


from kivy.uix.video import Video


class MyVideoApp(App):

    def build(self):
        video = Video(source='QUEVEDO.mp4')
        video.state = 'play'
        video.position = (1000000)
        return video

if __name__ == '__main__':

    MyVideoApp().run()


'''
class VideoWindow(App):
    def build(self):
        video = Video(source='QUEVEDO.mp4')
        video.state = 'play'
        video.options = {'eos': 'loop'}
        video.allow_stretch = True
        return video
 
if __name__ == "__main__":
    window = VideoWindow()
    window.run()
'''