# image_rotator_gui.py

import PySimpleGUI as sg
import shutil
import tempfile

from mirror_image import mirror
from rotate_image import rotate
from PIL import Image, ImageTk

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
        rotate(image_file, 180, tmp_file)


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

    window = sg.Window("Image Rotator App", elements)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["filename", "effects"]:
            selected_effect = values["effects"]
            image_file = values["filename"]
            if image_file:
                if "Rotate" in selected_effect:
                    apply_rotate(image_file, selected_effect)
                else:
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
