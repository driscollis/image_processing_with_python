# color_changer.py

from PIL import Image
from PIL import ImageColor

def change_colors(image_path):
    with Image.open(image_path) as image:
        colors = image.getcolors(1000000)
        colors.sort()
        red = ImageColor.getcolor('red', 'RGBA')

        width, height = image.size
        color_to_replace = colors[-1][1]
        for x in range(width):
            for y in range(height):
                color = image.getpixel((x, y))
                if color == color_to_replace:
                    image.putpixel((x, y), red)

        image.save('changed_butterfly.png')

if __name__ == '__main__':
    print(change_colors('butterfly.jpg'))