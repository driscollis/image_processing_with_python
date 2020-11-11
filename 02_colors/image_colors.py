# image_colors.py

from PIL import Image


def get_image_colors(image_path):
    with Image.open(image_path) as image:
        colors = image.getcolors()

    return colors


if __name__ == "__main__":
    print(get_image_colors("cape_thick_knee.jpg"))
