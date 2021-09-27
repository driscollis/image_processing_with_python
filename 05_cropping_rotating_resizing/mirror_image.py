# mirror_image.py

from PIL import Image


def mirror(image_path, output_image_path):
    image = Image.open(image_path)
    mirror_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    mirror_image.save(output_image_path)


if __name__ == "__main__":
    image = "mantis.jpg"
    mirror(image, "mantis_mirrored.jpg")