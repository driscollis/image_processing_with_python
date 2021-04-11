# image_converter.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from create_bw import black_and_white
from create_grayscale import grayscale
from create_sepia import create_sepia as sepia
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]

tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

effects = {
    "Normal": shutil.copy,
    "Black and White": black_and_white,
    "Grayscale": grayscale,
    "Sepia": sepia,
    }


def main():
    effect_names = list(effects.keys())
    layout = [
        [sg.Image(key="-IMAGE-", size=(400,400))],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILENAME-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image")
        ],
        [
            sg.Text("Effect"),
            sg.Combo(
                effect_names, default_value="Normal", key="-EFFECTS-",
                enable_events=True, readonly=True
                ),
        ],
        [sg.Button("Save")],
    ]

    window = sg.Window("Image Converter", layout, size=(450, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["Load Image", "-EFFECTS-"]:
            selected_effect = values["-EFFECTS-"]
            image_file = values["-FILENAME-"]
            if image_file:
                effects[selected_effect](image_file, tmp_file)
                image = Image.open(tmp_file)
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue(), size=(400,400))
        if event == "Save" and values["-FILENAME-"]:
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

    window.close()


if __name__ == "__main__":
    main()