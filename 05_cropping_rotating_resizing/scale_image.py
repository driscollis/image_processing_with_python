# scale_image.py

from PIL import Image
from typing import Optional


def scale(input_image_path: str,
          output_image_path: str,
          width: Optional[int] = None,
          height: Optional[int] = None) -> None:
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print(
        "The original image size is {wide} wide x {height} "
        "high".format(wide=w, height=h)
    )

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError("Width or height required!")

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print(
        "The scaled image size is {wide} wide x {height} "
        "high".format(wide=width, height=height)
    )


if __name__ == "__main__":
    scale(
        input_image_path="pilot_knob.jpg",
        output_image_path="pilot_knob_scaled.jpg",
        width=800
    )
