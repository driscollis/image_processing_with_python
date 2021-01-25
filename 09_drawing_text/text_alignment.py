# text_alignment.py

from PIL import Image, ImageDraw, ImageFont


def alignment(output_path):
    image = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(image)
    alignments = ["left", "center", "right"]
    y = 10
    font = ImageFont.truetype("Gidole-Regular.ttf", size=12)
    for alignment in alignments:
        draw.text((10, y), f"Hello from\n Pillow", font=font,
                align=alignment, fill="black")
        y += 35
    image.save(output_path)

if __name__ == "__main__":
    alignment("aligned_text.jpg")