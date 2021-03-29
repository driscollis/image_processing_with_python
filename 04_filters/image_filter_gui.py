# image_filter_gui.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from blur_image import blur
from contour_image import contour
from detail_image import detail
from edge_enhance_image import edge_enhance
from emboss_image import emboss
from find_edges_image import find_edges
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]

tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

effects = {
    "Normal": shutil.copy,
    "Blur": blur,
    "Contour": contour,
    "Detail": detail,
    "Edge Enhance": edge_enhance,
    "Emboss": emboss,
    "Find Edges": find_edges,
}

def apply_effect(values, window):
    selected_effect = values["-EFFECTS-"]
    image_file = values["-FILENAME-"]
    if os.path.exists(image_file):
        effects[selected_effect](image_file, tmp_file)
        image = Image.open(tmp_file)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE-"].update(data=bio.getvalue())


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
    effect_names = list(effects.keys())
    layout = [
        [sg.Image(key="-IMAGE-", size=(400, 400))],
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

    window = sg.Window("Image Filter App", layout, size=(450, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["Load Image", "-EFFECTS-"]:
            apply_effect(values, window)
        if event == "Save" and values["-FILENAME-"]:
            save_image(values)

    window.close()


if __name__ == "__main__":
    main()
