# tiff_metadata.py

from PIL import Image
from PIL.TiffTags import TAGS


def get_metadata(image_file_path):
    image = Image.open(image_file_path)
    metadata = {}
    for tag in image.tag.items():
        metadata[TAGS.get(tag[0])] = tag[1]
    return metadata


if __name__ == "__main__":
    metadata = get_metadata("reportlab_cover.tiff")
    print(metadata)
