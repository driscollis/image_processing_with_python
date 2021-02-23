# concatenating.py

import numpy as np
from PIL import Image


def concatenate(input_image_path, output_path):
    image = np.array(Image.open(input_image_path))

    red = image.copy()
    red[:, :, (1, 2)] = 0

    green = image.copy()
    green[:, :, (0, 2)] = 0

    blue = image.copy()
    blue[:, :, (0, 1)] = 0

    rgb = np.concatenate((red, green, blue), axis=1)
    output = Image.fromarray(rgb)
    output.save(output_path)

if __name__ == "__main__":
    concatenate("author.jpg", "concatenated.jpg")