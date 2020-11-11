# edge_enhance_image.py

from PIL import Image
from PIL import ImageFilter


def edge_enhance(input_image: str, output_image: str) -> None:
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
    filtered_image.save(output_image)


if __name__ == "__main__":
    edge_enhance("cactus.jpg", "cactus_edge.jpg")
