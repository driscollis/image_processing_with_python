# crop_image.py

from PIL import Image


def crop_image(image_path, coords, save_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(save_location)


if __name__ == "__main__":
    crop_image("green_mantis.jpeg",
               (302, 101, 910, 574),
               "cropped_mantis.jpg")
