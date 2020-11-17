# unsharp_mask_image.py

from PIL import Image
from PIL import ImageFilter


def unsharp_mask(input_image: str, output_image: str) -> None:
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.UnsharpMask)
    filtered_image.save(output_image)


if __name__ == "__main__":
    unsharp_mask("trex.jpg", "trex_unsharp.jpg")
