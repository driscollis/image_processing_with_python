# draw_rectangle.py

from PIL import Image, ImageDraw


def rectangle(output_path):
    image = Image.new("RGB", (400, 400), "blue")
    draw = ImageDraw.Draw(image)
    draw.rectangle((200, 100, 300, 200), fill="red")
    draw.rectangle((50, 50, 150, 150), fill="green", outline="yellow",
                   width=3)
    image.save(output_path)

if __name__ == "__main__":
    rectangle("rectangle.jpg")