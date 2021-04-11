# save_image_with_compression.py

import pathlib

from PIL import Image


def image_quality(input_file_path, output_file_path, quality):
    image = Image.open(input_file_path)
    image.save(output_file_path, quality=quality, optimize=True)

if __name__ == "__main__":
    image_quality("blue_flowers.jpg",
                  "blue_flowers_compressed.jpg",
                  quality=95)