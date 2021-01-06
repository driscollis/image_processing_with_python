# image_paste.py

from PIL import Image


def paste_demo(image_path, output_path, crop_coords):
    image = Image.open(image_path)
    cropped_image = image.crop(crop_coords)
    image.paste(cropped_image, (0, 0))
    image.save(output_path)


if __name__ == "__main__":
    coords = (125, 712, 642, 963)
    paste_demo("hummingbird.jpg", "hummingbird_pasted.jpg", coords)
