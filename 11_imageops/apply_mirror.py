# apply_mirror.py

from PIL import Image, ImageOps


def mirror(image_path, output_path):
    image = Image.open(image_path)
    converted_image = ImageOps.mirror(image)
    converted_image.save(output_path)


if __name__ == "__main__":
    mirror("ducklings.jpg", "ducklings_mirrored.jpg")