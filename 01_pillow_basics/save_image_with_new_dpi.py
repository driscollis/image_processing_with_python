# save_image_with_new_dpi.py

import pathlib

from PIL import Image


def image_converter(input_file_path, output_file_path, dpi):
    image = Image.open(input_file_path)
    image.save(output_file_path, dpi=dpi)

if __name__ == "__main__":
    image_converter("blue_flowers.jpg", "blue_flowers_dpi.jpg",
                    dpi=(72, 72))
