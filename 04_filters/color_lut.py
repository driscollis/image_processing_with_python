# color_lut_image.py

from PIL import Image
from PIL import ImageFilter


def color_lut(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.Color3DLUT(2, [0, 1, 2] * 8))
    filtered_image.save(output_image)


if __name__ == "__main__":
    color_lut("trex.jpg", "trex_lut.jpg")
