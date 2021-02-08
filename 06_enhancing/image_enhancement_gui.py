# image_enhancer_gui.py

import PySimpleGUI as sg
import shutil
import tempfile

from enhance_brightness import enhance_brightness
from enhance_color import enhance_color
from enhance_contrast import enhance_contrast
from enhance_sharpness import enhance_sharpness
from PIL import Image, ImageTk

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]

tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name

effects = {
    "Normal": shutil.copy,
    "Brightness": enhance_brightness,
    "Color": enhance_color,
    "Contrast": enhance_contrast,
    "Sharpness": enhance_sharpness
}

def apply_effect(values, window):
    selected_effect = values["-EFFECTS-"]
    image_file = values["-FILENAME-"]
    factor = values["-FACTOR-"]
    if image_file:
        if selected_effect == "Normal":
            effects[selected_effect](image_file, tmp_file)
        else:
            effects[selected_effect](image_file, factor, tmp_file)

        image = Image.open(tmp_file)
        image.thumbnail((400, 400))
        photo_img = ImageTk.PhotoImage(image)
        window["-IMAGE-"].update(data=photo_img)


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
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="-FILENAME-",
                     readonly=True),
            sg.FileBrowse(file_types=file_types),
        ],
        [
            sg.Text("Effect"),
            sg.Combo(
                effect_names, default_value="Normal", key="-EFFECTS-",
                enable_events=True, readonly=True
            ),
            sg.Slider(range=(0, 5), default_value=2, resolution=0.1,
                      orientation="h", enable_events=True, key="-FACTOR-"),
        ],
        [sg.Button("Save")],
    ]

    window = sg.Window("Image Enhancer", layout, size=(450, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["-FILENAME-", "-EFFECTS-", "-FACTOR-"]:
            apply_effect(values, window)
        if event == "Save" and values["-FILENAME-"]:
            save_image(values)

    window.close()


if __name__ == "__main__":
    main()
