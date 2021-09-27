# crop_image.py

from PIL import Image


def crop_image(image_path, coords, output_image_path):
    image = Image.open(image_path)
    cropped_image = image.crop(coords)
    cropped_image.save(output_image_path)


if __name__ == "__main__":
    crop_image("green_mantis.jpeg", 
               (302, 101, 910, 574), 
               "cropped_mantis.jpg")