# thumbnail_maker.py

from PIL import Image


def create_thumbnail(
    input_file_path: str, thumbnail_path: str,
    thumbnail_size: tuple[int, int]
) -> None:
    with Image.open(input_file_path) as image:
        image.thumbnail(thumbnail_size)
        image.save(thumbnail_path, "JPEG")


if __name__ == "__main__":
    create_thumbnail("flowers.jpg",
                     "flowers.thumbnail", (128, 128))
