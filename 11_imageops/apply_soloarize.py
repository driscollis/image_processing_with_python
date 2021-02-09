# apply_solarize.py

from PIL import Image, ImageOps


def solarize(image_path, output_path, threshold=128):
    image = Image.open(image_path)
    converted_image = ImageOps.solarize(image, threshold=threshold)
    converted_image.save(output_path)


if __name__ == "__main__":
    solarize("jellyfish.jpg", "jelly_solarize.jpg")