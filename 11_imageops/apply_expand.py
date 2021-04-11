# apply_expand.py

from PIL import Image, ImageOps


def expand(image_path, output_path, border, fill):
    image = Image.open(image_path)
    converted_image = ImageOps.expand(image, border, fill)
    converted_image.save(output_path)


if __name__ == "__main__":
    expand("flowers.jpg", "flower_border.jpg", border=100, fill="yellow")