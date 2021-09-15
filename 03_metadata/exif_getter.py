# exif_getter.py

from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    info = image._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
    return exif_table


if __name__ == "__main__":
    exif = get_exif("bridge.JPG")
    print(exif)
