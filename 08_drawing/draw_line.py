# draw_line.py

import random
from PIL import Image, ImageDraw


def line(image_path, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    colors = ["red", "green", "blue", "yellow",
              "purple", "orange"]

    for i in range(0, 100, 20):
        draw.line((i, 0) + image.size, width=5, fill=random.choice(colors))

    image.save(output_path)

if __name__ == "__main__":
    line("madison_county_bridge_2.jpg", "lines.jpg")