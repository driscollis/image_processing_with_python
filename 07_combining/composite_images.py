# composite_images.py

from PIL import Image


def composite_image(input_image_path, input_image_path_2, output_path):
    image1 = Image.open(input_image_path)
    image2 = Image.open(input_image_path_2).resize(image1.size)
    mask = Image.new("L", image1.size, 120)
    composited_images = Image.composite(image1, image2, mask)
    composited_images.save(output_path)


if __name__ == "__main__":
    composite_image("pilot_knob.jpg", "grasshopper.jpg", "composited.jpg")