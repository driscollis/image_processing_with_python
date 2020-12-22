# find_edges_image.py

from PIL import Image
from PIL import ImageFilter


def find_edges(input_image, output_image):
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.FIND_EDGES)
    filtered_image.save(output_image)


if __name__ == "__main__":
    find_edges("buffalo.jpg", "buffalo_edges.jpg")
