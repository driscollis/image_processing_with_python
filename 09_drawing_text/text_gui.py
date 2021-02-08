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
    if value.isdigit():
        return int(value)
    return 0


def apply_text(values, window):
    image_file = values["-FILENAME-"]
    font_name = values["-TTF-"]
    font_size = get_value("-FONT_SIZE-", values)
    color = values["-COLORS-"]
    x, y = get_value("-TEXT-X-", values), get_value("-TEXT-Y-", values)
    text = values["-TEXT-"]

    if image_file and os.path.exists(image_file):
        shutil.copy(image_file, tmp_file)
        image = Image.open(tmp_file)
        image.thumbnail((400, 400))

        if text:
            draw = ImageDraw.Draw(image)
            if font_name == "Default Font":
                font = None
            else:
                font = ImageFont.truetype(font_name, size=font_size)
            draw.text((x, y), text=text, font=font, fill=color)
            image.save(tmp_file)

        photo_img = ImageTk.PhotoImage(image)
        window["-IMAGE-"].update(data=photo_img)


def create_row(label, key, file_types):
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), enable_events=True, key=key,
                 readonly=True),
        sg.FileBrowse(file_types=file_types),
    ]


def get_ttf_files(directory=None):
    if directory is not None:
        ttf_files = glob.glob(directory + "/*.ttf")
    else:
        ttf_files = glob.glob("*.ttf")
    if not ttf_files:
        return {"Default Font": None}
    ttf_dict = {}
    for ttf in ttf_files:
        ttf_dict[os.path.basename(ttf)] = ttf
    return ttf_dict


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


def update_ttf_values(window):
    directory = sg.popup_get_folder("Get TTF Directory")
    if directory is not None:
        ttf_files = get_ttf_files(directory)
        new_values = list(ttf_files.keys())
        window["-TTF-"].update(values=new_values,
                             value=new_values[0])


def main():
    colors = list(ImageColor.colormap.keys())
    ttf_files = get_ttf_files()
    ttf_filenames = list(ttf_files.keys())

    menu_items = [["File", ["Open Font Directory"]]]

    elements = [
        [sg.Menu(menu_items)],
        [sg.Image(key="-IMAGE-")],
        create_row("Image File:", "-FILENAME-", file_types),
        [sg.Text("Text:"), sg.Input(key="-TEXT-", enable_events=True)],
        [
            sg.Text("Text Position"),
            sg.Text("X:"),
            sg.Input("10", size=(5, 1), enable_events=True,
                     key="-TEXT-X-"),
            sg.Text("Y:"),
            sg.Input("10", size=(5, 1), enable_events=True,
                     key="-TEXT-Y-"),
        ],
        [
            sg.Combo(colors, default_value=colors[0], key='-COLORS-',
                     enable_events=True, readonly=True),
            sg.Combo(ttf_filenames, default_value=ttf_filenames[0],
                     key='-TTF-', enable_events=True, readonly=True),
            sg.Text("Font Size:"),
            sg.Input("12", size=(5, 1), key="-FONT_SIZE-", enable_events=True),

        ],
        [sg.Button("Save Image", enable_events=True)],
    ]

    window = sg.Window("Draw Text GUI", elements, size=(500, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["-FILENAME-", "-COLORS-", "-TTF-", "-FONT_SIZE-",
                     "-TEXT-X-", "-TEXT-Y-", "-TEXT-"]:
            apply_text(values, window)
        if event == "Save Image" and values["-FILENAME-"]:
            save_image(values)
        if event == "Open Font Directory":
            update_ttf_values(window)

    window.close()

if __name__ == "__main__":
    main()