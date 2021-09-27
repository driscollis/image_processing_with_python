# enhance_sharpness.py

from PIL import Image
from PIL import ImageEnhance


def enhance_sharpness(image_path, enhance_factor, output_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Sharpness(image)
    new_image = enhancer.enhance(enhance_factor)
    new_image.save(output_path)


if __name__ == "__main__":
    enhance_sharpness("hummingbird.jpg", 2.5,
                      "hummingbird_sharpened.jpg")