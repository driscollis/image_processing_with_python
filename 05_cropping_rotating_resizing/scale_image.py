# scale_image.py

from PIL import Image


def scale(input_image_path,
          output_image_path,
          width=None,
          height=None):
    image = Image.open(input_image_path)
    w, h = image.size
    print(f"The image size is {w} wide x {h} high")

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError("Width or height required!")

    image.thumbnail(max_size, Image.ANTIALIAS)
    image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print(f"The scaled image size is {width} wide x {height} high")


if __name__ == "__main__":
    scale(
        input_image_path="pilot_knob.jpg",
        output_image_path="pilot_knob_scaled.jpg",
        width=800
    )
