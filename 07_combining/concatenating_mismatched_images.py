# concatenating_mismatched_images.py

from PIL import Image


def concatenate_vertically(first_image_path, second_image_path,
                           output_image_path):
    image_one = Image.open(first_image_path)
    image_two = Image.open(second_image_path)
    height = image_one.height + image_two.height
    width = min(image_one.width, image_two.width)
    new_image = Image.new("RGB", (width, height))

    new_image.paste(image_one, (0, 0))
    new_image.paste(image_two, (0, image_one.height))

    new_image.save(output_image_path)


def concatenate_horizontally(first_image_path, second_image_path,
                             output_image_path):
    image_one = Image.open(first_image_path)
    image_two = Image.open(second_image_path)
    width = image_one.width + image_two.width
    height = min(image_one.height, image_two.height)
    new_image = Image.new("RGB", (width, height))

    new_image.paste(image_one, (0, 0))
    new_image.paste(image_two, (image_one.width, 0))

    new_image.save(output_image_path)


if __name__ == "__main__":
    coords = (125, 712, 642, 963)
    concatenate_horizontally("hummingbird.jpg",
                             "silver_falls2.jpg",
                             "h_combined.jpg")
    concatenate_vertically("hummingbird.jpg",
                            "silver_falls2.jpg",
                            "v_combined.jpg")
