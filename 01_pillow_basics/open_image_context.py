# open_image_context.py

from PIL import Image

with Image.open("flowers.jpg") as image:
    image.show("flowers")
