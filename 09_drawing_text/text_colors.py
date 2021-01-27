# text_colors.py

from PIL import Image, ImageDraw, ImageFont


def text_color(output_path):
    image = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(image)
    colors = ["green", "blue", "red", "yellow", "purple"]
    font = ImageFont.truetype("Gidole-Regular.ttf", size=12)
    y = 10
    for color in colors:
        draw.text((10, y), f"Hello from Pillow", font=font, fill=color)
        y += 35
    image.save(output_path)

if __name__ == "__main__":
    text_color("colored_text.jpg")