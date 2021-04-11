# open_image_from_tar.py

from PIL import Image, TarIO

fobj = TarIO.TarIO("flowers.tar", "flowers.jpg")
image = Image.open(fobj)
image.show()