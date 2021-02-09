# apply_fit.py

from PIL import Image, ImageOps


def fit(image_path, output_path, size, centering=(0.5, 0.5)):
    image = Image.open(image_path)
    converted_image = ImageOps.fit(image, size, centering=centering)
    converted_image.save(output_path)


if __name__ == "__main__":
    fit("flowers.jpg", "flowers_fitted.jpg", size=(400, 400))