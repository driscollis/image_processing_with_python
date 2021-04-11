# imageops_gui.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from apply_autocontrast import autocontrast
from apply_equalize import equalize
from apply_flip import flip
from apply_invert import invert
from apply_mirror import mirror
from apply_solarize import solarize
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]
tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

effects = {
    "Normal": shutil.copy,
    "Autocontrast": autocontrast,
    "Equalize": equalize,
    "Flip": flip,
    "Mirror": mirror,
    "Negative": invert,
    "Solarize": solarize,
    }


def apply_effect(image_file_one, effect, image_obj):
    if os.path.exists(image_file_one):
        effects[effect](image_file_one, tmp_file)
        image = Image.open(tmp_file)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        image_obj.update(data=bio.getvalue(), size=(400,400))


def create_row(label, key, file_types):
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), key=key),
        sg.FileBrowse(file_types=file_types),
        ]


def save_image(filename_one):
    save_filename = sg.popup_get_file(
        "File", file_types=file_types, save_as=True, no_window=True,
        )
    if save_filename == filename_one:
        sg.popup_error("You are not allowed to overwrite the original image!")
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"Saved: {save_filename}")


def main():
    effect_names = list(effects.keys())
    layout = [
        [sg.Image(key="-IMAGE-", size=(400,400))],
        create_row("Image File 1:", "-FILENAME_ONE-", file_types),
        [sg.Button("Load Image")],
        [
            sg.Text("Effect"),
            sg.Combo(
                effect_names,
                default_value="Normal",
                key="-EFFECTS-",
                enable_events=True,
                readonly=True,
                ),
        ],
        [sg.Button("Save")],
    ]

    window = sg.Window("ImageOps GUI", layout, size=(450, 550))
    image = window["-IMAGE-"]

    events = ("Load Image", "-EFFECTS-")
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        filename_one = values["-FILENAME_ONE-"]
        effect = values["-EFFECTS-"]

        if event in events:
            apply_effect(filename_one, effect, image)
        if event == "Save" and filename_one:
            save_image(filename_one)

    window.close()


if __name__ == "__main__":
    main()