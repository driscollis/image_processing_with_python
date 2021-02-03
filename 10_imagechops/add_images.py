# add_images.py

from PIL import Image, ImageChops

def add_images(image_path_one, image_path_two, output_path,
               scale=1.0, offset=0):
    image_one = Image.open(image_path_one)
    image_two = Image.open(image_path_two)
    image_three = ImageChops.add(image_one, image_two, scale=scale, offset=offset)
    image_three.save(output_path)


if __name__ == "__main__":
    add_images("shell.png", "skyline.png",
               "added_images.jpg")