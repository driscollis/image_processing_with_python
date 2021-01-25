# draw_truetype.py

from PIL import Image, ImageDraw, ImageFont


def text(input_image_path, output_path):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    y = 10
    for font_size in range(12, 75, 10):
        font = ImageFont.truetype("Gidole-Regular.ttf", size=font_size)
        draw.text((10, y), f"Chihuly Exhibit ({font_size=})", font=font)
        y += 35
    image.save(output_path)

if __name__ == "__main__":
    text("chihuly_exhibit.jpg", "truetype.jpg")