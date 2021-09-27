# draw_arc.py

from PIL import Image, ImageDraw


def arc(output_path):
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.arc((25, 50, 175, 200), start=30, end=250, fill="green")

    draw.arc((100, 150, 275, 300), start=20, end=100, width=5, 
             fill="yellow")

    image.save(output_path)

if __name__ == "__main__":
    arc("arc.jpg")