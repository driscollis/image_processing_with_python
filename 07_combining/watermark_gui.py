# watermark_gui.py

import PySimpleGUI as sg
from PIL import Image, ImageTk
from watermark_transparent import watermark_with_transparency

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]


def convert_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((400, 400))
    return ImageTk.PhotoImage(image)


def create_row(label, key, file_types):
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), enable_events=True, key=key),
        sg.FileBrowse(file_types=file_types),
    ]


def apply_watermark(original_image, values, position, window):
    if original_image != values["output"]:
        watermark_with_transparency(
            original_image, values["output"], values["watermark"], position
        )
        photo_img = convert_image(values["output"])
        window["image"].update(data=photo_img)
    else:
        sg.Popup("Error", "Output path cannot match input file path!")


def check_for_errors(values):
    if not values["file"]:
        sg.Popup("Error", "Image file not loaded!")
        return True
    if not values["watermark"]:
        sg.Popup("Error", "Watermark file not loaded!")
        return True
    if not values["watermark-x"] or not values["watermark-y"]:
        sg.Popup("Error", "Watermark position not set completely")
        return True
    if not values["output"]:
        sg.Popup("Error", "Output file not specified!")
        return True
    return False


def main():
    original_image = None
    elements = [
        [sg.Image(key="image")],
        create_row("Image File:", "file", file_types),
        create_row("Watermark File:", "watermark",
                   [("PNG (*.png)", "*.png")]),
        create_row("Output File:", "output", file_types),
        [
            sg.Text("Watermark Position"),
            sg.Text("X:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="watermark-x"),
            sg.Text("Y:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="watermark-y"),
        ],
        [sg.Button("Apply Watermark", enable_events=True,
                   key="apply")],
    ]

    window = sg.Window("Watermark GUI", elements)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "file":
            photo_img = convert_image(values["file"])
            window["image"].update(data=photo_img)
            original_image = values["file"]
        if event in ["watermark-x", "watermark-y"]:
            # filter watermark position to integers
            if values["watermark-x"] and values["watermark-y"]:
                if not values["watermark-x"][-1].isdigit():
                    window["watermark-x"].update(values["watermark-x"][:-1])
                if not values["watermark-y"][-1].isdigit():
                    window["watermark-y"].update(values["watermark-y"][:-1])
        if event == "apply":
            if check_for_errors(values):
                continue
            position = (int(values["watermark-x"]),
                        int(values["watermark-y"]))
            apply_watermark(original_image, values, position, window)

    window.close()


if __name__ == "__main__":
    main()
