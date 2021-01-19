# draw_pieslice.py

from PIL import Image, ImageDraw


def pieslice(output_path):
    image = Image.new("RGB", (400, 400), "grey")
    draw = ImageDraw.Draw(image)
    draw.pieslice((25, 50, 175, 200), start=30, end=250, fill="green")

    draw.pieslice((100, 150, 275, 300), start=20, end=100, width=5, 
                  outline="yellow")

    image.save(output_path)

if __name__ == "__main__":
    pieslice("pieslice.jpg")