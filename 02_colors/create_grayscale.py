# create_grayscale.py

from PIL import Image


def grayscale(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert("L")
    gray_scale.save(output_image_path)


if __name__ == "__main__":
    grayscale("monarch_caterpillar.jpg", "gray_caterpillar.jpg")