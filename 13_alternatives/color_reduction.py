# color_reduction.py

import numpy as np
from PIL import Image


def reduce_colors(input_image_path, output_path):
    image = np.array(Image.open(input_image_path))

    image_32 = image // 32 * 32
    image_128 = image // 128 * 128
    concat_images = np.concatenate((image, image_32, image_128),
                                   axis=1)

    output = Image.fromarray(concat_images)
    output.save(output_path)

if __name__ == "__main__":
    reduce_colors("author.jpg", "reduced_colors.jpg")