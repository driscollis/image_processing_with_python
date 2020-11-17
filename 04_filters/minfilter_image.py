# minfilter_image.py

from PIL import Image
from PIL import ImageFilter


def minfilter(input_image: str, output_image: str) -> None:
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.MinFilter(size=3))
    filtered_image.save(output_image)


if __name__ == "__main__":
    minfilter("giraffe.jpg", "giraffe_minfilter.jpg")
