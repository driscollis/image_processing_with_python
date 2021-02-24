# image_resizer_cli_modular.py

import argparse
import controller


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
        if controller.validate_directory(input_dir):
            image_paths = controller.get_image_paths(
                input_dir, args.recursive)
            controller.resize_images(
                image_paths, args.width, args.height, output_dir)


if __name__ == "__main__":
    main()
