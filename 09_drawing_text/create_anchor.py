# create_anchor.py

from PIL import Image, ImageDraw, ImageFont


def anchor(xy=(100, 100), anchor="la"):
    font = ImageFont.truetype("Gidole-Regular.ttf", 22)
    image = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(image)
    draw.line(((0, 100), (200, 100)), "gray")
    draw.line(((100, 0), (100, 200)), "gray")
    draw.text((100, 100), f"{anchor} Example", fill="black",
              anchor=anchor, font=font)
    image.save(f"anchor_{anchor}.jpg")

if __name__ == "__main__":
    anchor(anchor)