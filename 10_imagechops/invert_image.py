# invert_image.py

from PIL import Image, ImageChops

def invert(image_path, output_path):
    image = Image.open(image_path)
    inverted_image = ImageChops.invert(image)
    inverted_image.save(output_path)


if __name__ == "__main__":
    invert("yellow_butterfly.jpg", "inverted.jpg")