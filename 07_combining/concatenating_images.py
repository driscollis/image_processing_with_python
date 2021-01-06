# concatenating_images.py

from PIL import Image


def concatenate_vertically(first_image_path, second_image_path,
                           output_image_path):
    image_one = Image.open(first_image_path)
    image_two = Image.open(second_image_path)
    height = image_one.height + image_two.height
    new_image = Image.new("RGB", (image_one.width, height))

    new_image.paste(image_one, (0, 0))
    new_image.paste(image_two, (0, image_one.height))

    new_image.save(output_image_path)


def concatenate_horizontally(first_image_path, second_image_path,
                             output_image_path):
    image_one = Image.open(first_image_path)
    image_two = Image.open(second_image_path)
    width = image_one.width + image_two.width
    new_image = Image.new("RGB", (width, image_one.height))

    new_image.paste(image_one, (0, 0))
    new_image.paste(image_two, (image_one.width, 0))

    new_image.save(output_image_path)


if __name__ == "__main__":
    coords = (125, 712, 642, 963)
    concatenate_horizontally("silver_falls.jpg",
                             "silver_falls2.jpg",
                             "silver_h_combined.jpg")
    concatenate_vertically("silver_falls.jpg",
                             "silver_falls2.jpg",
                             "silver_v_combined.jpg")
