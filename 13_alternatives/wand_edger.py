# wand_edger.py

from wand.image import Image


def edge(input_image_path, output_path):
    with Image(filename=input_image_path) as img:
        img.transform_colorspace("gray")
        img.edge(radius=3)
        img.save(filename=output_path)

if __name__ == "__main__":
    edge("ducklings.jpg", "edged.jpg")