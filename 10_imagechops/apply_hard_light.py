# apply_hard_light.py

from PIL import Image, ImageChops

def hard_light(image_path_one, image_path_two, output_path):
    image_one = Image.open(image_path_one)
    image_two = Image.open(image_path_two)
    image_three = ImageChops.hard_light(image_one, image_two)
    image_three.save(output_path)


if __name__ == "__main__":
    hard_light("shell.png", "skyline.png",
               "hard_light.jpg")