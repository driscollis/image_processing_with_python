# gaussian_blur_image.py

from PIL import Image
from PIL import ImageFilter


def gaussian_blur(input_image: str, output_image: str) -> None:
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.GaussianBlur)
    filtered_image.save(output_image)


if __name__ == "__main__":
    gaussian_blur("trex.jpg", "trex_gauss.jpg")
