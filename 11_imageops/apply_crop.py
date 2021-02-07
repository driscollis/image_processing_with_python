# apply_crop.py

from PIL import Image, ImageOps


def crop(image_path, output_path, border):
    image = Image.open(image_path)
    converted_image = ImageOps.crop(image, border)
    converted_image.save(output_path)


if __name__ == "__main__":
    crop("flower_border.jpg", "flower_no_border.jpg",
         border=100)