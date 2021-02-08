# watermark_gui.py

import PySimpleGUI as sg
import shutil
import tempfile

from PIL import Image, ImageTk
from watermark_transparent import watermark_with_transparency

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]
tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

def convert_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((400, 400))
    return ImageTk.PhotoImage(image)


def create_row(label, key, file_types, save=False):
    if save:
        return [
        sg.Text(label),
        sg.Input(size=(25, 1), enable_events=True, key=key,
                 readonly=True),
        sg.FileSaveAs(file_types=file_types)
    ]
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), enable_events=True, key=key,
                 readonly=True),
        sg.FileBrowse(file_types=file_types),
    ]


def apply_watermark(original_image, values, position, window):
    watermark_with_transparency(
        original_image, tmp_file, values["-WATERMARK-"], position
    )
    photo_img = convert_image(tmp_file)
    window["-IMAGE-"].update(data=photo_img)


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
        "File", file_types=file_types, save_as=True, no_window=True
    )
    if save_filename == values["-FILENAME-"]:
        sg.popup_error(
            "You are not allowed to overwrite the original image!")
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"Saved: {save_filename}")


def main():
    original_image = None
    layout = [
        [sg.Image(key="-IMAGE-")],
        create_row("Image File:", "-FILENAME-", file_types),
        create_row("Watermark File:", "-WATERMARK-",
                   [("PNG (*.png)", "*.png")]),
        [
            sg.Text("Watermark Position"),
            sg.Text("X:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="-WATERMARK-X-"),
            sg.Text("Y:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="-WATERMARK-Y-"),
        ],
        [sg.Button("Apply Watermark", enable_events=True),
         sg.Button("Save Image", enable_events=True),
         ],
    ]

    window = sg.Window("Watermark GUI", layout, size=(450, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FILENAME-":
            filename = values["-FILENAME-"]
            if filename:
                photo_img = convert_image(values["-FILENAME-"])
                window["-IMAGE-"].update(data=photo_img)
                original_image = values["-FILENAME-"]
                shutil.copy(original_image, tmp_file)
        if event in ["-WATERMARK-X-", "-WATERMARK-Y-"]:
            # filter watermark position to integers
            if values["-WATERMARK-X-"] and values["-WATERMARK-Y-"]:
                if not values["-WATERMARK-X-"][-1].isdigit():
                    window["-WATERMARK-X-"].update(values["-WATERMARK-X-"][:-1])
                if not values["-WATERMARK-Y-"][-1].isdigit():
                    window["-WATERMARK-Y-"].update(values["-WATERMARK-Y-"][:-1])
        if event == "Apply Watermark":
            if check_for_errors(values):
                continue
            position = (int(values["-WATERMARK-X-"]),
                        int(values["-WATERMARK-Y-"]))
            apply_watermark(original_image, values, position, window)
        if event == "Save Image" and values["-FILENAME-"]:
            save_image(values)

    window.close()


if __name__ == "__main__":
    main()
