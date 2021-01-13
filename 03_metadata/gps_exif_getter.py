# gps_exif_getter.py

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    info = image.getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value

    gps_info = {}
    for key in exif_table['GPSInfo']:
        decode = GPSTAGS.get(key,key)
        gps_info[decode] = exif_table['GPSInfo'][key]

    if gps_info:
        return gps_info
    else:
        return "No GPS data found!"


if __name__ == "__main__":
    exif = get_exif("jester.jpg")
    print(exif)
