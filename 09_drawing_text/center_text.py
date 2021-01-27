# center_text.py

from PIL import Image, ImageDraw, ImageFont


def center(output_path):
    width, height = (400, 400)
    image = Image.new("RGB", (width, height), "grey")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Gidole-Regular.ttf", size=12)
    text = "Pillow Rocks!"
    font_width, font_height = font.getsize(text)

    new_width = (width - font_width) / 2
    new_height = (height - font_height) / 2
    draw.text((new_width, new_height), text, fill="black")
    image.save(output_path)

if __name__ == "__main__":
    center("centered_text.jpg")