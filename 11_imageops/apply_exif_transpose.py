# apply_exif_transpose.py

from PIL import Image, ImageOps


def exif_transpose(image_path, output_path):
    image = Image.open(image_path)

    exif = image.getexif()
    orientation = exif.get(0x0112)
    print(f"Orientation = {orientation}")

    converted_image = ImageOps.exif_transpose(image)
    converted_image.save(output_path)


if __name__ == "__main__":
    exif_transpose("snowman.jpg", "snowman_exif_transposed.jpg")