# drawing_gui.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from PIL import Image, ImageColor, ImageDraw

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]
tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name


def get_value(key, values):
    value = values[key]
    if value.isdigit():
        return int(value)
    return 0


def apply_drawing(values, window):
    image_file = values["-FILENAME-"]
    shape = values["-SHAPES-"]
    begin_x = get_value("-BEGIN_X-", values)
    begin_y = get_value("-BEGIN_Y-", values)
    end_x = get_value("-END_X-", values)
    end_y = get_value("-END_Y-", values)
    width = get_value("-WIDTH-", values)
    fill_color = values["-FILL_COLOR-"]
    outline_color = values["-OUTLINE_COLOR-"]

    if os.path.exists(image_file):
        shutil.copy(image_file, tmp_file)
        image = Image.open(tmp_file)
        image.thumbnail((400, 400))
        draw = ImageDraw.Draw(image)
        if shape == "Ellipse":
            draw.ellipse(
                (begin_x, begin_y, end_x, end_y),
                fill=fill_color,
                width=width,
                outline=outline_color,
            )
        elif shape == "Rectangle":
            draw.rectangle(
                (begin_x, begin_y, end_x, end_y),
                fill=fill_color,
                width=width,
                outline=outline_color,
            )
        image.save(tmp_file)

        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE-"].update(data=bio.getvalue())


def create_coords_elements(label, begin_x, begin_y, key1, key2):
    return [
        sg.Text(label),
        sg.Input(begin_x, size=(5, 1), key=key1, enable_events=True),
        sg.Input(begin_y, size=(5, 1), key=key2, enable_events=True),
    ]


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
    colors = list(ImageColor.colormap.keys())
    layout = [
        [sg.Image(key="-IMAGE-", size=(400, 400))],
        [
            sg.Text("Image File"),
            sg.Input(
                size=(25, 1), key="-FILENAME-"
            ),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [
            sg.Text("Shapes"),
            sg.Combo(
                ["Ellipse", "Rectangle"],
                default_value="Ellipse",
                key="-SHAPES-",
                enable_events=True,
                readonly=True,
            ),
        ],
        [
            *create_coords_elements(
                "Begin Coords", "10", "10", "-BEGIN_X-", "-BEGIN_Y-"
            ),
            *create_coords_elements(
                "End Coords", "100", "100", "-END_X-", "-END_Y-"
            ),
        ],
        [
            sg.Text("Fill"),
            sg.Combo(
                colors,
                default_value=colors[0],
                key="-FILL_COLOR-",
                enable_events=True,
                readonly=True
            ),
            sg.Text("Outline"),
            sg.Combo(
                colors,
                default_value=colors[0],
                key="-OUTLINE_COLOR-",
                enable_events=True,
                readonly=True
            ),
            sg.Text("Width"),
            sg.Input("3", size=(5, 1), key="-WIDTH-", enable_events=True),
        ],
        [sg.Button("Save")],
    ]

    window = sg.Window("Drawing GUI", layout, size=(450, 500))

    events = [
        "Load Image",
        "-BEGIN_X-",
        "-BEGIN_Y-",
        "-END_X-",
        "-END_Y-",
        "-FILL_COLOR-",
        "-OUTLINE_COLOR-",
        "-WIDTH-",
        "-SHAPES-",
    ]
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in events:
            apply_drawing(values, window)
        if event == "Save" and values["-FILENAME-"]:
            save_image(values)
    window.close()


if __name__ == "__main__":
    main()
