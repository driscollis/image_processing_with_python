# draw_ellipse.py

from PIL import Image, ImageDraw


def ellipse(output_path):
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((25, 50, 175, 200), fill="red")

    draw.ellipse((100, 150, 275, 300), outline="black", width=5,
                 fill="yellow")

    image.save(output_path)

if __name__ == "__main__":
    ellipse("ellipse.jpg")