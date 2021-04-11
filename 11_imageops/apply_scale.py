# apply_scale.py

from PIL import Image, ImageOps


def scale(image_path, output_path, factor):
    image = Image.open(image_path)
    converted_image = ImageOps.scale(image, factor)
    converted_image.save(output_path)


if __name__ == "__main__":
    scale("flowers.jpg", "flower_scaled.jpg", factor=0.6)