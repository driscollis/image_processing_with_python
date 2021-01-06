# watermark.py

from PIL import Image


def watermark(input_image_path, output_image_path,
              watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark_image = Image.open(watermark_image_path)
    # add watermark to your image
    base_image.paste(watermark_image, position)
    base_image.save(output_image_path)


if __name__ == "__main__":
    watermark("hummingbird.jpg", "hummingbird_watermarked.jpg",
              "logo.png", position=(0, 0))
