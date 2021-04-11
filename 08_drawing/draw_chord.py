# draw_chord.py

from PIL import Image, ImageDraw


def chord(output_path):
    image = Image.new("RGB", (400, 400), "green")
    draw = ImageDraw.Draw(image)
    draw.chord((25, 50, 175, 200), start=30, end=250, fill="red")

    draw.chord((100, 150, 275, 300), start=20, end=100, width=5,
                fill="yellow", outline="blue")

    image.save(output_path)

if __name__ == "__main__":
    chord("chord.jpg")