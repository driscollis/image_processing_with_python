# wand_vignette.py

from wand.image import Image


def vignette(input_image_path, output_path):
    with Image(filename=input_image_path) as img:
        img.vignette(x=10, y=10)
        img.save(filename=output_path)


if __name__ == "__main__":
    vignette("author.jpg", "vignette.jpg")