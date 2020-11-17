# boxblur_image.py

from PIL import Image
from PIL import ImageFilter


def boxblur(input_image: str, output_image: str) -> None:
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.BoxBlur(radius=2))
    filtered_image.save(output_image)


if __name__ == "__main__":
    boxblur("trex.jpg", "trex_boxblur.jpg")
