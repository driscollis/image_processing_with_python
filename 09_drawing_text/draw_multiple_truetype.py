# draw_multiple_truetype.py

import glob
from PIL import Image, ImageDraw, ImageFont


def truetype(input_image_path, output_path):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    y = 10
    ttf_files = glob.glob("*.ttf")
    for ttf_file in ttf_files:
        font = ImageFont.truetype(ttf_file, size=44)
        draw.text((10, y), f"{ttf_file} (font_size=44)", font=font)
        y += 55
    image.save(output_path)

if __name__ == "__main__":
    truetype("chihuly_exhibit.jpg", "truetype_fonts.jpg")