# apply_flip.py

from PIL import Image, ImageOps


def flip(image_path, output_path):
    image = Image.open(image_path)
    converted_image = ImageOps.flip(image)
    converted_image.save(output_path)


if __name__ == "__main__":
    flip("ducklings.jpg", "ducklings_flipped.jpg")