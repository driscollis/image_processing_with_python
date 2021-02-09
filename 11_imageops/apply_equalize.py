# apply_equalize.py

from PIL import Image, ImageOps


def equalize(image_path, output_path):
    image = Image.open(image_path)
    converted_image = ImageOps.equalize(image)
    converted_image.save(output_path)


if __name__ == "__main__":
    equalize("flowers.jpg", "flowers_equalized.jpg")