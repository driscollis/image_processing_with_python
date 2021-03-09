# kivy_pillow_demo.py

from io import BytesIO
from kivy.app import App
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from PIL import Image as PilImage

class MyApp(App):

    def build(self):
        image = Image(source="")
        pil_image = PilImage.open("pink_flower.jpg")
        img_data = BytesIO()

        # Save PIL image to memory
        pil_image.save(img_data, format='png')
        img_data.seek(0)

        # Update Kivy Image
        image.texture = CoreImage(img_data, ext="png").texture
        image.reload()

        return image

# run the App
MyApp().run()
