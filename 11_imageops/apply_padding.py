# apply_padding.py

from PIL import Image, ImageOps


def pad(image_path, output_path, size):
    image = Image.open(image_path)
    converted_image = ImageOps.pad(image, size=size, color="red")
    converted_image.save(output_path)


if __name__ == "__main__":
    pad("flowers.jpg", "flowers_padded.jpg", size=(1200, 600))