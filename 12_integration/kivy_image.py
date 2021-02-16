# kivy_image.py

from kivy.app import App
from kivy.uix.image import Image

class ImageViewer(App):

    def build(self):
        return Image(source="pink_flower.jpg")

# run the App
ImageViewer().run()
