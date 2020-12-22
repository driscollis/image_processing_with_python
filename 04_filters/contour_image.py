# contour_image.py

from PIL import Image
from PIL import ImageFilter


def contour(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.CONTOUR)
    filtered_image.save(output_image)


if __name__ == "__main__":
    contour("flowers_dallas.jpg", "flowers_contour.jpg")
