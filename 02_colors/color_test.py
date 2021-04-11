# color_test.py

from PIL import ImageColor


def get_rgb_value(color_name):
    return ImageColor.getcolor(color_name, "RGBA")


if __name__ == "__main__":
    for color in ImageColor.colormap:
        print(f"{color} = {get_rgb_value(color)}")