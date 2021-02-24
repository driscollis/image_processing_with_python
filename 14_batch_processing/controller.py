# controller.py

import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from PIL import Image


def get_image_paths(path, recursive, file_format="png"):
    if "/" == path[-1]:
        search_path = path + f"**/*.{file_format}"
    else:
        search_path = path + f"/**/*.{file_format}"

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
            executor.submit(resize_image, image_path, width, height,
                            output_dir) for
            image_path in image_paths
        ]
        for future in as_completed(futures):
            result = future.result()
            if "Skipping" not in result:
                images_converted += 1
            print(result)

    end = time.time()
    print(f"Converted {images_converted} image(s) in {end-start} seconds.")
    print(f"Output folder is: {output_dir}")


def validate_directory(path):
    if not os.path.isdir(path):
        print(f"{path} is not a directory")
        return False
    return True