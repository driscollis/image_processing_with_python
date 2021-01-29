# text_gui.py

import glob
import os
import PySimpleGUI as sg
import shutil
import tempfile

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageTk

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]
tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name


def get_value(key, values):
    value = values[key]
    if value:
        return int(value)
    return 0


def apply_text(values, window):
    image_file = values["filename"]
    font_name = values["ttf"]
    font_size = get_value("font_size", values)
    color = values["colors"]
    x, y = get_value("text-x", values), get_value("text-y", values)
    text = values["text"]

    if image_file:
        shutil.copy(image_file, tmp_file)
        image = Image.open(tmp_file)
        image.thumbnail((400, 400))

        if text:
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_name, size=font_size)
            draw.text((x, y), text=text, font=font, fill=color)
            image.save(tmp_file)

        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)


def create_row(label, key, file_types):
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), enable_events=True, key=key),
        sg.FileBrowse(file_types=file_types),
    ]


def get_ttf_files():
    ttf_files = glob.glob("*.ttf")
    ttf_dict = {}
    for ttf in ttf_files:
        ttf_dict[os.path.basename(ttf)] = ttf
    return ttf_dict


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
    colors = list(ImageColor.colormap.keys())
    ttf_files = get_ttf_files()
    ttf_filenames = list(ttf_files.keys())

    elements = [
        [sg.Image(key="image")],
        create_row("Image File:", "filename", file_types),
        [sg.Text("Text:"), sg.Input(key="text", enable_events=True)],
        [
            sg.Text("Text Position"),
            sg.Text("X:"),
            sg.Input("10", size=(5, 1), enable_events=True,
                     key="text-x"),
            sg.Text("Y:"),
            sg.Input("10", size=(5, 1), enable_events=True,
                     key="text-y"),
        ],
        [
            sg.Combo(colors, default_value=colors[0], key='colors',
                     enable_events=True),
            sg.Combo(ttf_filenames, default_value=ttf_filenames[0], key='ttf',
                     enable_events=True),
            sg.Text("Font Size:"),
            sg.Input("12", size=(5, 1), key="font_size", enable_events=True),

        ],
        [sg.Button("Save Image", enable_events=True,
                   key="save")],
    ]

    window = sg.Window("Draw Text GUI", elements)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["filename", "colors", "ttf", "font_size",
                     "text-x", "text-y", "text"]:
            apply_text(values, window)
        if event == "save" and values["filename"]:
            save_image(values)

    window.close()

if __name__ == "__main__":
    main()