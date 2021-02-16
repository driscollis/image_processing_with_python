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
        data = BytesIO()
        # Save PIL image to memory
        pil_image.save(data, format='png')

        # Read the data from memory into new BytesIO object
        data.seek(0)
        img_data = BytesIO(data.read())

        # Update Kivy Image
        image.texture = CoreImage(img_data, ext="png").texture
        image.reload()

        return image

# run the App
MyApp().run()
