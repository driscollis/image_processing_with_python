# invert.py

import numpy as np
from PIL import Image


def invert(input_image_path, output_path):
    image = np.array(Image.open(input_image_path))

    inverted_image = 255 - image

    output = Image.fromarray(inverted_image)
    output.save(output_path)

if __name__ == "__main__":
    invert("author.jpg", "inverted.jpg")