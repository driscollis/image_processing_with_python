# create_4_color.py

from PIL import Image


def four_color(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert("P", palette=Image.ADAPTIVE, colors=4)
    gray_scale.save(output_image_path)


if __name__ == "__main__":
    four_color("monarch_caterpillar.jpg", "four_color_caterpillar.png")
