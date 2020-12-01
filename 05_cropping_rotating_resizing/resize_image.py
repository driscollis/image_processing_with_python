# resize_image.py

from PIL import Image


def resize(input_image_path: str,
           output_image_path: str,
           size: tuple[int, int]) -> None:
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} high")

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f"The resized image size is {width} wide x {height} high")
    resized_image.save(output_image_path)


if __name__ == "__main__":
    resize(
        input_image_path="pilot_knob.jpg",
        output_image_path="pilot_knob_small.jpg",
        size=(800, 400),
    )
