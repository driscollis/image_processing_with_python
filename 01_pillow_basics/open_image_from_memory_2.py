# open_image_from_memory_2.py

import io

from PIL import Image

with open("flowers.jpg", "rb") as fp:
    data = fp.read()
    image = Image.open(io.BytesIO(data))
    image.show("flowers")
