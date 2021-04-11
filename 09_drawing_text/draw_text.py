# draw_text.py

from PIL import Image, ImageDraw, ImageFont


def text(output_path):
    image = Image.new("RGB", (200, 200), "green")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Hello from")
    draw.text((10, 25), "Pillow",)
    image.save(output_path)

if __name__ == "__main__":
    text("text.jpg")