# mirror_image.py

from PIL import Image


def mirror(image_path, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)


if __name__ == "__main__":
    image = "mantis.jpg"
    mirror(image, "mantis_mirrored.jpg")
