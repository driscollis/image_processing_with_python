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
        sg.Input(size=(25, 1), enable_events=True, key=key),
        sg.FileSaveAs(file_types=file_types)
    ]
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), enable_events=True, key=key),
        sg.FileBrowse(file_types=file_types),
    ]


def apply_watermark(original_image, values, position, window):
    watermark_with_transparency(
        original_image, tmp_file, values["watermark"], position
    )
    photo_img = convert_image(tmp_file)
    window["image"].update(data=photo_img)


def check_for_errors(values):
    if not values["filename"]:
        sg.Popup("Error", "Image file not loaded!")
        return True
    if not values["watermark"]:
        sg.Popup("Error", "Watermark file not loaded!")
        return True
    if not values["watermark-x"] or not values["watermark-y"]:
        sg.Popup("Error", "Watermark position not set completely")
        return True
    return False

def save_image(values):
    save_filename = sg.popup_get_file(
        "File", file_types=file_types, save_as=True, no_window=True
    )
    if save_filename == values["filename"]:
        sg.popup_error(
            "You are not allowed to overwrite the original image!")
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"Saved: {save_filename}")


def main():
    original_image = None
    elements = [
        [sg.Image(key="image")],
        create_row("Image File:", "filename", file_types),
        create_row("Watermark File:", "watermark",
                   [("PNG (*.png)", "*.png")]),
        [
            sg.Text("Watermark Position"),
            sg.Text("X:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="watermark-x"),
            sg.Text("Y:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="watermark-y"),
        ],
        [sg.Button("Apply Watermark", enable_events=True,
                   key="apply"),
         sg.Button("Save Image", enable_events=True,
                   key="save"),
         ],
    ]

    window = sg.Window("Watermark GUI", elements)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "filename":
            photo_img = convert_image(values["filename"])
            window["image"].update(data=photo_img)
            original_image = values["filename"]
            shutil.copy(original_image, tmp_file)
        if event in ["watermark-x", "watermark-y"]:
            # filter watermark position to integers
            if values["watermark-x"] and values["watermark-y"]:
                if not values["watermark-x"][-1].isdigit():
                    window["watermark-x"].update(values["watermark-x"][:-1])
                if not values["watermark-y"][-1].isdigit():
                    window["watermark-y"].update(values["watermark-y"][:-1])
        if event == "apply":
            if check_for_errors(values):
                continue
            position = (int(values["watermark-x"]),
                        int(values["watermark-y"]))
            apply_watermark(original_image, values, position, window)
        if event == "save" and values["filename"]:
            save_image(values)

    window.close()


if __name__ == "__main__":
    main()
