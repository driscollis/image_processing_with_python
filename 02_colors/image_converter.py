# image_converter.py

import PySimpleGUI as sg
import shutil
import tempfile

from create_bw import black_and_white
from create_grayscale import grayscale
from create_sepia import create_sepia as sepia
from PIL import Image, ImageTk

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
    elements = [
        [sg.Image(key="image")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="filename"),
            sg.FileBrowse(file_types=file_types),
        ],
        [
            sg.Text("Effect"),
            sg.Combo(
                effect_names, default_value="Normal", key="effects",
                enable_events=True
            ),
        ],
        [sg.Button("Save", key="save")],
    ]

    window = sg.Window("Image Converter", elements)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["filename", "effects"]:
            selected_effect = values["effects"]
            image_file = values["filename"]
            if image_file:
                effects[selected_effect](image_file, tmp_file)
                image = Image.open(tmp_file)
                image.thumbnail((400, 400))
                photo_img = ImageTk.PhotoImage(image)
                window["image"].update(data=photo_img)
        if event == "save" and values["filename"]:
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

    window.close()


if __name__ == "__main__":
    main()
