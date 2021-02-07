# apply_colorize.py

from PIL import Image, ImageOps


def colorize(image_path, output_path, black, white):
    image = Image.open(image_path)
    converted_image = ImageOps.colorize(image, black, white)
    converted_image.save(output_path)


if __name__ == "__main__":
    colorize("gray_caterpillar.jpg", "color_caterpillar.jpg",
             black="green", white="white")