# blend_images.py

from PIL import Image


def blend(input_image_path, input_image_path_2, output_path, alpha):
    image1 = Image.open(input_image_path).convert("RGBA")
    image2 = Image.open(input_image_path_2).convert("RGBA")
    if image1.size != image2.size:
        print("ERROR: Images are not the same size!")
        return
    blended_image = Image.blend(image1, image2, alpha)
    blended_image.save(output_path)

if __name__ == "__main__":
    blend("skyline.png", "shell.png", "blended.png", alpha=0.4)
