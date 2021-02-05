# apply_autocontrast.py

from PIL import Image, ImageOps

def autocontrast(image_path, output_path, cutoff=0,
                 ignore=None):
    image = Image.open(image_path)
    converted_image = ImageOps.autocontrast(image)
    converted_image.save(output_path)


if __name__ == "__main__":
    autocontrast("ducklings.jpg", "autocontrast.jpg",
                 cutoff=0.5)