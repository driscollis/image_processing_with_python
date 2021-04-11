# image_resizer_cli.py

import argparse
import glob
import os
import time

from PIL import Image


def get_image_paths(search_path, recursive):
    if "/" != search_path[-1]:
        search_path += "/"
    if recursive:
        search_path += "**/"
    search_path += "*.png"
    image_paths = glob.glob(search_path, recursive=recursive)
    return image_paths


def resize_images(image_paths, width, height, output_dir):
    start = time.time()
    if width is None:
        width = height
    if height is None:
        height = width

    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError:
            print(f"Error creating {output_dir}")
            return

    images_converted = 0
    for image_path in image_paths:
        pil_image = Image.open(image_path)
        im_w, im_h = pil_image.size
        image_name = os.path.basename(image_path)
        output = os.path.join(output_dir, image_name)
        if height < im_h or width < im_w:
            # convert image and inform user
            pil_image.thumbnail((width, height), Image.ANTIALIAS)
            print(f"{image_path} converted to {output}")
            images_converted += 1
        else:
            # do not convert image, and inform user
            print(f"{image_path} size is smaller than new size. Skipping file.")
        # save (converted) image to destination directory
        pil_image.save(output)
    end = time.time()
    print(f"Converted {images_converted} image(s) in {end-start} seconds.")
    print(f"Output folder is: {output_dir}")


def validate_directory(path):
    if not os.path.isdir(path):
        print(f"{path} is not a directory")
        return False
    return True


def main():
    parser = argparse.ArgumentParser("Image Resizer")
    parser.add_argument("-i", "--infolder", help="Input folder",
                        required=True, dest="input_dir")
    parser.add_argument("-r", "--recursive",
                        help="Search sub-folders recursively",
                        dest="recursive", default=False,
                        action="store_true")
    parser.add_argument("--height",
                        help="The new height the image should be",
                        dest="height", type=int)
    parser.add_argument("--width",
                        help="The new width the image should be",
                        dest="width", type=int)
    parser.add_argument("-o", "--out", help="Output folder",
                        required=True, dest="output_dir")
    args = parser.parse_args()

    if args.width is None and args.height is None:
        print("You need to specify width or height or both")
        return

    input_dir = args.input_dir
    output_dir = args.output_dir

    if input_dir == output_dir:
        print("The output folder cannot be the same as the input")
        return
    else:
        if validate_directory(input_dir):
            image_paths = get_image_paths(input_dir, args.recursive)
            resize_images(image_paths, args.width, args.height,
                          output_dir)


if __name__ == "__main__":
    main()