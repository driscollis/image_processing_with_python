# blur_image.py

from PIL import Image
from PIL import ImageFilter


def blur(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.BLUR)
    filtered_image.save(output_image)


if __name__ == "__main__":
    blur("butterfly.jpg", "butterfly_blurred.jpg")
