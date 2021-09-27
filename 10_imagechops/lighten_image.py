# lighten_image.py

from PIL import Image, ImageChops

def lighten(image_path_one, image_path_two, output_path):
    image_one = Image.open(image_path_one)
    image_two = Image.open(image_path_two)
    image_three = ImageChops.lighter(image_one, image_two)
    image_three.save(output_path)


if __name__ == "__main__":
    lighten("shell.png", "skyline.png", "lighter_image.jpg")