# create_bw_dithering.py

from PIL import Image


def black_and_white(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert("1", dither=0)
    gray_scale.save(output_image_path)


if __name__ == "__main__":
    black_and_white("monarch_caterpillar.jpg", "dither_caterpillar.jpg")
