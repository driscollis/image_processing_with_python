# drawing_gui.py

import PySimpleGUI as sg
import shutil
import tempfile

from PIL import Image, ImageColor, ImageDraw, ImageTk

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]
tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name


def get_value(key, values):
    value = values[key]
    if value:
        return int(value)
    return 0

def apply_drawing(values, window):
    image_file = values["filename"]
    shape = values["shapes"]
    begin_x = get_value("begin_x", values)
    begin_y = get_value("begin_y", values)
    end_x = get_value("end_x", values)
    end_y = get_value("end_y", values)
    width = get_value("width", values)
    fill_color = values["fill_color"]
    outline_color = values["outline_color"]

    shutil.copy(image_file, tmp_file)

    if image_file:
        image = Image.open(tmp_file)
        image.thumbnail((400, 400))
        draw = ImageDraw.Draw(image)
        if shape == "Ellipse":
            draw.ellipse((begin_x, begin_y, end_x, end_y),
                         fill=fill_color, width=width,
                         outline=outline_color)
        elif shape == "Rectangle":
            draw.rectangle((begin_x, begin_y, end_x, end_y),
                           fill=fill_color, width=width,
                           outline=outline_color)

        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)

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
    if save_filename == values["filename"]:
        sg.popup_error(
            "You are not allowed to overwrite the original image!")
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"Saved: {save_filename}")


def main():
    colors = list(ImageColor.colormap.keys())
    elements = [
        [sg.Image(key="image")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="filename"),
            sg.FileBrowse(file_types=file_types),
        ],
        [
            sg.Text("Shapes"),
            sg.Combo(
                ["Ellipse", "Rectangle"], default_value="Ellipse",
                key="shapes", enable_events=True
            ),

        ],
        [
            *create_coords_elements("Begin Coords", "10", "10",
                                    "begin_x", "begin_y"),
            *create_coords_elements("End Coords", "100", "100",
                                    "end_x", "end_y"),
        ],
        [
            sg.Text("Fill"),
            sg.Combo(colors, default_value=colors[0], key='fill_color',
                     enable_events=True),
            sg.Text("Outline"),
            sg.Combo(colors, default_value=colors[0], key='outline_color',
                     enable_events=True),
            sg.Text("Width"),
            sg.Input("3", size=(5, 1), key="width", enable_events=True)

        ],
        [sg.Button("Save", key="save")],
    ]

    window = sg.Window("Drawing GUI", elements)

    events = ["filename", "begin_x", "begin_y", "end_x", "end_y",
              "fill_color", "outline_color", "width", "shapes"]
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in events:
            apply_drawing(values, window)
    window.close()

if __name__ == "__main__":
    main()