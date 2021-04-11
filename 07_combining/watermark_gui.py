# watermark_gui.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from PIL import Image
from watermark_transparent import watermark_with_transparency

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]
tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

def convert_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((400, 400))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    return bio.getvalue()


def create_row(label, key, file_types, save=False):
    if save:
        return [
                sg.Text(label),
                sg.Input(size=(25, 1), key=key),
                sg.FileSaveAs(file_types=file_types),
                ]
    else:
        return [
                sg.Text(label),
                sg.Input(size=(25, 1), key=key),
                sg.FileBrowse(file_types=file_types),
                ]


def apply_watermark(original_image, values, position, window):
    watermark_with_transparency(
            original_image, tmp_file, values["-WATERMARK-"], position,
            )
    photo_img = convert_image(tmp_file)
    window["-IMAGE-"].update(data=photo_img, size=(400,400))


def check_for_errors(values):
    if not values["-FILENAME-"]:
        sg.Popup("Error", "Image file not loaded!")
        return True
    if not values["-WATERMARK-"]:
        sg.Popup("Error", "Watermark file not loaded!")
        return True
    if not values["-WATERMARK-X-"] or not values["-WATERMARK-Y-"]:
        sg.Popup("Error", "Watermark position not set completely")
        return True
    return False


def save_image(values):
    save_filename = sg.popup_get_file(
            "File", file_types=file_types, save_as=True, no_window=True,
            )
    if save_filename == values["-FILENAME-"]:
        sg.popup_error(
                "You are not allowed to overwrite the original image!",
                )
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"Saved: {save_filename}")


def main():
    original_image = None
    layout = [
        [sg.Image(key="-IMAGE-", size=(400,400))],
        create_row("Image File:", "-FILENAME-", file_types),
        create_row("Watermark File:", "-WATERMARK-",
                   [("PNG (*.png)", "*.png")]),
        [sg.Button("Load Image")],
        [
            sg.Text("Watermark Position"),
            sg.Text("X:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="-WATERMARK-X-"),
            sg.Text("Y:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="-WATERMARK-Y-"),
        ],
        [
            sg.Button("Apply Watermark", enable_events=True),
            sg.Button("Save Image", enable_events=True),
        ],
    ]

    window = sg.Window("Watermark GUI", layout, size=(450, 600))

    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
        watermark_x = values["-WATERMARK-X-"]
        watermark_y = values["-WATERMARK-Y-"]

        if event == "Load Image":
            filename = values["-FILENAME-"]
            if os.path.exists(filename):
                photo_img = convert_image(filename)
                window["-IMAGE-"].update(data=photo_img, size=(400,400))
                original_image = filename
                shutil.copy(original_image, tmp_file)
        if event in ["-WATERMARK-X-", "-WATERMARK-Y-"]:
            # filter watermark position to integers
            if watermark_x and watermark_y:
                if not watermark_x[-1].isdigit():
                    window["-WATERMARK-X-"].update(watermark_x[:-1])
                if not watermark_y[-1].isdigit():
                    window["-WATERMARK-Y-"].update(watermark_y[:-1])
        if event == "Apply Watermark":
            if check_for_errors(values):
                continue
            position = (int(watermark_x), int(watermark_y))
            apply_watermark(original_image, values, position, window)
        if event == "Save Image" and values["-FILENAME-"]:
            save_image(values)

    window.close()


if __name__ == "__main__":
    main()