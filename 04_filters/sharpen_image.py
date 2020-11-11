# sharpen_image.py

from PIL import Image
from PIL import ImageFilter


def sharpen(input_image: str, output_image: str) -> None:
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.SHARPEN)
    filtered_image.save(output_image)


if __name__ == "__main__":
    sharpen("grasshopper.jpg", "grasshopper_sharpened.jpg")
