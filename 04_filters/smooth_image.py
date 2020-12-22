# smooth_image.py

from PIL import Image
from PIL import ImageFilter


def smooth(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.SMOOTH)
    filtered_image.save(output_image)


if __name__ == "__main__":
    smooth("spider.jpg", "spider_smooth_more.jpg")
