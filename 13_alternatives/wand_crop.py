# wand_crop.py

from wand.image import Image


def crop(input_image_path, output_path, left, top, width, height):
    with Image(filename=input_image_path) as img:
        img.crop(100, 800, width=width, height=height)
        img.save(filename=output_path)


if __name__ == "__main__":
    crop("ducklings.jpg", "cropped.jpg", 100, 800, 800, 800)