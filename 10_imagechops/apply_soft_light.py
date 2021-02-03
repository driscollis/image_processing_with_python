# apply_soft_light.py

from PIL import Image, ImageChops

def soft_light(image_path_one, image_path_two, output_path):
    image_one = Image.open(image_path_one)
    image_two = Image.open(image_path_two)
    image_three = ImageChops.soft_light(image_one, image_two)
    image_three.save(output_path)


if __name__ == "__main__":
    soft_light("shell.png", "skyline.png",
               "soft_light.jpg")