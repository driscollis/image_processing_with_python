# imagechops_gui.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from add_images import add_images
from apply_hard_light import hard_light
from apply_overlay import overlay
from apply_soft_light import soft_light
from darken_image import darken
from diff_image import diff
from invert_image import invert
from lighten_image import lighten
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]

tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

effects = {
    "Normal": shutil.copy,
    "Addition": add_images,
    "Darken": darken,
    "Lighten": lighten,
    "Difference": diff,
    "Negative": invert,
    "Hard Light": hard_light,
    "Soft Light": soft_light,
    "Overlay": overlay,
}


def apply_effect(values, window):
    selected_effect = values["-EFFECTS-"]
    image_file_one = values["-FILENAME_ONE-"]
    image_file_two = values["-FILENAME_TWO-"]
    if os.path.exists(image_file_one):
        shutil.copy(image_file_one, tmp_file)
        if selected_effect == "Normal":
            effects[selected_effect](image_file_one, tmp_file)
        elif selected_effect == "Negative":
            effects[selected_effect](image_file_one, tmp_file)
        elif os.path.exists(image_file_two):
            effects[selected_effect](image_file_one, image_file_two,
                                     tmp_file)
        elif selected_effect not in ["Normal", "Negative"]:
            sg.popup("You need both images selected to apply "
                     "this effect!")
            return

        image = Image.open(tmp_file)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE-"].update(data=bio.getvalue())


def create_row(label, key, file_types):
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), key=key),
        sg.FileBrowse(file_types=file_types),
    ]


def save_image(filename_one, filename_two):
    save_filename = sg.popup_get_file(
        "File", file_types=file_types, save_as=True, no_window=True
    )
    filenames = [filename_one, filename_two]
    if save_filename in filenames:
        sg.popup_error(
            "You are not allowed to overwrite the original image!")
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"Saved: {save_filename}")


def main():
    effect_names = list(effects.keys())
    layout = [
        [sg.Image(key="-IMAGE-", size=(400, 400))],
        create_row("Image File 1:", "-FILENAME_ONE-", file_types),
        [sg.Button("Load Image")],
        create_row("Image File 2:", "-FILENAME_TWO-", file_types),
        [
            sg.Text("Effect"),
            sg.Combo(
                effect_names, default_value="Normal", key="-EFFECTS-",
                enable_events=True, readonly=True
            ),
        ],
        [sg.Button("Save")],
    ]

    window = sg.Window("ImageChops GUI", layout, size=(450, 500))

    events = ["Load Image", "-FILENAME_TWO-", "-EFFECTS-"]
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in events:
            apply_effect(values, window)
        filename_one = values["-FILENAME_ONE-"]
        filename_two = values["-FILENAME_TWO-"]
        if event == "Save" and filename_one:
            save_image(filename_one, filename_two)

    window.close()


if __name__ == "__main__":
    main()
