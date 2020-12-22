# rotate_image.py

from PIL import Image


def rotate(image_path, degrees_to_rotate, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)


if __name__ == "__main__":
    image = "dragonfly.jpg"
    rotate(image, 90, "dragonfly_rotated.jpg")
