# draw_multiline_text_2.py

from PIL import Image, ImageDraw, ImageFont


def text(input_image_path, output_path):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Gidole-Regular.ttf", size=42)
    text = """
    Chihuly Exhibit
    Dallas, Texas"""
    draw.multiline_text((10, 25), text, font=font)
    image.save(output_path)

if __name__ == "__main__":
    text("chihuly_exhibit.jpg", "multiline_text_2.jpg")