# create_image.py

from PIL import Image
from PIL import ImageColor


def create_image(path, size):
    image = Image.new("RGBA", size)

    red = ImageColor.getcolor("red", "RGBA")
    green = ImageColor.getcolor("green", "RGBA")
    color = red

    count = 0
    for y in range(size[1]):
        for x in range(size[0]):
            if count == 5:
                # swap colors
                color = red if red != color else green
                count = 0
            image.putpixel((x, y), color)
            count += 1

    image.save(path)


if __name__ == "__main__":
    create_image("lines.png", (150, 150))
