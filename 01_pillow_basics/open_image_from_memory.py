# open_image_from_memory.py

import io
import urllib.request

from PIL import Image

# Use a real URL to an image here:
url = "http://my_url/photo.jpg"
f = urllib.request.urlopen(url)
data = f.read()

with Image.open(io.BytesIO(data)) as image:
    image.show("Downloaded Image")