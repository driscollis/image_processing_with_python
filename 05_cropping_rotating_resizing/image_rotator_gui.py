# image_rotator_gui.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from mirror_image import mirror
from rotate_image import rotate
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

effects = {
    "Normal": shutil.copy,
    "Rotate 90": None,
    "Rotate 180": None,
    "Rotate 270": None,
    "Mirror": mirror,
    }

def apply_rotate(image_file, effect):
    if effect == "Rotate 90":
        rotate(image_file, 90, tmp_file)
    elif effect == "Rotate 180":
        rotate(image_file, 180, tmp_file)
    elif effect == "Rotate 270":
        rotate(image_file, 270, tmp_file)


def apply_effect(values, window):
    selected_effect = values["-EFFECTS-"]
    image_file = values["-FILENAME-"]
    if os.path.exists(image_file):
        if "Rotate" in selected_effect:
            apply_rotate(image_file, selected_effect)
        else:
            effects[selected_effect](image_file, tmp_file)
        image = Image.open(tmp_file)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE-"].update(data=bio.getvalue(), size=(400, 400))


def save_image(image_filename):
    save_filename = sg.popup_get_file(
        "File", file_types=file_types, save_as=True, no_window=True,
        )
    if save_filename == image_filename:
        sg.popup_error(
            "You are not allowed to overwrite the original image!",
            )
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"Saved: {save_filename}")


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
                enable_events=True, readonly=True,
                ),
        ],
        [sg.Button("Save")],
    ]

    window = sg.Window("Image Rotator App", layout, size=(450, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["Load Image", "-EFFECTS-"]:
            apply_effect(values, window)
        image_filename = values["-FILENAME-"]
        if event == "Save" and image_filename:
            save_image(image_filename)

    window.close()


if __name__ == "__main__":
    main()
