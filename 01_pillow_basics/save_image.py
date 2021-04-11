# save_image.py

import pathlib

from PIL import Image


def image_converter(input_file_path, output_file_path):
    image = Image.open(input_file_path)
    image.save(output_file_path)
    original_suffix = pathlib.Path(input_file_path).suffix
    new_suffix = pathlib.Path(output_file_path).suffix
    print(f"Converting {input_file_path} from {original_suffix} " 
          f"to {new_suffix}")

if __name__ == "__main__":
    image_converter("flowers.jpg", "flowers.png")