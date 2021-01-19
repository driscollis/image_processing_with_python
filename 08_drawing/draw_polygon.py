# draw_polygon.py

from PIL import Image, ImageDraw


def polygon(output_path):
    image = Image.new("RGB", (400, 400), "grey")
    draw = ImageDraw.Draw(image)
    draw.polygon(((100, 100), (200, 50), (125, 25)), fill="green")

    draw.polygon(((175, 100), (225, 50), (200, 25)),
                  outline="yellow")

    image.save(output_path)

if __name__ == "__main__":
    polygon("polygons.jpg")