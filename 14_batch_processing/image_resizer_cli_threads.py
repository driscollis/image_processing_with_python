# image_resizer_cli.py

import argparse
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from PIL import Image


def get_image_paths(path, recursive):
    if "/" == path[-1]:
        search_path = path + "**/*.png"
    else:
        search_path = path + "/**/*.png"

    image_paths = glob.glob(search_path, recursive=recursive)
    return image_paths


def resize_image(image_path, width, height, output_dir):
    pil_image = Image.open(image_path)
    im_w, im_h = pil_image.size
    image_name = os.path.basename(image_path)
    output = os.path.join(output_dir, image_name)
    if height < im_h or width < im_w:
        pil_image.thumbnail((width, height), Image.ANTIALIAS)
        pil_image.save(output)
        return f"{image_path} converted to {output}"
    else:
        return f"{image_path} size is smaller than new size. Skipping file."


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
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(resize_image, image_path, width, height, output_dir) for
            image_path in image_paths
        ]
        for future in as_completed(futures):
            images_converted += 1
            print(future.result())

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
