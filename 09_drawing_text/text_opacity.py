# text_opacity.py

from PIL import Image, ImageDraw, ImageFont


def change_opacity(input_path, output_path):
    base_image = Image.open(input_path).convert("RGBA")

    txt_img = Image.new("RGBA", base_image.size, (255,255,255,0))
    font = ImageFont.truetype("Gidole-Regular.ttf", 40)
    draw = ImageDraw.Draw(txt_img)

    # draw text at half opacity
    draw.text((10,10), "Pillow", font=font, fill=(255,255,255,128))

    # draw text at full opacity
    draw.text((10,60), "Rocks!", font=font, fill=(255,255,255,255))

    composite = Image.alpha_composite(base_image, txt_img)
    composite.save(output_path)

if __name__ == "__main__":
    change_opacity("flowers_dallas.png", "flowers_opacity.png")